#!/usr/bin/python3
"""
Myint class
"""


class MyInt(int):
    """"""
    def __eq__(self, other):
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return True
