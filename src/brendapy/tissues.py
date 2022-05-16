"""Tissue information."""

import json

from brendapy.ontologies.owl_parser import BTO_JSON


with open(BTO_JSON, "r") as fin:
    BTO = json.load(fin)

if __name__ == "__main__":
    print("Loading tissue information")
    print(BTO["liver"])
