"""Fixtures for pytest."""

import pytest


def pytest_sessionstart(session):
    """Session setup for brendapy tests.

    Force download of resources before beginning the test.
    """
    # download resources if not existing
    import brendapy
