#!/usr/bin/python3
"""
takes a url, sends a request to it and displays X-Request-Id
variable found in the header of the response
"""
import urllib.request
from sys import argv



if __name__ == "__main__":
    """takes a url, sends a request to it and displays X-Request-Id
    variable found in the header of the response"""
    with urllib.request.urlopen(argv[1]) as response:
        hid = response.info().get('X-Request-Id')
        print(hid)
