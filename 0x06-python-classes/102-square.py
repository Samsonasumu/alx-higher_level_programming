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
        self.size = size

    def area(self):
        """calculates square's area

        Returns: None
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size

        Returns:
            The square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the square's size

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, square2):
        """Compare if square is less than another by area
        Args:
            square2 (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < square2.size

    def __le__(self, square2):
        """Compare if square is less than another or equal by area
        Args:
            square2 (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= square2.size

    def __eq__(self, square2):
        """Compare if square is equal to another by area
        Args:
            square2 (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == square2.size

    def __ne__(self, square2):
        """Compare if square is diferent to another by area
        Args:
            square2 (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != square2.size

    def __gt__(self, square2):
        """Compare if square is greater to another or by area
        Args:
            square2 (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > square2.size

    def __ge__(self, square2):
        """Compare if square is greater to another or equal by area
        Args:
            square2 (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= square2.size
