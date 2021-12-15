#!/usr/bin/python3
"""
Module 0-add_integer
Contains method that returns an integer sum
Accepts two args, whether int or float, and casts them to integer before adding
"""


def add_integer(a, b=98):
    """
    Returns a + b as int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
