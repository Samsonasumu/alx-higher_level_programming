#!/usr/bin/python3
"""
 MyList that inherits from list
"""


class MyList(list):
    """"subclas"""
    def __init__(self):
        """"initializes the object"""
        super().__init__()

    def print_sorted(self):
        """"print sorted"""
        print(sorted(self))
