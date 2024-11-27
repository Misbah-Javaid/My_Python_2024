#! /usr/bin/env python
import sys
from os import rename
import math
import requests

print(sys.version)
print(sys.executable)
print("This is not working and I am tring hard")


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greet


r = requests.get('https://coreyms.com')
print(r.status_code)
print("This is not working and I am tring hard")
print("This is a cat and that is a ball")
