#!/usr/bin/python3

"""
Module that contains a function that reads from a text file (UTF8)
"""


def read_file(filename=""):
    """Reads from filename and prints its contents to stdout.

    Args:
        filename: name of the file

    """

    with open(filename, encoding="utf-8", mode="r") as f:
        read_text = f.read()
        print(read_text, end="")
