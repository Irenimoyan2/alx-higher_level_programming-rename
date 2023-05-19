#!/usr/bin/python3
def weight_average(my_list=[]):
    """ function that returns the weighted average of all integers tuple"""
    if len(my_list) == 0:
        return 0

    total_weight = 0
    total_score = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight
