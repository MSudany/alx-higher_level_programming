#!/usr/bin/python3
"""..."""
from sys import argv
import requests


if __name__ == '__main__':
    response = requests.get(argv[1])
    status_code = response.status_code
    if status_code > 400:
        print('Error code: {}'.format(status_code))
    else:
        print('{}'.format(response.text))
