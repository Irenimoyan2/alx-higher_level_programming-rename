#!/usr/bin/python3
"""
This Module contains one function
"""


def lookup(obj):
    """Function that returns the list of available 
    attributes and methods of an object:
    """
    return [attr for attr in dir(obj)]
