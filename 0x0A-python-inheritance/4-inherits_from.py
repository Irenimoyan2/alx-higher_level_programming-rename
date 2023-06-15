#!/usr/bin/python3
"""
Contains one module
"""


def inherits_from(obj, a_class):
    """
    Function thats checks for instance and subclass
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
