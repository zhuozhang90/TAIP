import math
from taip import parser

def prompt():
    while True:
        command = input(">>> ")
        parser.parse(command)
