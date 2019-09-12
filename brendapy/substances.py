# -*- coding: utf-8 -*-
import os
import json
from zipfile import ZipFile

from brendapy.settings import RESOURCES_PATH
CHEBI_DATA = os.path.join(RESOURCES_PATH, "chebi.json")
CHEBI_ZIP = os.path.join(RESOURCES_PATH, "chebi.json.zip")

if not os.path.exists(CHEBI_DATA):
    with ZipFile(CHEBI_ZIP, 'r') as zipObj:
        zipObj.extractall(RESOURCES_PATH)

with open(CHEBI_DATA, "r") as fin:
    CHEBI = json.load(fin)


if __name__ == "__main__":
    from pprint import pprint
    print("Loading chebi information")
    pprint(CHEBI["D-glucose"])
