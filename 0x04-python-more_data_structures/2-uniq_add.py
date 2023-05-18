#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function that adds all unique integers in a list"""
    unique_integers = set(my_list)
    # Sum up the unique integers
    total = sum(unique_integers)
    return total
