#!/usr/bin/python3
"""..."""
import urllib.request
from sys import argv

if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
