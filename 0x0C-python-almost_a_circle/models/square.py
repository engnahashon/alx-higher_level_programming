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
