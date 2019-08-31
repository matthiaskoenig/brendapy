"""
Resolve substance information from BRENDA.

Ontologies downloaded from:
https://www.ebi.ac.uk/ols/ontologies/chebi
https://www.ebi.ac.uk/ols/ontologies/bto

on 2019-08-31


# chebi information:
ftp://ftp.ebi.ac.uk/pub/databases/chebi/Flat_file_tab_delimited/




TODO: parse the CHeBI information for the given Km parameter.

Name:  Get src_compound_ids from InChIKey
Description:  Obtain a list of all src_compound_ids (from all sources) which are CURRENTLY assigned to a query InChIKey
Extension of base url:  inchikey
Number of required input parameters:  1
Input:  /InChIKey
Output:  list of two element arrays, containing 'src_compound_id' and 'src_id'.
Example:  https://www.ebi.ac.uk/unichem/rest/inchikey/AAOVKJBEBIDNHE-UHFFFAOYSA-N


"""
from pprint import pprint
import logging
import requests

def get_pubchem_collections():
    """ Available collections in PubChem.

    Name:  Get all src_ids
    Description:  Obtain all src_ids currently in UniChem
    Extension of base url:  src_ids
    Number of required input parameters:  0
    Input:   - none -
    Output:  list of 'src_id's.
    Example:  https://www.ebi.ac.uk/unichem/rest/src_ids/

    Name:  Get source infomation
    Description:  Obtain all information on a source by querying with a source id (src_id).
    Extension of base url:  sources
    Number of required input parameters:  1
    Input:  /src_id
    Output:  list containing:
    src_id (the src_id for this source),
    src_url (the main home page of the source),
    name (the unique name for the source in UniChem, always lower case),
    name_long (the full name of the source, as defined by the source),
    name_label (A name for the source suitable for use as a 'label' for the source within a web-page. Correct case setting for source, and always less than 30 characters),
    description (a description of the content of the source),
    base_id_url_available (an flag indicating whether this source provides a valid base_id_url for creating cpd-specific links [1=yes, 0=no]).
    base_id_url (the base url for constructing hyperlinks to this source [append an identifier from this source to the end of this url to create a valid url to a specific page for this cpd], unless aux_for_url=1),
    aux_for_url (A flag to indicate whether the aux_src field should be used to create hyperlinks instead of the src_compound_id [1=yes, 0=no]
    Example:  https://www.ebi.ac.uk/unichem/rest/sources/1

    :return:
    """
    url_source_ids = "https://www.ebi.ac.uk/unichem/rest/src_ids/"
    print(url_source_ids)
    response = requests.get(url_source_ids)
    src_ids_data = response.json()
    pprint(src_ids_data)

    data = {}

    for item in src_ids_data:
        src_id = item['src_id']
        url_src_id = f"https://www.ebi.ac.uk/unichem/rest/sources/{src_id}"
        response = requests.get(url_src_id)
        src_json = response.json()
        data[src_id] = src_json

    pprint(data)
    return data



def get_substance_info():
    """
    Possible to map between all database identifiers, i.e., CHeBI to BRENDA id can be resolved.

    # connectivity search
    https://www.ebi.ac.uk/unichem/info/widesearchInfo

    # chebi: 7
    # brenda: 37

    # TODO: map between BRENDA ligand names & BRENDA ids

    :return:
    """

    logging.warning(f"Parse BRENDA ligand: {brenda_ligand_id}")


    url = "https://www.ebi.ac.uk/unichem/rest/inchikey/AAOVKJBEBIDNHE-UHFFFAOYSA-N"
    print(url)
    response = requests.get(url)
    contents = response.json()
    pprint(contents)



if __name__ == "__main__":
    # get_substance_info(brenda_ligand_id=100)
    data = get_pubchem_collections()


# use unichem for resolution:
# UniChem efficiently produces cross-references between chemical structure identifiers from different databases (more background). Use the form below to search UniChem...
# https://www.ebi.ac.uk/unichem/info/downloads
# https://www.ebi.ac.uk/unichem/info/webservices