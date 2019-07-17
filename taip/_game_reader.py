import json
from taip.game_objects import Player, Room, Game

with open("gamefile.json", "r") as game_file:
    data = json.load(game_file)
    game_map = data['map']
    rooms = data['rooms']

print(game_map.keys())

for room, neighbors in game_map.items():
    print(room)
    if neighbors["north"] != None:
        print(neighbors["north"])
    if neighbors["south"] != None:
        print(neighbors["south"])
    if neighbors["east"] != None:
        print(neighbors["east"])
    if neighbors["west"] != None:
        print(neighbors["west"])



















    # game = Game(start=data["start"])
    # print(list(data["map"].keys()))

    # entrance = Room(list(data["map"].keys())[0])
    # print(map[entrance.name])
    

    # for name, room in data["rooms"].items():
    #     print(name)
    #     for prop, val in room.items():
    #         if prop == "children":
    #             # print(val)
    #             # print(type(val))
    #             if val is None:
    #                 print("Empty")
    #             else:
    #                 # print(val)
    #                 for item, contains in val.items():
    #                     print(item, contains["contains"])

                   


 