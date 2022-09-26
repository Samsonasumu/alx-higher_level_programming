#!/usr/bin/python3
"""
class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """validates values"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of w and h"""
        return self.__width * self.__height

    def __str__(self):
        """return a descrpition"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
