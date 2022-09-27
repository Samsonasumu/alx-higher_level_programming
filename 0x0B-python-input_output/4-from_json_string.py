#!/usr/bin/python3

"""Module that returns an object (python data structure)
represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """Function that returns the object represented by my_str.

    Args:
        my_str: JSON string representation

    Returns:
        corresponding object
    """

    return json.loads(my_str)
