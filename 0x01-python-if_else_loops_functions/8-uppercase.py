#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        uppercase = str[i]
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            uppercase = chr(ord(str[i]) - 32)
        print("{}".format(uppercase), end='')
    print()
