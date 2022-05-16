"""Examples for testing brendapy."""

import pytest

from brendapy.examples import (
    parse_all_proteins_for_all_ecs,
    parse_human_proteins_for_ec,
    parse_proteins_by_taxonomy,
    parse_proteins_for_ec,
)


def test_parse_proteins_for_ec() -> None:
    """Test parsing proteins by EC."""
    parse_proteins_for_ec(ec="1.1.1.1")


def test_parse_human_proteins_for_ec() -> None:
    """Test parsing human proteins by EC."""
    parse_human_proteins_for_ec(ec="1.1.1.1")


def test_parse_proteins_by_taxonomy() -> None:
    """Test parsing proteins by taxonomy."""
    parse_proteins_by_taxonomy()


@pytest.mark.skip(reason="takes too long")
def test_parse_all_proteins_for_all_ecs() -> None:
    """Testing parsing of all proteins for given EC."""
    parse_all_proteins_for_all_ecs()
