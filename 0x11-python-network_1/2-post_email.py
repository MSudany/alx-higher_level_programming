#!/usr/bin/python3
"""..."""
from urllib import request, parse
from sys import argv


if len(argv) > 2:
    email = {'email': argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))
