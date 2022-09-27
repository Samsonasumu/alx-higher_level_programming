#!/usr/bin/python3

"""Module that defines the class Stident
"""


class Student:
    """class Student tha defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation
        of a Student instance

        Returns:
            the dict representation of the instance.

        """

        return self.__dict__
