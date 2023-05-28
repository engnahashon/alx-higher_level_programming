#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    function that appends a string at the end of a text file
    returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
