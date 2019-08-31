"""
Examples of using brendapy
"""
import pandas as pd
import logging
from collections import OrderedDict

from brendapy import BrendaParser, BrendaProtein
from brendapy.taxonomy import Taxonomy
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

        if p.SA:
            print("*** SA ***")
            pprint(p.SA)
        if p.KM:
            print("*** KM ***")
            pprint(p.KM)
        if p.KI:
            print("*** KI ***")
            pprint(p.KI)
        if p.KKM:
            print("*** KKM ***")
            pprint(p.KKM)
        print("-" * 80)


def parse_parameters():
    for ec in BRENDA_PARSER.keys():
        proteins = parse_parameters_for_ec(ec)


def missing_bto_tissues():
    """ Find all source/tissue keys which are not defined in BTO.

    :return:
    """
    from collections import Counter
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
    # parse_parameters_for_ec()
    missing_tissues = missing_bto_tissues()
    from pprint import pprint
    pprint(missing_tissues)

