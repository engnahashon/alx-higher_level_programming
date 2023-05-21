#!/usr/bin/python3
"""Python module to list all the attributes"""


def lookup(obj):
    """ returns the list of available attributes and methods of an object"""
    return dir(obj)
