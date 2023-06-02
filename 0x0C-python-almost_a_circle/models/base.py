#!/usr/bin/python3
"""Base Module for project 0x0C. Python - Almost a circle"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        my_obj = []

        if list_objs is not None:
            for obj in list_objs:
                my_obj.append(cls.to_dictionary(obj))

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(my_obj))
