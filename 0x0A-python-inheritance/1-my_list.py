#!/usr/bin/python3
"""
This module contains one function
"""


class MyList(list):
    """
    This class contains a single method
    """
    def print_sorted(self):
        """
        Write a class MyList that inherits from list
        """
        sorted_list = sorted(self)
        print(sorted_list)
