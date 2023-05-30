#!/usr/bin/python3
"""Module for the Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self))
        elif value <= 0:
            raise ValueError('{} must be > 0'.format(self))
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self))
        elif value <= 0:
            raise ValueError('{} must be > 0'.format(self))
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self))
        elif value < 0:
            raise ValueError('{} must be >= 0'.format(self))
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self))
        elif value < 0:
            raise ValueError('{} must be >= 0'.format(self))
        else:
            self.__y = value
