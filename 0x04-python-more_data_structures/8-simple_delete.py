#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in a_dictionary:
        if key in i:
            del a_dictionary[key]
        return a_dictionary
