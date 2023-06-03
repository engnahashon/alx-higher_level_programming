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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        instance_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                json_data = f.read()
                obj_list = cls.from_json_string(json_data)

                for obj in obj_list:
                    instance = cls.create(**obj)
                    instance_list.append(instance)

        except FileNotFoundError:
            return []

        return instance_list
