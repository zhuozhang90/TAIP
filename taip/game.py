from taip.game_objects import Player, Room, Item

def prompt():
    while True:
        command = input(">>> ")
        parse(command)

def parse(command):
    if command == "go east" or command == "e":
        print(">")
        if player.pos.e != None:
            player.e()
            print(player.pos.name)
            look()
        else:
            print("Nothing there.")
    elif command == "go west" or command == "w":
        print("<")
        if player.pos.w != None:
            player.w()
            print(player.pos.name)
            look()
        else:
            print("Nothing there.")    
    elif command == "go north" or command == "n":
        print("^")
        if player.pos.n != None:
            player.n()
            print(player.pos.name)
            look()
        else:
            print("Nothing there.")
    elif command == "go south" or command == "s":
        print("v")
        if player.pos.s != None:
            player.s()
            print(player.pos.name)
            look()
        else:
            print("Nothing there.")
    elif command == "look" or command == "l":
        look()
    elif command.startswith("examine "):
        item = command[8:]
        item = item.strip().lower()
        for a in player.pos.contains:
            if a.name == item:
                print(a.desc)
    elif command.startswith('x'):
        item = command[2:]
        item = item.strip().lower()
        for a in player.pos.contains:
            if a.name == item:
                print(a.desc)
                player.add_env(a)
    elif command.startswith("pick up "):
        item = command[8:]
        item = item.strip().lower()
        print(item)
    else:
        print("invalid command")

def look():
    room = player.pos
    print(room.desc)

def examine(item):
    if item is Item:
        print(item.desc)

# game setup



main_room = Room("main room", "You are at the entrance of a room that looks like someone's living room. There is a coffee table with a small box at the center of the room, there's also a chair in the corner. There's also some trash just laying around. This room is very dusty. It looks like there's a door leading to the west and the south.", )

small_room = Room("small room", "You are in the small room. It's so tiny that there's only space for one person to turn around. Not much going on here. Seems more like space between rooms instead of a room. There's a door to the north and the east.")

red_room = Room("red room", "You are in a red room. The walls are violently red it's almost agitating. There are pillows laying around randomly. Feels like this used to be a bedroom but now the bed is gone. You can also see a sack leaning against the wall to your right.")

blue_room = Room("blue room", "You are in a blue room. It's very cozy and feels less disturbing than the other rooms. There's a chest under a table that seems pretty old. On the desk stands a bottle that says 'Empty'.")

main_room.s = small_room
main_room.w = red_room

small_room.n = main_room
small_room.e = blue_room

red_room.e = main_room

blue_room.w = small_room

eyeball_1 = Item("eyeball", "Just a fresh, slimy eyeball.")
eyeball_2 = Item("eyeball", "Just an eyeball, dry and pruned.")
eyeball_3 = Item("eyeball", "It's made of gold. Still looks gross though.")

small_box = Item("small box", "This is a very strange looking box and it seems to be easy to open.")
small_box.contain(eyeball_1)
chair = Item("chair",  "Just a wooden chair. Nothing fancy.")
main_room.contain(small_box)
main_room.contain(chair)

pillows = Item("pillows", "Looks like someone had a pillow fight here. You see an eyeball.")
pillows.contain(eyeball_2)
sack = Item("sack", "Looks new and full. You opened it and saw a knife.")
knife = Item("knife", "Made of wood.")
sack.contain(knife)
red_room.contain(pillows)
red_room.contain(sack)

chest = Item("chest", "It's a very old treasure chest. You are probably in luck. You opened it and there's another eyeball.")
chest.contain(eyeball_3)
bottle = Item("bottle", "Very nice and rustic-looking glass bottle. Looks like there's a dead mouse inside.")
dead_mouse = Item("dead mouse", "It's more like a mummified little mouse.")
bottle.contain(dead_mouse)
blue_room.contain(chest)
blue_room.contain(bottle)


player = Player()
print("You must have slept for days. You woke up and found yourself in a strange place. The wall in front of you says 'collect 3 eyeballs and you can leave'. You think it must be a prank but you decided to play along.")
print("help: use snwe to move, l to look around and x to examine. pick up to pick up.")

player.pos = main_room
# look()
# examine(main_room)
# print(player.pos.name)
# player.pickup(eyeball_1)
# for i in player.inventory:
#     print(i.name)
# player.s()
# print(player.pos.name)
# examine(player.pos)
# player.e()
# print(player.pos.name)










