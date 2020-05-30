import sys
import unittest
import calc

# import requests
# import regex
print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


print(greet("Blue"))
print(greet("World"))
