#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        word = sentence[0]
        new_tuple = [length, word]
        return(new_tuple)
    else:
        return(length, None)
