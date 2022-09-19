#!/usr/bin/python3
"""
Defines a Rectangle class based on 6-rectangle.py.
"""


class Rectangle:
    """Represents a rectangle with width and heigh.

    Attributes:
        number_of_instances: number of Rectangle instances
            increments with every instantiation
            decrements with every deletion
        print_symbol: symbol for string representation

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character.
        """

        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        return rectangle[:-1]

    def __repr__(self):
        """
        Returns a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance

        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance

        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
