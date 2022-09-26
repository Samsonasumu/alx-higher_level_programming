#!/usr/bin/python3
"""
 returns True if the object is an instance of,
 or if the object is an instance
 of a class that inherited from, t
 he specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Return true or false if is instance"""
    return isinstance(obj, a_class)
