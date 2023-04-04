#!/usr/bin/python3
"""
Module that displays the value of the X-Request-Id variable.
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
