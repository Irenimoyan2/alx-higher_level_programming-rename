#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ function that prints a dictionary by ordered keys."""
    sorted_keys = sorted(a_dictionary.keys())

    for i in sorted_keys:
        value = a_dictionary[i]
        print(f"{i}: {value}")
