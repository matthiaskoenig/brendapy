
"""
    Module for loading the BRENDA gene information
    
    Load the full gene information data for all entries.
    The fasta data can be reached on the BRENDA network
    
    1. get all available ec numbers (parse brenda data for id entries)
    2. get all gene fasta data for all these ec numbers
    3. generate BRENDA gene objects
    
    The Gene information is saved as local files for all ec numbers.
    
    The gene information is loaded after the BRENDA enzyme information is 
    parsed. For every Enzyme object in the modell the full BRENDA gene 
    information is parsed.
    
    author: Matthias Koenig
    version: 0.1
    date: 06.06.08
"""
import tools.equationTools as equationTools
import tools.taxonomy
import files
import urllib
import re

# Location of the local files
genes_location = files.BRENDAgenes

class BRENDAGene(object):
    """ Class represents one BRENDA gene entry.
        Information is parsed from the fasta format. First for the local 
        fasta file is searched. If no such file is available the fasta data
        is received from BRENDA.
    """
    def __init__(self, ec, id):
        """ id is the fasta identifier in the first line of entry """
        if equationTools.isECnumber(ec):
            self.ec = ec
            self.id = id
            self.setData()
            
    def setData(self):
        """ Sets all the available data from the FASTA file """
        fasta = loadGenesFastaFromECFile(self.ec)
        if not fasta:
            # file not available (load from url)
            fasta = loadGenesFastaFromEC(self.ec)
        entries = fasta.split(">")
        for entry in entries:
            if entry and entry.startswith(self.id):
                lines = entry.split("\n")
                header = lines[0].split("|")
                self.name = header[1]
                self.organism = header[3]
                self.database = header[4]
                self.aa_sequence = "".join(lines[1:]).strip().replace("\r", "")
                self.taxonomy = tools.taxonomy.getTaxIdStringFromName(self.organism)
                self.taxonomyHuman = tools.taxonomy.findCommonNodeHuman(self.taxonomy[4:])

    def createInformationString(self):
        """ Creates information string for the BRENDA gene object. 
            Returns string of information
        """
        names = ["ID", "EC / Name", "Organism", "Taxonomy","Taxonomy Human", "Database", "Sequence"]
        infos = [self.id, self.ec + "\t"+ self.name, self.organism, self.taxonomy,
                 self.taxonomyHuman, self.database, self.aa_sequence]
        lines = []
        for name, info in zip(names, infos):
            lines.append(name.ljust(15) + str(info) + "\n")
        return "".join(lines)
    
    def printInformation(self):
        """ Prints the information string for the object. """
        print self.createInformationString()
    
def loadGenesFastaFromEC(ec):
    """ Loads all the gene information for a given ec number in fasta format.
        Returns fasta string.
        Returns Nonoe if no valid ec number is given"""
    if not equationTools.isECnumber(ec):
        return None
    url = "http://www.brenda-enzymes.info/sequences/seq_fasta_EC.php4?ec="+ec
    # proxies have to be set
    input = urllib.urlopen(url)
    return input.read()

def loadGenesFastaFromECFile(ec):
    """ Loads all the gene information for a given ec number in fasta format
        from file.
        The fasta file has to be available in the folder 'genes_location. 
        This file is created in loadGenesFastaFromEC(ec).
        Returns the fasta string if information is available, None otherwise
    """
    global genes_location
    if not equationTools.isECnumber(ec):
        return None
    file = genes_location + ec + ".fasta"
    input = open(file, "r")
    return input.read() 
    
def saveGenesFastaFromEC(ec):
    """ Saves the fasta information for a given ec number to file 
        in folder 'genes_location' 
        Returns None"""
    global genes_location
    file = genes_location + ec +".fasta"
    out = open(file, "w")
    out.write(loadGenesFastaFromEC(ec))
    del out
    print "Save:\t%s" % file

def getGeneIDsFromFASTA(fasta):
    """ Returns list of gene IDs for a given fasta string. """
    genes = []
    entries = fasta.split(">")
    for entry in entries:
        if entry:
            header = entry.split("|")
            genes.append(header[0])
    return genes

def getAllECNumbers():
    """ Gets all available EC numbers. 
        Returns a list of all available ec numbers. EC numbers are parsed from
        the BRENDA offline data
    """
    ecs = []
    input = open(files.BRENDAfile, "r")
    for line in input:
        if line.startswith("ID\t"):
            ec = re.findall("^\d+.\d+.\d+.\d+", line[3:-1])
            if ec:
                ecs.append(ec[0]) 
    return ecs

def getBRENDAGenesFromEC(ec):
    """ Returns list of all BRENDA gene objects 
        for a given ec number """
    fasta = loadGenesFastaFromECFile(ec) 
    gene_ids = getGeneIDsFromFASTA(fasta)
    return [BRENDAGene(ec, id) for id in gene_ids] 

def getFASTAForAllEC():
    """ Creates all fasta information files for all available 
        enzymes in the BRENDA database
    """
    ecs = getAllECNumbers()
    for ec in ecs:
        saveGenesFastaFromEC(ec)

def test():
    """ Tests the BRENDA gene information """
    ec = "1.1.1.10"
    #loadGenesFastaFromEC(ec)
    #saveGenesFastaFromEC(ec)
    fasta = loadGenesFastaFromECFile(ec)
    # Create all gene objects for fasta file
    gene_ids = getGeneIDsFromFASTA(fasta)
    gene_obj =  []
    for id in gene_ids:
        gene_obj.append(BRENDAGene(ec, id))
    # Print Information
    for gene in gene_obj:
        gene.printInformation()
    # Get all EC numbers
    #getFASTAForAllEC()

if __name__ == "__main__":
    print "Get BRENDA genes information for all ec numbers"
    test()