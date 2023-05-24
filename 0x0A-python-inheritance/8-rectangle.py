#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Script for task no 8-Rectangle"""


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize the attributes"""
        self.width = width
        self.height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
