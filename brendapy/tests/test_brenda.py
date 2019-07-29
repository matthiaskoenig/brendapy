import pytest
import os
base_path = os.path.dirname(os.path.realpath(__file__))
from brendapy import parser

brenda_file = os.path.join(base_path, "..", "..", 'data', 'brenda_download.txt')


def test_parsing():
	brenda = parser.BRENDAparser(brenda_file)
	assert brenda
	assert "1.1.1.1" in brenda.ec_data


def test_protein():
	""" Test the proteinBRENDA module """
	ec = "1.1.1.1"
	brenda = parser.BRENDAparser(brenda_file)
	proteins = brenda.parse_proteins(ec)
	assert proteins
	assert len(proteins) == 167
