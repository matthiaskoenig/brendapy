# -*- coding: utf-8 -*-
"""
Examples of using brendapy
"""
import pandas as pd
import logging
from collections import OrderedDict

from brendapy import BrendaParser, BrendaProtein
from brendapy.taxonomy import Taxonomy

BRENDA_PARSER = BrendaParser()  # reuse parser


def parse_proteins_for_ec(ec="1.1.1.1"):
    """Parse the protein entries for a given EC number in BRENDA.
    """
    proteins = BRENDA_PARSER.get_proteins(ec)
    return proteins


def parse_human_proteins_for_ec(ec="1.1.1.1"):
    """Parse the protein entries for a given EC number in BRENDA.

    Prints overview of proteins, protein ids, and Human proteins.
    """
    proteins = BRENDA_PARSER.get_proteins(ec)

    print(f"{len(proteins)} proteins for EC {ec} in BRENDA")
    print(f"Protein identifier: {proteins.keys()}")
    print("-" * 80)
    for p in proteins.values():
        if p.organism == "Homo sapiens":
            print(p)
            print("-" * 80)


def parse_proteins_by_taxonomy():
    """ Sort protein entries by taxonomy information.

    :return:
    """
    tax = Taxonomy()
    ec = "1.1.1.1"  # enzyme of interest
    tax_id_ref = tax.get_taxonomy_id("Homo sapiens")  # tax id of target species

    proteins = BRENDA_PARSER.get_proteins(ec)

    results = []
    for key, p in proteins.items():
        if p.taxonomy is None:
            logging.error(f"Taxonomy could not be resolved for protein <{p.protein_id}>: '{p.organism}': '{p.taxonomy}'")
            continue

        [common_node_id, common_name, common_dist] = tax.find_common_node(
            tax_id=p.taxonomy,
            tax_id_ref=tax_id_ref
        )
        results.append(OrderedDict(
            [
                ("protein_id", key),
                ("organism", p.organism),
                ("taxonomy", p.taxonomy),
                ("common_name", common_name),
                ("common_dist", common_dist),
            ])
        )

    # sorted data frame
    df = pd.DataFrame(results)
    df = df.sort_values(by=['common_dist'])
    print("-" * 80)
    print(df)
    print("-" * 80)


def parse_all_proteins_for_all_ecs():
    for ec in BRENDA_PARSER.keys():
        proteins = BRENDA_PARSER.get_proteins(ec)


if __name__ == "__main__":
    parse_proteins_for_ec(ec="1.1.1.1")
    parse_human_proteins_for_ec(ec="1.1.1.1")
    parse_proteins_by_taxonomy()
    parse_all_proteins_for_all_ecs()
