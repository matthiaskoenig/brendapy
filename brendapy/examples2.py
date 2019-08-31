"""
Examples of using brendapy
"""
import pandas as pd
import logging
from collections import OrderedDict

from brendapy import BrendaParser, BrendaProtein
from brendapy.taxonomy import Taxonomy

from collections import Counter
from pprint import pprint

BRENDA_PARSER = BrendaParser()  # reuse parser


def parse_parameters_for_ec(ec="1.1.1.1"):
    """Parse the protein entries for a given EC number in BRENDA.
    """
    proteins = BRENDA_PARSER.get_proteins(ec)
    for pkey, p in proteins.items():
        print(p.ec)
        print(p.organism)
        print(p.taxonomy)
        print(p.tissues)

        if p.SA:  # no substrate
            print("*** SA ***")
            pprint(p.SA)

        if p.KM:  # substrate
            print("*** KM ***")
            pprint(p.KM)
        if p.KI:  # substrate
            print("*** KI ***")
            pprint(p.KI)

        if p.KKM:  # no substrate
            print("*** KKM ***")
            pprint(p.KKM)
        print("-" * 80)


def missing_chebi_substances():
    missing_chebi = Counter()
    for ec in BRENDA_PARSER.keys():
        proteins = BRENDA_PARSER.get_proteins(ec)
        for pkey, p in proteins.items():

            km = p.KM
            if km:
                missing = [item['substrate'] for item in km if ("substrate" in item) and (not "chebi" in item)]
                missing_chebi.update(missing)
            ki = p.KI
            if ki:
                missing = [item['substrate'] for item in ki if ("substrate" in item) and (not "chebi" in item)]
                missing_chebi.update(missing)

    return missing_chebi


def missing_bto_tissues():
    """ Find all source/tissue keys which are not defined in BTO.

    :return:
    """
    missing_tissues = Counter()
    for ec in BRENDA_PARSER.keys():
        proteins = BRENDA_PARSER.get_proteins(ec)
        for pkey, p in proteins.items():
            st = p.ST
            if st:
                missing = [item['data'] for item in st if not "bto" in item]
                missing_tissues.update(missing)

    return missing_tissues


if __name__ == "__main__":

    def _serialize_json(data, path):
        import json
        with open(path, "w") as f:
            json.dump(data, fp=f, indent=2)

    # parse_parameters_for_ec()


    missing_substances = missing_chebi_substances()
    pprint(missing_substances)
    # _serialize_json(missing_substances, path="missing_substances.json")

    with open("missing_substances.txt", "w") as f:
        for key, count in missing_substances.most_common():
            f.write(f"{count} : {key}\n")


    missing_tissues = missing_bto_tissues()
    pprint(missing_tissues)
    # _serialize_json(missing_tissues, path="missing_tissues.json")

    with open("missing_tissues.txt", "w") as f:
        for key, count in missing_tissues.most_common():
            f.write(f"{count} : {key}\n")
