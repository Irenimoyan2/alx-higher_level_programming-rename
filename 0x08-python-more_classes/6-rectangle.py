#!/usr/bin/python3
"""A module containing a rectangle class"""


class Rectangle:
    """Represent a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            if width < 0:
                raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            if height < 0:
                raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        ...
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        ...
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        ...
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        ...
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += "#" * self.__width
            output += "\n"

        return output.rstrip()

    def __repr__(self):
        """Return the string representation of the Rectangle. """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        ...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
