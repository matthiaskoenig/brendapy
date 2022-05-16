"""Examples of using brendapy."""
from typing import Dict

import pandas as pd

from brendapy import BrendaParser, BrendaProtein
from brendapy.console import console
from brendapy.log import get_logger
from brendapy.taxonomy import Taxonomy


logger = get_logger(__name__)
BRENDA_PARSER = BrendaParser()


def parse_proteins_for_ec(ec: str = "1.1.1.1") -> Dict[int, BrendaProtein]:
    """Parse the protein entries for a given EC number in BRENDA."""
    proteins = BRENDA_PARSER.get_proteins(ec)
    return proteins


def parse_human_proteins_for_ec(ec: str = "1.1.1.1") -> None:
    """Parse the protein entries for a given EC number in BRENDA.

    Prints overview of proteins, protein ids, and Human proteins.
    """
    proteins = BRENDA_PARSER.get_proteins(ec)

    console.print(f"{len(proteins)} proteins for EC {ec} in BRENDA")
    console.print(f"Protein identifier: {proteins.keys()}")
    console.rule()
    for p in proteins.values():
        if p.organism == "Homo sapiens":
            console.print(p)
            console.rule()


def parse_proteins_by_taxonomy() -> None:
    """Sort protein entries by taxonomy information.

    :return:
    """
    tax = Taxonomy()
    ec = "1.1.1.1"  # enzyme of interest
    tax_id_ref = tax.get_taxonomy_id("Homo sapiens")  # tax id of target species

    proteins = BRENDA_PARSER.get_proteins(ec)

    results = []
    for key, p in proteins.items():
        if p.taxonomy is None:
            logger.error(
                f"Taxonomy could not be resolved for protein "
                f"<{p.protein_id}>: '{p.organism}': '{p.taxonomy}'"
            )
            continue

        [common_node_id, common_name, common_dist] = tax.find_common_node(
            tax_id=p.taxonomy, tax_id_ref=tax_id_ref
        )
        results.append(
            {
                "protein_id": key,
                "organism": p.organism,
                "taxonomy": p.taxonomy,
                "common_name": common_name,
                "common_dist": common_dist,
            }
        )

    # sorted data frame
    df = pd.DataFrame(results)
    df = df.sort_values(by=["common_dist"])
    console.rule()
    console.print(df)
    console.rule()


def parse_all_proteins_for_all_ecs() -> Dict[int, BrendaProtein]:
    """Parse all proteins for all ECs."""
    for ec in BRENDA_PARSER.keys():
        proteins = BRENDA_PARSER.get_proteins(ec)
    return proteins


if __name__ == "__main__":
    parse_proteins_for_ec(ec="1.1.1.1")
    parse_human_proteins_for_ec(ec="1.1.1.1")
    parse_proteins_by_taxonomy()
    parse_all_proteins_for_all_ecs()
