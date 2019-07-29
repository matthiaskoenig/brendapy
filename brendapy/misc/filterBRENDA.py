
"""
    List of filters to filter BRENDA protein entries.
    Filters always return boolean values.
    
    If protein entry fullfilles filter, filter returns 'True'.
    Filter returns 'False' otherwise.
"""

import tools.taxonomy as taxonomy
import brendapy.parser

def isSpecies(p, species):
    """
        Test if protein entry 'p' is for species 'species'. Returns True
        or False.
    """
    tax = taxonomy.getTaxIdStringFromName(species)
    # p.printInformation()
    if p.taxonomy == tax:
        return True
    if p.organism == species:
        return True
    return False

def isTaxonomy(p, tax):
    """
        Test if protein entry 'p' is for taxonomy 'tax'. Returns True
        or False.
    """
    if p.taxonomy == tax:
        return True
    return False

def isSourceTissue(p, source_tissue):
    """ Test if protein entry 'p' is for source tissue 'source_tissue'.
        Returns True or False.
    """
    for tissue in p.source_tissue:
        if tissue == source_tissue:
            return True
    return False

def isLocalisation(p, localisation):
    """ Test if protein entry 'p' is for localisation 'localisation'.
        Returns True or False. 
    """
    for loc in p.localisation:
        if loc == localisation:
            return True
    return False

def isDescendantSpecies(p, species):
    """ Test if protein entry 'p' is descendant or equal to species.
        Returns True or False. 
    """
    tax_id = taxonomy.getTaxIdStringFromName(species)
    return isDescendantTaxonomy(p, tax_id)

def isDescendantTaxonomy(p, tax_id):
    """ Test if protein entry 'p' is descendant or equal to species
        with taxonomy tax.
        Returns True or False. 
    """
    # Species is higher in the taxonomy tree
    # find all ancestor nodes of protein p
    if tax_id.isdigit():
        tax_id = "TAX:" + tax_id
    
    nodes = taxonomy.getParentNodes(p.taxonomy)
    #print tax_id
    #print nodes
    # get taxonomy entry of species
    if not nodes:
        # print "[%s]\tNo taxonomy data found" % tax_id
        return False
    if tax_id[4:] in nodes or tax_id == p.taxonomy:
        return True
    return False

def getLocalisationVocabulary(proteins):
    """ Calculates all vocabulary terms for localisation, which can
        be found in the given proteins 'proteins'.
        Returns List of found vocabulary terms.
    """
    voc = []
    for p in proteins:
        for loc in p.localisation:
            if loc not in voc:
                voc.append(loc)
    voc.sort()
    return voc
    
def getSourceTissueVocabulary(proteins):
    """ Calculates all vocabulary terms for source Tissue, which can
        be found in the given proteins 'proteins'.
        Returns List of found vocabulary terms.
    """
    voc = []
    for p in proteins:
        for st in p.source_tissue:
            if st not in voc:
                voc.append(st)
    voc.sort()
    return voc

def test():
    print "Test BRENDA.filterBRENDA"
    ec = "5.3.1.9"
    ec_string = brendapy.parser.get_brenda_info(ec)
    proteins = brendapy.parser.getBrendaProteinsFromEC(ec, ec_string)
    
    def basicTest():
        def testIsSpecies():
            results = []
            for p in proteins:
                filter = isSpecies(p, "Homo sapiens")
                if filter:
                    p.printInformation()
                results.append(filter)
            print results
        def testIsSourceTissue():
            results = []
            for p in proteins:
                filter = isSourceTissue(p, "heart")
                if filter:
                    p.printInformation()
                results.append(filter)
            print results
        def testIsLocalisation():
            results = []
            for p in proteins:
                filter = isLocalisation(p, "membrane")
                if filter:
                    p.printInformation()
                results.append(filter)
            print results
        
        testIsSpecies()
        testIsSourceTissue()
        testIsLocalisation()

    def testDescendant():
        #species = "Mammalia"
        #tax = taxonomy.getTaxIdFromName(species)[1]
        #tax = "40674" # Mammalia
        #tax = "9606" # homo sapiens
        species = "Mammalia"
        results = []
        for p in proteins:
            #filter = isDescendantSpecies(p, species)
            #filter = isDescendantTaxonomy(p, tax)
            filter = isDescendantSpecies(p, species)
            if filter:
                p.printInformation()
            results.append(filter)
        print results
    
    def testVocabulary():
        voc_localisation = getLocalisationVocabulary(proteins)
        voc_source_tissue = getSourceTissueVocabulary(proteins)
        for p in proteins:
            p.printInformation()
        print voc_localisation
        print voc_source_tissue
        
        
    if 0:
        basicTest()
    if 1:
        testDescendant()
    if 0:
        testVocabulary()
        
if __name__ == "__main__":
    test()
