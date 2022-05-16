# brendapy resources
Due to the size limit on `git` and `pypi` the resources have to be fetched on import.

To update the resources download the following files

## BRENDA
Download latest BRENDA file and README from https://www.brenda-enzymes.org/download_brenda_without_registration.php
to `resources/data/brenda/brenda_download.txt` and `resources/data/brenda/brenda_readme.txt` 
* Release 2022.1 (February 1, 2022) is online including 76 new and 428 updated enzyme classes.

## Taxonomy
This uses the NCBI taxonomy data available from ftp://ftp.ncbi.nih.gov/pub/taxonomy/. 
Download the `taxdmp.zip` to `resources/data/taxonomy/taxdmp.zip`.
* The taxonomy was downloaded on 2022-05-16 (ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip)

## ChEBI
Ontologies have been downloaded from https://www.ebi.ac.uk/ols/ontologies/chebi as OWL format
* Downloaded on 2022-05-16 with version 25:03:2022 01:58

## BTO
Ontologies have been downloaded from https://www.ebi.ac.uk/ols/ontologies/bto as OWL format




TAXONOMY_DATA = os.path.join(RESOURCES_PATH, "data", "taxonomy", "taxonomy.json")
TAXONOMY_ZIP = os.path.join(RESOURCES_PATH, "data", "taxonomy", "taxdmp.zip")
BTO_DATA = os.path.join(RESOURCES_PATH, "data", "bto", "bto.json")
CHEBI_DATA = os.path.join(RESOURCES_PATH, "data", "chebi", "chebi.json")
