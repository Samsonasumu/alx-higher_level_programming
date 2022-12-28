#!/usr/bin/python3
"""script that takes in a URL and
an email address, send post"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
