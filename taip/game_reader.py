import json
from taip.game_objects import Item, Room, Game

with open("gamefile.json", "r") as game_file:
    data = json.load(game_file)
    print(data)
    print(data["map"]["main room"])



 