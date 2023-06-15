#!/usr/bin/python3
"""
Contains a class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Write a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        initialisation
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns Area """
        return self.__size * self.__size

    def __str__(self):
        """ the str() """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
