#!/usr/bin/python3
for comb in range(0, 10):
    for comb1 in range(comb + 1, 10):
        if comb == 8 and comb1 == 9:
            print("{}{}".format(comb, comb1))
        else:
            print("{}{}".format(comb, comb1), end=', ')
