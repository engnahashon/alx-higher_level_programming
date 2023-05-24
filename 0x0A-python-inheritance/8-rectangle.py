#!/usr/bin/python3
"""Script for task no 8-Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize the attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
