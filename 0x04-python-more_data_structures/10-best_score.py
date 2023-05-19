#!/usr/bin/python3
def best_score(a_dictionary):
    """function that returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    max_key = None
    max_value = float('-inf')
    for j, value in a_dictionary.items():
        if value > max_value:
            max_key = j
            max_value = value
    return max_key
