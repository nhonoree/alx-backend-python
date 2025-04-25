#!/usr/bin/env python3
"""Duck typing - first element of a sequence"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each element and its length"""
    return [(i, len(i)) for i in lst]
