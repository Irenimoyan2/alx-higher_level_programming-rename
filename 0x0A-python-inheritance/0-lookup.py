#!/usr/bin/python3

def lookup(obj):
    """function that returns the list of available 
    attributes and methods of an object:
    """
    attributes = []
    methods = []

    # Get all the attributes and methods of the object
    for name in dir(obj):
        if callable(getattr(obj, name)):
            methods.append(name)
        else:
            attributes.append(name)

            return attributes + methods
