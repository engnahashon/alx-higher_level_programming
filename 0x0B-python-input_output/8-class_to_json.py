#!/usr/bin/python3
"""Python module for task 8. Class to JSON"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object:
    """
    return(obj.__dict__)
