"""
Examples of using brendapy
"""
import pandas as pd
import logging
from collections import OrderedDict

from brendapy import BrendaParser, BrendaProtein
from brendapy.taxonomy import Taxonomy


def parse_proteins_for_ec():
    """Parse the protein entries for a given EC number in BRENDA.

    Prints overview of proteins, protein ids, and Human proteins.
    """
    brenda = BrendaParser()
    ec = "1.1.1.1"
    proteins = brenda.get_proteins(ec)

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
    brenda = BrendaParser()
    tax = Taxonomy()
    ec = "1.1.1.1"  # enzyme of interest
    tax_id_ref = tax.get_taxonomy_id("Homo sapiens")  # tax id of target species

    proteins = brenda.get_proteins(ec)

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
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 30)
    print("-" * 80)
    print(df)
    print("-" * 80)


if __name__ == "__main__":
    # parse_proteins_for_ec()
    parse_proteins_by_taxonomy()
