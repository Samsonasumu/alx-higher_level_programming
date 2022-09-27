#!/usr/bin/python3

"""Module that defines the class Student(based on 10-student.py)
"""


class Student:
    """class Student tha defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation
        of a Student instance

        Args:
            attrs: list of attributes

        Returns:
            the dict representation of the instance.

        """

        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for i in range(len(attrs)):
                for x in obj:
                    if attrs[i] == x:
                        d_list[x] = obj[x]
            return d_list

        return obj

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json: dictionary of attributes
        """
        for key, value in json.items():
            self.__dict__[key] = value
