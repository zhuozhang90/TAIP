import math
from taip import commandparser
def prompt():
    while True:
        command = input(">>> ")
        commandparser.parse(command)