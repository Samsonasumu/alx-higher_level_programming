#!/usr/bin/python3

"""
Module containing a function that writes a string to a text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename: name of the file

    Returns:
        number of characters written

    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
