
import pytest
from brendapy import BrendaParser, BrendaProtein
from brendapy.settings import BRENDA_FILE


def test_parsing():
    brenda = BrendaParser()
    assert brenda
    assert "1.1.1.1" in brenda.ec_text


def test_parsing_from_file():
    brenda = BrendaParser(brenda_file=BRENDA_FILE)
    assert brenda
    assert "1.1.1.1" in brenda.ec_text


def test_protein():
    """ Test the proteinBRENDA module """
    brenda = BrendaParser()

    ec = "1.1.1.1"
    proteins = brenda.parse_proteins(ec)
    assert proteins
    assert len(proteins) == 167


def test_protein_detail1():
    brenda = BrendaParser()
    ec = "1.1.1.1"
    ec_str = brenda.ec_text[ec]
    protein = BrendaProtein(ec=ec, id=1, ec_string=ec_str)
    assert protein
    assert 'liver' in protein.source_tissue
    assert protein.organism == "Gallus gallus"
    assert 44 in protein.references
    assert len(protein.pubmed) == 1


def test_protein_detail2():
    brenda = BrendaParser()
    ec = "1.1.1.1"
    ec_str = brenda.ec_text[ec]
    protein = BrendaProtein(ec=ec, id=4, ec_string=ec_str)
    assert protein
    assert protein.organism == "Drosophila melanogaster"

    assert 8 in protein.references
    assert len(protein.pubmed) == 7


'''
def test_all_proteins():
    brenda = BrendaParser()
    for ec in brenda.keys():
        print(ec)
        proteins = brenda.parse_proteins(ec)

def test_info_dict():
    brenda = BrendaParser()
    ec = "1.1.1.2"
    ec_str = brenda.ec_text[ec]
    d = brenda.parse_info_dict(ec_str)
    from pprint import pprint
    pprint(d)
    import json
    assert False
'''
