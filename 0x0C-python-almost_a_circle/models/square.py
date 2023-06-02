#!/usr/bin/python3
"""Python model for Square, almost a circle task"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the __str__"""
        return('[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns and updated attributes"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
        }
