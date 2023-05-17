#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for j in my_list:
        result.append(j % 2 == 0)
    return result
