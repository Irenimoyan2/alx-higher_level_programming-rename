#!/usr/bin/python3
"""
This module contains one function
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix."""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \(list of lists\) of integers/floats")
    for i in range(len(matrix)):
        inner_res = []
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix \(list of lists\) of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix \(list of lists\) of integers/floats")
            inner_res.append(round(j / div, 2))
        result.append(inner_res)
    return result
