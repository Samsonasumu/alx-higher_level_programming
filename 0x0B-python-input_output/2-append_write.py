#!/usr/bin/python3

"""
Module to append a string at the end of a text file(UTF8)
"""


def append_write(filename="", text=""):
    """Appends text to a filename

    Args:
        filename: name of the file
        text: text to append
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
