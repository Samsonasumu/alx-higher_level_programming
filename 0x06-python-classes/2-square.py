#!/usr/bin/python3
"""defining a square"""


class Square:
    """ represents a square

    Attributes:
        ___size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
