#!/usr/bin/python3
"""Python module for task no 2"""


def write_file(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)"""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
