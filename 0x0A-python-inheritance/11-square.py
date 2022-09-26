#!/usr/bin/python3
"""
class BaseGeometry
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """represents a square"""
    def __init__(self, size):
        """validates values"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return square area"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
