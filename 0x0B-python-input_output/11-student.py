#!/usr/bin/python3
"""Python script for task 11. Student to disk and reload"""


class Student:
    """Public instance attributes:first_name last_name age"""
    def __init__(self, first_name, last_name, age):
        """initantiation of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return (self.__dict__)
        new_dict = {}
        for obj in attrs:
            if hasattr(self, obj):
                new_dict[obj] = getattr(self, obj)
        return (new_dict)

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for obj in json:
            self.__dict__[obj] = json[obj]
