#!/usr/bin/python3
"""
Module contains a class that inherits from a baseclasee
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class contains one module
    """
    def __init__(self, width, height):
        """
        Write a class Rectangle that inherits from BaseGeometry
        """
        super().integer_validator("width", width)
        super().integer_validator("height",  height)
        self.__width = width
        self.__height = height
