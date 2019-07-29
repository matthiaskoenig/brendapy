
"""
    Interface module for BRENDA queries.
    Brenda database is parsed in protein entries.
    
    Afterwards queries can be send to return the Brenda protein
    entries which fullfill the filter properties
"""
import cPickle
import files
import brendapy.parser
import brendapy.misc.filterBRENDA
import HEPATOSYS.enzymes

output_ecs = files.install_dir + "/data/output/brenda_ecs_file.dat"
output_proteins = files.install_dir + "/data/output/brenda_proteins/"
load_file = files.install_dir + "/data/output/brenda_proteins_file.dat"
save_file = files.install_dir + "/data/output/brenda_proteins_file.dat"
brenda_proteins = []
hepatosys_enzymes = []

def createAllBrendaProteinFiles(create_files=True):
    """
        Parses the BRENDA information file and generates all Brenda protein 
        entries from the data. For every ec number all protein entries are generated
        and saved to individual files.
        Returns list of EC numbers.
    """
    global output_ecs, output_proteins
    # Load all ec data
    ec_filehandler = open(output_ecs, "w")
    if create_files:
        ecs = brendapy.parser.create_ec_files()
        cPickle.dump(ecs, ec_filehandler)
        ec_filehandler.close()
    else:
        ecs = cPickle.load(ec_filehandler)
    
    # Create all protein entries
    for ec in ecs:
        output_file = output_proteins + ec
        out = open(output_file, "w")
        proteins = brendapy.parser.getBrendaProteinsFromEC(ec)
        cPickle.dump(proteins, out)
        print ec.ljust(20) + "[%s Protein entries]" % len(proteins)
        out.close
    print "Protein entries:\t %s" % len(brenda_proteins)

def loadECs():
    """ Loads ec numbers from file """
    global output_ecs
    filehandler = open(output_ecs, "r")        
    return cPickle.load(filehandler)

def getAllBrendaProteins():
    """
        Merges the individual protein files. All protein entries from the
        different ec numbers are taken and merged in one list.
        Sets the global variable 'brenda_proteins'
    """
    global brenda_proteins, output_ecs, output_proteins
    brenda_proteins = []
    ec_filehandler = open(output_ecs, "r")
    ecs = cPickle.load(ec_filehandler)
    for ec in ecs:
        print ec.ljust(15), "[load]"
        protein_filehandler = open(output_proteins + ec, "r")
        brenda_proteins.extend(cPickle.load(protein_filehandler))

def getBrendaProteins(ec):
    """ Returns list of Brenda Protein entries for given ec number.
        The protein files have to be generated first.  """
    global output_proteins
    # print ec.ljust(15), "[load]"
    try:
        protein_filehandler = open(output_proteins + ec, "r")
    except IOError:
        print "\t\t[%s]".ljust(15) % ec, "Brenda protein file not found"
        return []
    return cPickle.load(protein_filehandler)

def saveAllBrendaProteins(filename=None):
    """ saveAllBrendaProteins(filename)
        Save the global 'brenda_proteins' with pickle to file 'filename'
    """
    global brenda_proteins, save_file
    if not filename:
        filename = save_file
    print "Saving Brenda Proteins:\t%s" % filename
    filehandler = open(filename, 'w')
    cPickle.dump(brenda_proteins, filehandler)
    filehandler.close()
    print "Brenda Proteins saved."

def loadAllBrendaProteins(filename=None):
    """ loadAllBrendaProteins(filename)
        Loads the Brenda Protein entries from file 'filename' to 
        global variable 'brenda_proteins'
        Uses pickle for loading.
    """
    global brenda_proteins, load_file
    if not filename:
        filename = load_file
    print "Loading Brenda Proteins ..."
    try:
        filehandler = open(filename, 'r')
    except:
        print "Error while loading proteins:"
        print "Filename doesn't exist:\t %s" % filename
        exit(1)
    try:
        p = cPickle.load(filehandler)
    except:
        print "No correct protein file:\t%s" % filename
        print "Recreate protein file or give valid Brenda protein file"
        exit(1)
    print "Brenda Proteins loaded."
    brenda_proteins = p

