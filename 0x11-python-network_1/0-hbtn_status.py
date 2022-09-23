#!/usr/bin/python3
"""a python script that fetches a url"""
import urllib.request

if __name__ == "__main__":
    """fetches a url"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    html_dec = html.decode('utf-8')
