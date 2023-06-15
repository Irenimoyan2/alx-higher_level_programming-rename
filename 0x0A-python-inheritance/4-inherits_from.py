#!/usr/bin/python3
"""
Contains one module
"""


def inherits_from(obj, a_class):
    """
    Function thats checks if instance is True or False
    """
    if issubclass(obj.__class__, a_class):
        if obj.__class__ is not a_class:
            return True

        return False
