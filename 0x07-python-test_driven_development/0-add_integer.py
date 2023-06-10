#!/usr/bin/python3
"""
Module contains one function
"""


def add_integer(a, b=98):
    """Function that adds 2 integers."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)

    return a + b
