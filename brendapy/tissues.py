# -*- coding: utf-8 -*-
import os
import json
from zipfile import ZipFile

from brendapy.settings import RESOURCES_PATH
BTO_ZIP = os.path.join(RESOURCES_PATH, "bto.json.zip")
BTO_DATA = os.path.join(RESOURCES_PATH, "bto.json")

if not os.path.exists(BTO_DATA):
    with ZipFile(BTO_ZIP, 'r') as zipObj:
        zipObj.extractall(RESOURCES_PATH)

with open(BTO_DATA, "r") as fin:
    BTO = json.load(fin)

if __name__ == "__main__":
    print("Loading tissue information")
    print(BTO["liver"])