def createLocalisationsFile(filename):
    """ Creates file fo all localisation attributes used in the Brenda database
        and writes the data to file 'filename'
    """
    localisations = brendapy.misc.filterBRENDA.getLocalisationVocabulary(brenda_proteins)
    #print localisations
    output = open(filename, "w")
    for loc in localisations:
        output.write(loc + "\n")
    output.close()
    print "Brenda Localisations File created:\t%s" % filename

def createSourceTissueFile(filename):
    """ Creates file fo all source tissue attributes used in the Brenda database
        and writes the data to file 'filename'
    """
    source_tissues = brendapy.misc.filterBRENDA.getSourceTissueVocabulary(brenda_proteins)
    output = open(filename, "w")
    #print source_tissues
    for st in source_tissues:
        output.write(st + "\n")
    output.close()
    print "Brenda Source Tissue File created:\t%s" % filename

def getECsFromProteins(proteins):
    """ Returns list of all ec numbers in given protein instances.
        EC numbers are sorted and unique (no multiple entries exist 
        in returned list).
    """
    ecs = []
    for p in proteins:
        if p.ec not in ecs:
            ecs.append(p.ec)
    ecs.sort()
    return ecs

def main():
    """ Load BRENDA data and handle the search queries.
        To create the proteins again: set load to False and Save to true.
    """
    print "###\tBRENDA Query system\t###"
    
    # Get all the BRENDA information
    global ecs, brenda_proteins, hepatosys_enzymes
    localisations_file = files.install_dir + "/data/output/brenda_localisations_file.dat"
    source_tissue_file = files.install_dir + "/data/output/brenda_source_tissue_file.dat"
    load = True
    save = True
    loc_st_files = True
    if load:
        loadAllBrendaProteins(load_file)
    else:
        createAllBrendaProteinFiles()
        getAllBrendaProteins()
    if save:
        saveAllBrendaProteins(save_file)
    # Write Localisation and Source Tissue file if necessary
    if loc_st_files:
        createLocalisationsFile(localisations_file)
        createSourceTissueFile(source_tissue_file)

    # Get all the HEPATOSYS information
    hepatosys_enzymes = HEPATOSYS.enzymes.loadEnzymesFromFile(HEPATOSYS.enzymes.enzymes_file)
    hepatosys_enzymes = HEPATOSYS.enzymes.getEnzymesWithValidEC(hepatosys_enzymes)
    # query the protein entries
    # statistics
    ec_count = 4025
    protein_count = len(brenda_proteins)
    print "\n###\tBRENDA Statistics [08/08]\t###"
    print "EC entries searched:".ljust(30), ec_count
    print "Protein entries searched:".ljust(30), protein_count
    print "Proteins/EC:".ljust(30), 1.0*protein_count/ec_count    
    
    # query
    def query_1():
        print "\n# Query 1"
        species = "Homo sapiens"
        tissue_1 = "liver"
        tissue_2 = "hepatocyte"
        print " -> Species:\t", species
        print " -> Tissue 1:\t", tissue_1
        print " -> Tissue 1:\t", tissue_2
        result = []
        for p in brenda_proteins:
            if brendapy.misc.filterBRENDA.isSpecies(p, species) and (
                    brendapy.misc.filterBRENDA.isSourceTissue(p, tissue_1) or brendapy.misc.filterBRENDA.isSourceTissue(p, tissue_2)):
                result.append(p)
        return result
    
    def query_2():
        print "\n# Query 2"
        species = "Mammalia"
        tissue_1 = "liver"
        tissue_2 = "hepatocyte"
        print " -> Descendant of:\t", species
        print " -> Tissue 1:\t", tissue_1
        print " -> Tissue 1:\t", tissue_2
        result = []
        for p in brenda_proteins:
            if brendapy.misc.filterBRENDA.isDescendantSpecies(p, species) and (
                    brendapy.misc.filterBRENDA.isSourceTissue(p, tissue_1) or brendapy.misc.filterBRENDA.isSourceTissue(p, tissue_2)):
                result.append(p)
        return result
    
    def query_3():
        print "\n# Query 3"
        tissue_1 = "liver"
        tissue_2 = "hepatocyte"
        print " -> Tissue 1:\t", tissue_1
        print " -> Tissue 1:\t", tissue_2
        result = []
        for p in brenda_proteins:
            if brendapy.misc.filterBRENDA.isSourceTissue(p, tissue_1) or brendapy.misc.filterBRENDA.isSourceTissue(p, tissue_2):
                result.append(p)
        return result
    
    def writeProteinResults(proteins, filename):
        # General results
        ecs = getECsFromProteins(proteins)
        #print " => [%s] ECs found." % len(ecs)
        #print " => [%s] Proteins found." % len(proteins)

        # Compare to Hepatosys
        def not_in_hepatosys(proteins):
            results_p = []
            results_e = []
            for p in proteins:
                for e in hepatosys_enzymes:
                    if p.ec == e.ec:
                        break
                else:
                    if p not in results_p:
                        results_p.append(p)
            return results_p, results_e 
        
        def in_hepatosys(proteins):
            """ Filter proteins and return only proteins which obey the filter """
            results_p = []
            results_e = []
            for p in proteins:
                for e in hepatosys_enzymes:
                    if p.ec == e.ec:
                        if p not in results_p:
                            results_p.append(p)
                        results_e.append(e)
            return results_p, results_e
            
        def in_hepatosys_human(proteins):
            results_p = []
            results_e = []
            for p in proteins:
                for e in hepatosys_enzymes:
                    if p.ec == e.ec and e.inhuman == "t":
                        if p not in results_p:
                            results_p.append(p)
                        results_e.append(e)
            return results_p, results_e
        
        def in_hepatosys_not_human(proteins):
            results_p = []
            results_e = []
            for p in proteins:
                for e in hepatosys_enzymes:
                    if p.ec == e.ec and e.inhuman == "f":
                        if p not in results_p:
                            results_p.append(p)
                        results_e.append(e)
            return [results_p, results_e]
        
        def writeProteins(proteins, filename, text):
            ecs = getECsFromProteins(proteins)
            # print " => [%s] ECs found." % len(ecs)
            # print " => [%s] Proteins found." % len(proteins)
            print "-> " + text.ljust(60) + "[ " +str(len(ecs)).rjust(4)+ " | " + str(len(proteins)).rjust(4) + " ]"
            out = open(filename, "w")
            lines = []
            for p in proteins:
                items = [str(item) for item in [p.ec, p.id, p.organism, p.taxonomy, p.source_tissue, p.localisation]]
                lines.append("\t".join(items) + "\n")
            out.write("".join(lines))
            out.close()
                        
        def writeEnzymes(enzymes, filename):
            out = open(filename, "w")
            lines = []
            for e in enzymes:
                items = [str(item) for item in [e.id, e.compartment, e.ec, e.note, e.name, e.reaction, e.confidence, e.inhuman, e.excluded]]
                lines.append("\t".join(items) + "\n")
            out.write("".join(lines))
            
        texts = ["[EC|Protein] entries found", "[EC|Protein] not found in Hepatosys",
                "[EC|Protein] found in Hepatosys", "[EC|Protein] found in Hepatosys  AND in_human",
                "[EC|Protein] found in Hepatosys and not in_human"]
        filenames_p = [filename + "_" + str(number) + "_p" for number in range(1,6)]
        filenames_e = [filename + "_" + str(number)+ "_e" for number in range(1,6)]
        data = [[proteins, []], not_in_hepatosys(proteins), in_hepatosys(proteins), in_hepatosys_human(proteins),
                         in_hepatosys_not_human(proteins)]
        data_p = [item[0] for item in data]
        data_e = [item[1] for item in data]
        for filename, p, text in zip(filenames_p, data_p, texts):
            writeProteins(p, filename, text)
        for filename, e in zip(filenames_e[1:],data_e[1:]):
            writeEnzymes(e, filename)
    
    out_folder = files.install_dir + "/data/output/"             
    writeProteinResults(query_1(), out_folder + "q1")
    writeProteinResults(query_2(), out_folder + "q2")
    writeProteinResults(query_3(), out_folder + "q3")
    
def test():
    def createProteins():
        createAllBrendaProteinFiles()
    
    do_tests = [1]
    tests = [createProteins]
    for do, test in zip(do_tests, tests):
        if do: test()

if __name__ == "__main__":
    #main()
    test()