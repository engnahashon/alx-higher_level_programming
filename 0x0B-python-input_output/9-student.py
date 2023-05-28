#!/usr/bin/python3
"""Python script for task 9. Student to JSON"""


class Student:
    """Public instance attributes:first_name last_name age"""
    def __init__(self, first_name, last_name, age):
        """initantiation of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return (self.__dict__)
