#!/usr/bin/python3
"""
Contain one module
"""


class BaseGeometry:
    """
    Non empty class
    """
    def area(self):
        """
        Write a class BaseGeometry (based on 6-base_geometry.py).
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
