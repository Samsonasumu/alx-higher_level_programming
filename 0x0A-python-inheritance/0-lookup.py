#!/usr/bin/python3
"""
returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Returns all methods of and obj"""
    ret = dir(obj)
    return ret
