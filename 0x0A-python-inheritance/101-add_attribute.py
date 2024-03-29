#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Raise a TypeError exception, with the message can't
    add new attribute if the object can’t have new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__setattr__(attr_name, attr_value)
