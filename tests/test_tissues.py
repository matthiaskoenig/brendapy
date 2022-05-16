"""Test tissues."""
from brendapy.tissues import BTO


def test_bto_liver() -> None:
    """Test chebi for D-glucose."""
    assert BTO["liver"] == "BTO:0000759"
