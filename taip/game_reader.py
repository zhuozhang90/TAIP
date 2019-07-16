import json
from taip.game_objects import Player , Room, Game

with open("gamefile.json", "r") as game_file:
    data = json.load(game_file)
    game = Game(start=data["start"])
    print(data["rooms"])
    for room, neighbors in data["map"].items():
        print(room)
    for name, room in data["rooms"].items():
        print(name)
        for prop, val in room.items():
            if prop == "children":
                # print(val)
                # print(type(val))
                if val is None:
                    print("Empty")
                else:
                    # print(val)
                    for item, contains in val.items():
                        print(item, contains["contains"])

                   


 