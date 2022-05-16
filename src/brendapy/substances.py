"""Loading substances."""


import json

from brendapy.ontologies.owl_parser import CHEBI_JSON


with open(CHEBI_JSON, "r") as fin:
    CHEBI = json.load(fin)


if __name__ == "__main__":
    from pprint import pprint

    print("Loading chebi information")
    pprint(CHEBI["D-glucose"])
