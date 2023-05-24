#!/usr/bin/python3
"""Python script for task 4"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that
    inherited from the specified class ; otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
         return False
