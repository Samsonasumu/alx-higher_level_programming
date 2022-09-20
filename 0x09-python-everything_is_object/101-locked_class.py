#!/usr/bin/python3
"""locket class"""


class LockedClass:
    """ locket class that just only allows dynamically create
    the instance attribute "first_name"""
    __slots__ = ["first_name"]
