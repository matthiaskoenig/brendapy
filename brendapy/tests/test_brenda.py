
import pytest
import logging
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


def test_protein1():
    """ Test the proteinBRENDA module """
    brenda = BrendaParser()

    ec = "1.1.1.1"
    proteins = brenda.get_proteins(ec)
    assert proteins
    assert len(proteins) == 167


def test_protein_detail1():
    brenda = BrendaParser()
    ec = "1.1.1.1"
    proteins = brenda.get_proteins(ec)
    protein = proteins[1]

    assert protein
    assert 'liver' in protein.source_tissues
    assert protein.organism == "Gallus gallus"
    assert 44 in protein.references


def test_protein_detail2():
    brenda = BrendaParser()
    ec = "1.1.1.1"
    proteins = brenda.get_proteins(ec)
    protein = proteins[4]

    assert protein
    assert protein.organism == "Drosophila melanogaster"
    assert 8 in protein.references


brenda_parser = BrendaParser()
@pytest.mark.parametrize("ec", BrendaParser().keys())
def test_proteins_for_ec(ec):
    proteins = brenda_parser.get_proteins(ec)
    assert proteins is not None


def test_info_dict():
    brenda = BrendaParser()
    ec = "1.1.1.2"
    ec_str = brenda.ec_text[ec]
    d = brenda._parse_info_dict(ec, ec_str)
    assert d


