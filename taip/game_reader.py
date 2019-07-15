import json
from taip.game_objects import Item, Room, Map

with open("gamefile.json", "r") as gameFile:
    data = json.load(gameFile)
    print(data["start"])
    print(data["map"]["main room"])



 