# -*- coding: utf-8 -*-
import os
import json

from brendapy.settings import RESOURCES_PATH
CHEBI_DATA = os.path.join(RESOURCES_PATH, "chebi", "chebi.json")

with open(CHEBI_DATA, "r") as fin:
    CHEBI = json.load(fin)

if __name__ == "__main__":
    from pprint import pprint
    print("Loading chebi information")
    pprint(CHEBI["D-glucose"])
