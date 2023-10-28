#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    if x == 0:
        sentence = (None)
    return x, sentence[0]
