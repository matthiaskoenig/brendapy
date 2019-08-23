
import pytest
from brendapy.examples import *


def test_parse_proteins_for_ec():
    parse_proteins_for_ec(ec="1.1.1.1")


def test_parse_human_proteins_for_ec():
    parse_human_proteins_for_ec(ec="1.1.1.1")


def test_parse_proteins_by_taxonomy():
    parse_proteins_by_taxonomy()


def test_parse_all_proteins_for_all_ecs():
    parse_all_proteins_for_all_ecs()
