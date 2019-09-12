import pytest
import logging
from brendapy import BrendaParser, BrendaProtein
from brendapy.settings import BRENDA_FILE

BRENDA_PARSER = BrendaParser()


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
    ec = "1.1.1.1"
    proteins = BRENDA_PARSER.get_proteins(ec)
    assert proteins
    assert len(proteins) == 167


def test_protein_detail1():
    proteins = BRENDA_PARSER.get_proteins(ec="1.1.1.1")
    protein = proteins[1]

    assert protein

    tissues = [item['data'] for item in protein.ST]
    assert 'liver' in tissues
    assert protein.organism == "Gallus gallus"
    assert protein.taxonomy == 9031
    assert 44 in protein.references


def test_protein_detail2():
    proteins = BRENDA_PARSER.get_proteins("1.1.1.1")
    protein = proteins[4]

    assert protein
    assert protein.organism == "Drosophila melanogaster"
    assert 8 in protein.references


def test_info_dict():
    ec = "1.1.1.2"
    ec_str = BRENDA_PARSER.ec_text[ec]
    d = BRENDA_PARSER._parse_info_dict(ec, ec_str)
    assert d


def test_organism():
    """test https://github.com/matthiaskoenig/brendapy/issues/16
    :return:
    """
    proteins = BRENDA_PARSER.get_proteins("1.1.1.1")
    p = proteins[106]
    assert p.organism == "Homo sapiens"


def test_source_tissue_reference():
    """test https://github.com/matthiaskoenig/brendapy/issues/13

    ST	#3# lymphocyte <34,40,51>
    ST	#3# skin fibroblast <31>
    ST	#3,4# more (#3# cell line 3152 and cell line 13042 <31>; #4# in adult,
        absent from astrocytes, oligodendrocytes and microcapillary endothelial
        cells (blood-brain barrier). Present in rhombencephalon of embryos
        <41>; #4# PCCalpha is present in choroid plexus epithelium, is absent
        from astrocytes and oligodendrocytes and in microcapillary endothelial
        cells (blood brain barrier) <41>; #3# two-years-old girl with
        propionic acidemia <42>) <31,41,42>
    ST	#3,4,6# liver (#4# in embryos (E15.5 and E18.5), PCCalpha shows a much
        higher expression level in the entire central nervous system than in
        the liver <41>; #4# low levels in the E15.5 embryonic liver <41>)
        <5,6,16,41>

    :return:
    """
    proteins = BRENDA_PARSER.get_proteins("6.4.1.3")
    p = proteins[3]

    source_tissues = p.data["ST"]
    assert source_tissues
    assert len(source_tissues) == 3

    st1 = source_tissues[0]
    assert st1['data'] == "lymphocyte"
    assert len(st1['refs']) == 3
    for ref in [34, 40, 51]:
        assert ref in st1['refs']

    st2 = source_tissues[1]
    assert st2['data'] == "skin fibroblast"
    assert len(st2['refs']) == 1
    assert 31 in st2['refs']

    st3 = source_tissues[2]
    assert st3['data'] == "liver"
    assert len(st3['refs']) == 4
    for ref in [5, 6, 16, 41]:
        assert ref in st3['refs']


def test_substances():
    """test https://github.com/matthiaskoenig/brendapy/issues/12

    KM	#4,5# 2.4 {2-oxoglutarate}  (#4# pH 8.0, 25°C, substrate L-isoleucine
        <23,40>; #5# pH 8.4, 25°C, substrate L-alloisoleucine <41>) <23,40,41>
    KM	#4,5,17,63# 1.7 {2-oxoglutarate}  (#4# pH 8.0, 25°C, substrate L-valine
        <23,40>; #5,17# pH 8.0, 37°C, isoenzyme III, valine as amino group
        donor <24>; #63# half transamination reaction, pH 8.0, 90°C <96>)
        <23,24,40,96>
    KM	#4,5,6,17# 1 {2-oxoglutarate}  (#6# pH 8.2, 37°C <7>; #4# pH 8.0, 25°C,
        substrate L-methionine <23,40>; #5# pH 8.0, 37°C, isoenzyme III,
        leucine as amino group donor <24>; #17# pH 8.0, 37°C, isoenzyme III,
        isoleucine as amino group donor <24>) <7,23,24,40>
    KM	#5# 0.06 {(R)-3-methyl-2-oxopentanoate}  (#5# pH 8.0, 25°C, substrate
        L-glutamate <41>) <41>
    KM	#5# 0.17 {(S)-3-methyl-2-oxopentanoate}  (#5# pH 8.0, 25°C, substrate
        L-glutamate <41>) <41>
    ...
    :return:
    """
    proteins = BRENDA_PARSER.get_proteins("2.6.1.42")
    p = proteins[5]
    data = p.data["KM"]
    assert data[0]["data"] == "2.4 {2-oxoglutarate}"
    assert data[0]["value"] == 2.4
    assert data[0]["substrate"] == "2-oxoglutarate"
    assert data[0]["units"] == "mM"

    assert data[1]["data"] == "1.7 {2-oxoglutarate}"
    assert data[2]["data"] == "1 {2-oxoglutarate}"
    assert data[3]["data"] == "0.06 {(R)-3-methyl-2-oxopentanoate}"
    assert data[4]["data"] == "0.09 {(S)-3-methyl-2-oxopentanoate}"
    assert data[0]["comment"] == "#4# pH 8.0, 25°C, substrate L-isoleucine <23,40>; #5# pH 8.4, 25°C, substrate L-alloisoleucine <41>"  # noqa: E501


def test_minus_999():
    """test https://github.com/matthiaskoenig/brendapy/issues/8

    :return:
    """
    proteins = BRENDA_PARSER.get_proteins("1.1.1.100")
    p = proteins[2]
    data = p.data["IC50"]
    assert len(data) == 2


def test_unique_ki_entries():
    """Testing https://github.com/matthiaskoenig/brendapy/issues/30.
     Checking that no duplicates are written.
     """
    proteins = BRENDA_PARSER.get_proteins("1.1.1.1")
    for key, p in proteins.items():
        if key != 5:
            continue
        assert len(p.KI) == 9


def test_uniprot_swissprot_parsing():
    """Testing https://github.com/matthiaskoenig/brendapy/issues/28.
     Test that uniprot/swissprot are extracted from PR items.
     """
    proteins = BRENDA_PARSER.get_proteins("1.1.1.1")

    p1 = proteins[109]
    assert p1.uniprot == "P08319"
    p2 = proteins[128]
    assert p2.uniprot is None
    p3 = proteins[120]
    assert p3.uniprot == "P00331"


def test_source_tissue():
    ec = "1.1.1.2"
    ec_str = BRENDA_PARSER.ec_text[ec]
    d = BRENDA_PARSER._parse_info_dict(ec, ec_str)
    assert d


@pytest.mark.parametrize("ec", BRENDA_PARSER.keys())
def test_proteins_for_ec(ec):
    proteins = BRENDA_PARSER.get_proteins(ec)
    assert proteins is not None
