#!/usr/bin/python3
"""Python module for task 2"""


def write_file(filename="", text=""):
    """
    function that writes a string at end of text file (UTF8
    and returns the number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
        
