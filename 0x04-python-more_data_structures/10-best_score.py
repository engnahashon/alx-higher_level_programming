#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = ''
    high = 0
    for key, value in a_dictionary.items():
        if value > high:
            high = value
            best = key
    return best
