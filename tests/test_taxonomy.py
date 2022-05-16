import pytest
from brendapy.taxonomy import Taxonomy

TAXONOMY = Taxonomy()


def test_get_taxonomy_id():
    """ Test the module """
    tid = TAXONOMY.get_taxonomy_id("Homo sapiens")
    assert tid == 9606

    tid = TAXONOMY.get_taxonomy_id("Mus musculus")
    assert tid == 10090


def test_get_scientific_name():
    """ Test the module """
    tid = TAXONOMY.get_scientific_name(9606)
    assert tid == "Homo sapiens"

    tid = TAXONOMY.get_scientific_name(10090)
    assert tid == "Mus musculus"

    tid = TAXONOMY.get_scientific_name("9606")
    assert tid == "Homo sapiens"

    tid = TAXONOMY.get_scientific_name("10090")
    assert tid == "Mus musculus"

    tid = TAXONOMY.get_scientific_name("TAX:9606")
    assert tid == "Homo sapiens"

    tid = TAXONOMY.get_scientific_name("TAX:10090")
    assert tid == "Mus musculus"


def test_find_common_node_by_name():
    common = TAXONOMY.find_common_node_by_name("Mus musculus", "Homo sapiens")
    assert common[0]
    assert common[1]
    assert common[2] > 1


def test_find_common_node():
    common = TAXONOMY.find_common_node(10090, 9606)
    assert common[0]
    assert common[1]
    assert common[2] > 1


def test_find_common_node2():
    common1 = TAXONOMY.find_common_node(10090, 9606)
    common2 = TAXONOMY.find_common_node(10090, 9606)
    assert common1[0] == common2[0]
    assert common1[1] == common2[1]


def test_parent_nodes():
    p1 = TAXONOMY.get_parent_nodes(tax_id=7227)
    assert p1
    p2 = TAXONOMY.get_parent_nodes(tax_id="7227")
    assert p2
    p3 = TAXONOMY.get_parent_nodes(tax_id="TAX:7227")
    assert p3

    assert p1 == p2
    assert p1 == p3
