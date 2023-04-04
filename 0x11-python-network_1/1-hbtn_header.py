#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import sys
import urllib.request
with urllib.request.urlopen(sys.argv[1]) as response:
    request_id = response.getheader('X-Request-Id')
    print(request_id)
