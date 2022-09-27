#!/usr/bin/python3

"""Module that writes an Object to a text file using
a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes the representaion of my_obj
    to filename.

    Args:
        my_obj: object to write
        filename: file to write into
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
