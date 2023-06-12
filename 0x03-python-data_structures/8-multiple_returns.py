#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        x, y = 0, None
    else:
        x, y = len(sentence), sentence[0]
    return (x, y)
