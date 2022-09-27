#!/usr/bin/python3

"""Module that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Function that returns the dictionary description of an obj
    """

    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
