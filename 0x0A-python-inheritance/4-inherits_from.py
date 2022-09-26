#!/usr/bin/python3
"""
 returns True if the object is an instance of,
 or if the object is an instance
 of a class that inherited from, t
 he specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Return true or false if is instance"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
