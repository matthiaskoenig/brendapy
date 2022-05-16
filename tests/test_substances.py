"""Test substance model."""
from brendapy.substances import CHEBI


def test_chebi_dglc() -> None:
    """Test chebi for D-glucose."""
    assert CHEBI["D-glucose"] == "CHEBI:17634"
