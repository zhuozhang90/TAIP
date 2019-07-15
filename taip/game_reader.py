import json
from taip.game_objects import Item, Room, Game

with open("gamefile.json", "r") as game_file:
    data = json.load(game_file)
    for room, neighbors in data["map"].items():
        print(room)
        for _, neighbors in neighbors.items():
            for direction, room in neighbors.items():
                print(direction, room)
    for name, room in data["rooms"].items():
        print(name)
        for prop, val in room.items():
            print(prop)
            if prop == "children":
                for i, j in val.items():
                    print(i, j)
            else:
                print(val)



 