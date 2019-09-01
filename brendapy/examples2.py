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
from copy import deepcopy

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

        if p.KM:  # substrate
            print("*** KM ***")
            pprint(p.KM)

        if p.TN:  # substrate
            print("*** TN ***")
            pprint(p.TN)

        if p.KI:  # substrate
            print("*** KI ***")
            pprint(p.KI)

        if p.KKM:  # no substrate
            print("*** KKM ***")
            pprint(p.KKM)

        if p.SA:  # no substrate
            print("*** SA ***")
            pprint(p.SA)
        print("-" * 80)


def parse_all_parameters():
    """ Parses all KM, KI, SA, TN and KKM

    :return:
    """

    # Keep track of information which cannot be mapped to ontologies
    unmapped_organisms = Counter()
    unmapped_substances = Counter()
    unmapped_tissues = Counter()

    def find_mapped_substances(items):
        """ Find entries with substance information mapped to chebi."""
        mapped = []
        unmapped = []
        for item in items:
            if "substrate" in item:
                if "chebi" in item:
                    mapped.append(item)
                else:
                    unmapped.append(item['substrate'])

        return mapped, unmapped

    results = {}

    for ec in BRENDA_PARSER.keys():
        proteins = BRENDA_PARSER.get_proteins(ec)
        for pkey, p in proteins.items():

            # unmapped organisms
            if not p.taxonomy:
                unmapped_organisms.update([p.organism])

            # unmapped tissues
            if p.ST:
                unmapped_tissues.update(
                    [item['data'] for item in p.ST if not "bto" in item]
                )

            # resolve parameters (track unmapped substances
            data = {}
            if p.KM:
                mapped, unmapped = find_mapped_substances(p.KM)
                unmapped_substances.update(unmapped)
                data['KM'] = deepcopy(mapped)
            if p.KI:
                mapped, unmapped = find_mapped_substances(p.KI)
                unmapped_substances.update(unmapped)
                data['KI'] = deepcopy(mapped)
            if p.TN:
                mapped, unmapped = find_mapped_substances(p.TN)
                unmapped_substances.update(unmapped)
                data['TN'] = deepcopy(mapped)
            if p.KKM:
                data['KKM'] = deepcopy(p.KKM)
            if p.SA:
                data['SA'] = deepcopy(p.SA)

            # parameter for export (full annotation)
            if p.taxonomy:
                ec_str = (p.ec).replace('.', '_')
                eid = f"EC{ec_str}__PR{p.protein_id}"
                entry = {
                    'eid': eid,
                    'ec': p.ec,
                    'taxonomy': p.taxonomy,
                    'protein_id': p.protein_id,
                    'data': data
                }
                results[eid] = entry

    return results, unmapped_organisms, unmapped_substances, unmapped_tissues


def _serialize_json(data, path):
    """Serialize dict to json."""
    import json
    with open(path, "w") as f:
        json.dump(data, fp=f, indent=2)


def _serialize_counter(counter, path):
    """Serialize Counter to text file."""
    with open(path, "w") as fout:
        for key, count in counter.most_common():
            fout.write(f"{count} : {key}\n")


if __name__ == "__main__":
    # parse_parameters_for_ec()

    results, unmapped_organisms, unmapped_substances, unmapped_tissues = parse_all_parameters()

    _serialize_json(results, path="./resources/parameters.json")
    _serialize_counter(unmapped_organisms, path="./resources/unmapped_organisms.txt")
    _serialize_counter(unmapped_tissues, path="./resources/unmapped_tissues.txt")
    _serialize_counter(unmapped_substances, path="./resources/unmapped_substances.txt")

