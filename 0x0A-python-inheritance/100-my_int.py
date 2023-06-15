#!/usr/bin/python3
"""
Module contains a class
"""


class MyInt(int):
    """
    Write a class MyInt that inherits from int:
    """
    def __eq__(self, other):
        """ doc """
        return super().__ne__(other)

    def __ne__(self, other):
        """ doc here """
        return super().__eq__(other)
