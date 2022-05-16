"""brendapy - BRENDA in python."""

from .parser import BrendaParser
from .parser import BrendaProtein

__author__ = "Matthias Koenig"
__version__ = "0.5.0"


from depinfo import print_dependencies  # type: ignore


def show_versions() -> None:
    """Print dependency information."""
    print_dependencies("pymetadata")
