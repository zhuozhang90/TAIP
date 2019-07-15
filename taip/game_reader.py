import json
from taip.game_objects import Item, Room, Game

with open("gamefile.json", "r") as game_file:
    data = json.load(game_file)
    # print(data)
    for i, j in data["rooms"]["main room"].items():
        print(i, j)



 