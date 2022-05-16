"""Utility functions."""

import time
from typing import Any, Callable, List


def is_ec_number(ec: str) -> bool:
    """Test if given string 'ec' is EC number.

    :param ec: ec string
    :return: True if EC number, False otherwise
    """
    ec_items: List[str] = ec.strip().split(".")
    for number in ec_items:
        if not number.isdigit():
            return False
    return True


def timeit(method: Callable) -> Any:
    """Decorate function with timing functionality."""

    def timed(*args, **kw) -> Any:
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if "log_time" in kw:
            name = kw.get("log_name", method.__name__.upper())
            kw["log_time"][name] = int((te - ts) * 1000)
        else:
            print("%r  %2.2f ms" % (method.__name__, (te - ts) * 1000))
        return result

    return timed
