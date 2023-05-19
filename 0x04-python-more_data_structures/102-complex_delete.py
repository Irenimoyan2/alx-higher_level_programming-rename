#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """function that deletes keys with a specific value in a dictionary"""
    keys_to_delete = []

    for j, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(j)

    for j in keys_to_delete:
        del a_dictionary[j]

    return a_dictionary
