#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        return (None)
    else:
        return(l, sentence[0])
