import os
import json


from brendapy.settings import RESOURCES_PATH
BTO_DATA = os.path.join(RESOURCES_PATH, "bto", "bto.json")

with open(BTO_DATA, "r") as fin:
    BTO = json.load(fin)

if __name__ == "__main__":
    print("Loading tissue information")
    print(BTO["liver"])
