#!/usr/bin/python3
"""defining a square"""


class Square:
    """ represents a square

    Attributes:
        ___size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
