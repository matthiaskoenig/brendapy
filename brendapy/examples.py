"""
Examples of using brendapy
"""
from pprint import pprint
from brendapy import BrendaParser, BrendaProtein


def parse_proteins_for_ec():
    """Parse the protein entries for a given EC number in BRENDA.

    Prints overview of proteins, protein ids, and Human proteins.
    """
    brenda = BrendaParser()
    ec = "1.1.1.1"
    proteins = brenda.parse_proteins(ec)

    print(f"{len(proteins)} proteins for EC {ec} in BRENDA")
    print(f"Protein identifier: {proteins.keys()}")
    print("-"*80)
    for p in proteins.values():
        if p.organism == "Homo sapiens":
            print(p)
            print("-" * 80)




if __name__ == "__main__":
    # parse_proteins_for_ec()

    brenda = BrendaParser()
    ec = "1.14.13.29"
    ec_str = brenda.ec_text[ec]
    with open(f"{ec}.txt", "w") as f_ec:
        f_ec.write(ec_str)

    d = brenda._parse_info_dict(ec_str)
    from pprint import pprint

    # print(ec_str)
    print("---")
    # pprint(d["RN"])
    pprint(d)
    print("---")
    import json