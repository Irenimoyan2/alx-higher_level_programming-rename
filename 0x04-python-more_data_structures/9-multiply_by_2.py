#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with all values multiplied by 2"""
    new_dictionary = {}
    for j, value in a_dictionary.items():
        new_dictionary[j] = value * 2
    return new_dictionary
