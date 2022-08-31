#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for key in a_dictionary:
        keys.append(key)
    keys.sort()
    new_dict = {}
    for i in keys:
        new_dict[i] = a_dictionary[i]
    for m, n in new_dict.items():
        print(f"{m}: {n}")
