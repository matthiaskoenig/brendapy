# -*- coding: latin-1 -*-
"""
    Parsed protein information from the BRENDA database.
    
    For every ec number one or more (in most cases multiple) protein entries
    exist. The information for one protein entry is stored in 
    a BRENDAProtein() object.
    
    author: Matthias Koenig
    version: 0.1
    date 06.08
    
"""
import re
import parseBRENDA
import tools.taxonomy

class BRENDAProtein(object):
    """ Stores all BRENDA information for a given EC number.
        One BRENDA entry consists of multiple protein entries.
        One protein entry is specific for one organism and 
        correspondes to one information in the BRENDA database
        
        TODO: Write general parser functions for the different entities
        For example can cofactors and inhibitors be set with the same methods
        (not so important)
    """
    ids = ["PR", "RE", "ST", "LO", "NSP", "SP", "TN", "KM", "SA", "CF", "IN", "KI", "ME", "RF"]
    names = ["Protein", "Reaction", "Source Tissue", "Localization", "Natural Substrate Product",
             "Substrate Product", "Turnover number", "Km", "Specific activity", "Cofactors",
             "Inhibitors", "Ki", "Metal ions", "References"]   
    
    def __init__(self, ec, id, ec_string):
        """ Protein object is initialized with ec number 'ec', 
            id (number of entry for ec in Brenda) and ec_string which contains the
            data for the protein.
        """
        self.ec = ec
        self.id = id
        self.ec_string = ec_string
        self.setData()
    
    def setData(self):
        """ Sets all the data for a given EC number and protein id """
        #print "ID\t%s" % self.id
        # information in BRENDA for ec
        self.organism = self.getOrganism()
        self.taxonomy = self.getTaxonomy()
        self.taxonomyHuman = self.getTaxonomyHuman()
        self.gene = self.getSwissProtGene()
        self.references = self.getReferences()
        self.reaction = self.getReaction()
        self.source_tissue = self.getSourceTissue()
        self.localisation = self.getLocalication()
        self.natural_substrate_product = self.getNaturalSubstrateProduct()
        self.substrate_product = self.getSubstrateProduct()
        self.turnover_number = self.getTurnoverNumber()
        self.km = self.getKm()
        self.specific_activity = self.getSpecificActivity()
        self.cofactors = self.getCofactors()
        self.inhibitors = self.getInhibitors()
        self.ki = self.getKi()
        self.metal_ions = self.getMetalIons()
        self.pubmed = self.getPubMedReferences()
        #print
    
    def getOrganism(self):
        """ Sets organism information from protein """
        pr_entries = parseBRENDA.getEntryFromString("PR", self.ec_string)
        # Get Entries for id
        entry = parseBRENDA.getEntryWithID(self.id, pr_entries)
        items = entry[0].split(" ")
        if (len(items[2]) > 0 and items[2][0] != "Q"):
            organism = items[1] + " " + items[2]
        else:
            organism = items[1]
        return organism
    
    def getTaxonomy(self):
        """ Sets the taxonomy information from the organism name using
            module taxonomy and NCBI data """
        return tools.taxonomy.getTaxIdStringFromName(self.organism)
        
    def getTaxonomyHuman(self):
        """ Sets the evolutionary distance from human """
        return tools.taxonomy.findCommonNodeHuman(self.taxonomy[4:])
    
    def getSwissProtGene(self):
        """ Sets gene information for protein """
        #print "BRENDAProtein.getSwissProtGene()"
        pr_entries = parseBRENDA.getEntryFromString("PR", self.ec_string)
        # Get Entries for id
        entry = parseBRENDA.getEntryWithID(self.id, pr_entries)
        items = entry[0].split(" ")
        gene = [items[-3], items[-2]]
        return gene
    
    def getReferences(self):
        """ Sets references for protein """
        #print "BRENDAProtein.getReferences()"
        pr_entries = parseBRENDA.getEntryFromString("PR", self.ec_string)
        # Get Entries for id
        entry = parseBRENDA.getEntryWithID(self.id, pr_entries)
        items = entry[0].split(" ")
        references = items[-1].replace("<", "").replace(">","").split(",") 
        return references
    
    def getReaction(self):
        """ Sets reaction for protein 
            TODO: What is this ? Still necessary ?"""
        pass

    def getSourceTissue(self):
        """ Sets source tissue for protein """
        st_entries = parseBRENDA.getEntryFromString("ST", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, st_entries)  
        tissues = []
        def getTissue(entry):
            pattern = r"#.*# .* \("
            tmp = re.findall(pattern, entry)
            if not tmp:
                pattern = r"#.*# .* <"
                tmp = re.findall(pattern, entry)                
            tmp = tmp[0].split("#")
            tissue = tmp[-1][:-1].strip()
            return tissue
        for entry in entries:
            tissues.append(getTissue(entry))
        return tissues
        
    def getLocalication(self):
        """ Sets localisation for protein """
        lo_entries = parseBRENDA.getEntryFromString("LO", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, lo_entries)  
        localisation = []
        
        def getLoc(entry):
            pattern = r"^#.*# .* <"
            tmp = re.findall(pattern, entry) 
            if not tmp:
                pattern = r"^#.*# .* ("
                tmp = re.findall(pattern, entry)              
            tmp = tmp[0].split("#")
            loc = tmp[2][:-1].strip()
            return loc
        
        for entry in entries:
            localisation.append(getLoc(entry))
        return localisation
        
    def getNaturalSubstrateProduct(self):
        """ Sets natural substrate, product for protein """
        nsp_entries = parseBRENDA.getEntryFromString("NSP", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, nsp_entries)  
        nsp = []
        def getReaction(entry):
            """ Gets the natural reaction equation """
            pattern = r"#.*# .* \("
            tmp = re.findall(pattern, entry)
            if not tmp:
                pattern = r"#.*# .* <"
                tmp = re.findall(pattern, entry)
            if not tmp: 
                tmp = re.findall(r"#.*# .*", entry)     
            tmp = tmp[0].split("#")
            reaction = tmp[-1][:-1].strip()
            return reaction
        
        def getInfo(entry):
            """ Gets additional information """
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1]
            else:
                info = ''
            if not parseBRENDA.isIDinEntry(self.id, info):
                info = ''
            return info
               
        for entry in entries:
            nsp.append( [getReaction(entry), getInfo(entry)] )
        return nsp
        
    def getSubstrateProduct(self):
        """ Sets substrate, product for protein 
            Additional substrate, product information
            TODO: not implemented (information not very important)
        """
        sp_entries = parseBRENDA.getEntryFromString("SP", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, sp_entries)  
        #print entries
        sp = []
        return []
    
    def getTurnoverNumber(self):
        """ Sets the turnover numbers for the proteins """
        tn_entries = parseBRENDA.getEntryFromString("TN", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, tn_entries)  
        #print entries
        tn = []
        def getTN(entry):
            """ gets the turnover value """
            pattern = r"#.*# \d*.\d*.* {"
            tmp = re.findall(pattern, entry)               
            tmp = tmp[0].split("#")
            tn = tmp[-1][:-1].strip()
            return tn
        def getSubstrate(entry):
            """ gets the coresponding value """
            pattern = r"{.*}"
            tmp = re.findall(pattern, entry)               
            substrate = tmp[0][1:-1]
            return substrate
        def getAddInfo(entry):
            """ gets addtional information for the tn value """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1].replace("\xb0", "")
            if not parseBRENDA.isIDinEntry(self.id, info):
                info = ''
            else:
                info = re.sub("#.*#", "", info).strip()
            return info
        # Get the information from the entries
        for entry in entries:
            tn.append([getTN(entry), getSubstrate(entry), getAddInfo(entry)])
            #print tn[-1]
        return tn
    
    def getKm(self):
        """ Sets the Km values of the proteins """
        km_entries = parseBRENDA.getEntryFromString("KM", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, km_entries)  
        # print entries
        km = []
        def getKM(entry):
            """ gets the turnover value """
            pattern = r"#.*# \d*.\d*.* {"
            tmp = re.findall(pattern, entry)
            tmp = tmp[0].split("#")
            km = tmp[-1][:-1].strip()
            return km
        def getSubstrate(entry):
            """ gets the coresponding value """
            pattern = r"{.*}"
            tmp = re.findall(pattern, entry)               
            substrate = tmp[0][1:-1]
            return substrate
        def getAddInfo(entry):
            """ gets addtional information for the tn value """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1].replace("\xb0", "")
            if not parseBRENDA.isIDinEntry(self.id, info):
                info = ''
            else:
                info = re.sub("#.*#", "", info).strip()
            return info        
   
        for entry in entries:
            km.append([getKM(entry), getSubstrate(entry), getAddInfo(entry)])
            #print km[-1]
        return km
        
    def getSpecificActivity(self):
        """ Sets the specific activity of the proteins """
        km_entries = parseBRENDA.getEntryFromString("SA", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, km_entries)  
        #print entries
        sa = []
    
        def getSA(entry):
            """ gets value of specific activity """
            pattern = r"#.*# \d*.\d*.* \("
            tmp = re.findall(pattern, entry)
            if not tmp:
                tmp = re.findall(r"#.*# \d*.\d*.* <", entry)
            if not tmp:
                tmp = re.findall(r"#.*# -\d*.\d*.* \(", entry)
            if not tmp:
                tmp = re.findall(r"#.*# -\d*.\d*.* <", entry)
            tmp = tmp[0].split("#")
            sa = tmp[-1][:-1].strip()
            return sa
        
        def getAddInfo(entry):
            """ gets additional information for the sa value """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1]
            if not parseBRENDA.isIDinEntry(self.id, info):
                info = ''
            else:
                info = re.sub("#.*#", "", info).strip()
            return info        
   
        for entry in entries:
            sa.append([getSA(entry), getAddInfo(entry)])
            #print sa[-1]
        return sa
    
    def getCofactors(self):
        """ Sets the cofactors of the proteins """
        co_entries = parseBRENDA.getEntryFromString("CF", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, co_entries)  
        #print entries
        co = []
        
        def getCF(entry):
            """ Gets the cofactor from entry. """
            pattern = r"#.*# .* \("
            tmp = re.findall(pattern, entry)
            if not tmp:
                pattern = r"#.*# .* <"
                tmp = re.findall(pattern, entry)                
            tmp = tmp[0].split("#")
            cf = tmp[-1][:-1].strip()
            return cf
        
        def getAddInfo(entry):
            """ Gets additional information for the cofactor """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1]
                info = [item for item in info.split(';') if parseBRENDA.isIDinEntry(self.id, item)]
                info = [re.sub(r"#.*#", "", item).strip() for item in info]
            return "; ".join(info)
                        
        for entry in entries:
            co.append([getCF(entry), getAddInfo(entry)])
            #print co[-1]
        return co
        
    def getInhibitors(self):
        """ Sets the inhinitors of the proteins """
        in_entries = parseBRENDA.getEntryFromString("IN", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, in_entries)  
        #print entries
        inhibitors = []
        def getIN(entry):
            """ Gets the inhibitor from entry. """
            pattern = r"#.*# .* \("
            tmp = re.findall(pattern, entry)
            if not tmp:
                pattern = r"#.*# .* <"
                tmp = re.findall(pattern, entry)                
            tmp = tmp[0].split("#")
            inhibitor = tmp[-1][:-1].strip()
            return inhibitor
        
        def getAddInfo(entry):
            """ Gets additional information for the inhibitor """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1]
                info = [item for item in info.split(';') if parseBRENDA.isIDinEntry(self.id, item)]
                info = [re.sub(r"#.*#", "", item).strip() for item in info]
            return "; ".join(info)
                        
        for entry in entries:
            inhibitors.append([getIN(entry), getAddInfo(entry)])
            #print inhibitors[-1]
        return inhibitors
              
    def getKi(self):
        """ Sets the Ki values of the proteins """
        ki_entries = parseBRENDA.getEntryFromString("KI", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, ki_entries)  
        #print entries
        ki = []
        def getKI(entry):
            """ gets the turnover value """
            pattern = r"#.*# \d*.\d*.* {"
            tmp = re.findall(pattern, entry)
            #print entry               
            tmp = tmp[0].split("#")
            ki = tmp[-1][:-1].strip()
            return ki
        def getSubstrate(entry):
            """ gets the coresponding value """
            pattern = r"{.*}"
            tmp = re.findall(pattern, entry)               
            substrate = tmp[0][1:-1]
            return substrate
        def getAddInfo(entry):
            """ gets addtional information for the tn value """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1].replace("\xb0", "")
            if not parseBRENDA.isIDinEntry(self.id, info):
                info = ''
            else:
                info = re.sub("#.*#", "", info).strip()
            return info        
        for entry in entries:
            ki.append([getKI(entry), getSubstrate(entry), getAddInfo(entry)])
            # print ki[-1]
        return ki
        
    def getMetalIons(self):
        """ Sets the metal ions of the proteins """
        me_entries = parseBRENDA.getEntryFromString("ME", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, me_entries)  
        #print entries
        me = []
        
        def getME(entry):
            """ Gets the metal ions from entry. """
            pattern = r"#.*# .* \("
            tmp = re.findall(pattern, entry)
            if not tmp:
                pattern = r"#.*# .* <"
                tmp = re.findall(pattern, entry)                
            tmp = tmp[0].split("#")
            me_ion = tmp[-1][:-1].strip()
            return me_ion
        
        def getAddInfo(entry):
            """ Gets additional information for the cofactor """
            info = ''
            pattern = r"\(.*\)"
            tmp = re.findall(pattern, entry)
            if tmp:
                info = tmp[0][1:-1]
                info = [item for item in info.split(';') if parseBRENDA.isIDinEntry(self.id, item)]
                info = [re.sub(r"#.*#", "", item).strip() for item in info]
            return "; ".join(info)
                        
        for entry in entries:
            me.append([getME(entry), getAddInfo(entry)])
            #print me[-1]
        return me
        
    def getPubMedReferences(self):
        """ Gets information about the cited references. So the given data in the 
            protein objects can be validated
            TODO: Parse the given references (can be down in the output of the protein 
                  information
        """
        rf_entries = parseBRENDA.getEntryFromString("RF", self.ec_string)
        entries = parseBRENDA.getEntryWithID(self.id, rf_entries)  
        #print entries
        rf = []
        
        return rf
    
    def createInformation(self):
        """ creates InformationString for object"""
        lines = []
        names = ["EC", "ID", "Organism", "Taxonomy", "Taxonomy Human", "Source Tissue", "Localisation",
                 "NSP", "Turnover Number", "Km",
                 "Specific Activity", "Cofactors", "Inhibitors", "Ki",
                 "Metal Ions", "Pubmed"]
        infos = [self.ec, self.id, self.organism, self.taxonomy,
                 self.taxonomyHuman, self.source_tissue, self.localisation,
                 self.natural_substrate_product, self.turnover_number,
                 self.km, self.specific_activity, self.cofactors, self.inhibitors,
                 self.ki, self.metal_ions, self.references]
        for (name, info) in zip(names, infos):
            lines.append(name.ljust(20) + str(info) + "\n")
        return "".join(lines)
    
    def printInformation(self):
        """ Prints the information for a given object """
        print self.createInformation()


def test():
    """ Test the proteinBRENDA module """
    print "Test proteinBRENDA module"
    #ec = "1.1.1.10"
    ec = "5.3.1.9"
    # BRENDA information for ec
    # In the process all BRENDAprotein objects for the different
    # protein entities are created
    BI = parseBRENDA.BRENDAInformation(ec)
    BI.printInformationString()

if __name__ == "__main__":
    test()