#!/usr/bin/python3
"""
Class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init a square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """string rep of a square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """square size"""
        return self.width

    @size.setter
    def size(self, value):
        """quare size getter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign attrs from args an kwargs"""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dic representation of a square"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["x"] = self.x
        dictionary["size"] = self.size
        dictionary["y"] = self.y
        return dictionary
