#!/usr/bin/python3
"""Python script for task 10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initiliaze the class attributes"""
        self.__size = size
        super().__init__(size, size)
        self.integer_validator('size', size)

    def area(self):
        """Implement the area method"""
        return (self.__size * self.__size)
