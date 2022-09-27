#!/usr/bin/python3

"""
read file function
"""


def read_file(filename=""):
    """Reads from filename and prints its contents to stdout.

    Args:
        filename: name of the file

    """

    with open(filename, "r", encoding=("utf-8")) as text:
        lines = text.read()
    print(lines, end="")
