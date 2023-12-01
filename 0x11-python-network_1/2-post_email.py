#!/usr/bin/python3
"""
Takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
    print(html.decode())
