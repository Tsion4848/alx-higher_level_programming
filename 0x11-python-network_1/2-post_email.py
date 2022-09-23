#!/usr/bin/python3
"""
takes in url and email and sends a POST request to the url via
an email parameter
"""
import urllib.request
from sys import argv



if __name__ == "__main__":
    """
    takes in url and email and sends a POST request to the url via
    an email parameter
    """
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urlib.request.urlopen(req) as response:
        html = response.read()
        html_dec = html.decode('utf-8')
    print(html_dec)
