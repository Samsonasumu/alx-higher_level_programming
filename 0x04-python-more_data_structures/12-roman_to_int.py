#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                "D": 500, "M": 1000}

    i = 0
    integer = 0

    if not roman_string or type(roman_string) != str:
        return 0

    while (i < len(roman_string)):
        val_char1 = dict_rom[roman_string[i]]
        if (i + 1) < len(roman_string):
            # do something
            val_char2 = dict_rom[roman_string[i + 1]]
            if val_char1 >= val_char2:
                integer = integer + val_char1
                i += 1
            else:
                integer = integer + val_char2 - val_char1
                i += 2
        else:
            integer = integer + val_char1
            i += 1

    return integer
