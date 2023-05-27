#!/usr/bin/python3
"""Python module for task 2"""


def write_file(filename="", text=""):
    """writes a string at end of text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
        
