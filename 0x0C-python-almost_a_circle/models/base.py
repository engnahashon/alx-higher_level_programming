#!/usr/bin/python3
"""Base Module for project 0x0C. Python - Almost a circle"""


class Base:
    """Base model 0x0C. Python - Almost a circle"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
