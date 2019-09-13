# -*- coding: utf-8 -*-
import json
from brendapy.settings import CHEBI_DATA

with open(CHEBI_DATA, "r") as fin:
    CHEBI = json.load(fin)


if __name__ == "__main__":
    from pprint import pprint
    print("Loading chebi information")
    pprint(CHEBI["D-glucose"])
