#!/usr/bin/python3
"""
Contains a class that inherits from base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    contains init method only
    """
    def __init__(self, width, height):
        """
        Write a class Rectangle that inherits from BaseGeometry
        """
        super().integer_validator("width", width)
        super().integer_validator("height",  height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns Area """
        return self.__width * self.__height

    def __str__(self):
        """ the str() """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
