#!/usr/bin/python3
"""
This module contains one function
"""


def print_square(size):
    """
    Function that prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    count = 0
    while count < size:
        print("#" * size)
        count += 1
