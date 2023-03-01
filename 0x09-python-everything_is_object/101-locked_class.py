#!/usr/bin/python3
"""class LockedClass with no class or object attribute"""


class LockedClass:
    """class LockedClass with no class or object attribute"""
    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(attr))
        self.__dict__.update({attr: value})
