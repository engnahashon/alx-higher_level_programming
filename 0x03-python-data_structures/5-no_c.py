#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for idx in my_string:
        if idx != 'C' and idx != 'c':
            new_string = new_string + idx
    return (new_string)
