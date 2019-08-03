from taip.game_objects import Player, Room, Item

# infinite loop to keep waiting for commands
def prompt():
    while True:
        command = input(">>> ")
        try:
            parse(command)
            check_goal()
        except :
            print("Something went wrong.")

# takes user input and manipulates the game objects
def parse(command):
    player.add_comm(command)
    if command == "p":
        print(player.commands)
    # control directions. 
    # Each time going into a new room the env is reset and look() is called to display desc
    if command == "go east" or command == "e":
        print(">")
        if player.pos.e != None:
            player.e()
            player.reset_env()
            print(player.pos.name)
            look()
        else:
            print("You can't go that way.")
    elif command == "go west" or command == "w":
        print("<")
        if player.pos.w != None:
            player.w()
            player.reset_env()
            print(player.pos.name)
            look()
        else:
            print("You can't go that way.")    
    elif command == "go north" or command == "n":
        print("^")
        if player.pos.n != None:
            player.n()
            player.reset_env()
            print(player.pos.name)
            look()
        else:
            print("You can't go that way.")
    elif command == "go south" or command == "s":
        print("v")
        if player.pos.s != None:
            player.s()
            player.reset_env()
            print(player.pos.name)
            look()
        else:
            print("You can't go that way.")
    # prints the desc of the room
    elif command == "look" or command == "l":
        look()
    # examine specific objects
    elif command.startswith("examine "):
        item = command[8:]
        item = item.strip().lower()
        env = player.env + player.pos.contains
        for a in env:
            if a.name == item:
                print(a.desc)
    elif command.startswith('x'):
        item = command[2:]
        item = item.strip().lower()
        env = player.env + player.pos.contains
        for a in env:
            if a.name == item:
                print(a.desc)
                player.add_env(a)
    # adds item to inventory
    elif command.startswith("pick up "):
        item = command[8:]
        item = item.strip().lower()
        env = player.env + player.pos.contains
        for a in env:
            if a.name == item:
                player.pickup(a)
                print("you picked up " + a.name)
    elif command.startswith("p"):
        item = command[2:]
        item = item.strip().lower()
        env = player.env + player.pos.contains
        for a in env:
            if a.name == item:
                player.pickup(a)
                print("you picked up " + a.name)
    # displays items in inventory
    elif command == "inventory" or command == "i":
        for i in player.inventory:
            print(i.name)
    else:
        print("invalid command")

# print desc of room 
def look():
    room = player.pos
    print(room.desc)

# print desc of certain item
def examine(item):
    if item is Item:
        print(item.desc)

# checks if goal is met, meaning all three objects are in inventory
# then writes the history of commands into a file if won
def check_goal():
    if eyeball_1 in player.inventory and eyeball_2 in player.inventory \
        and eyeball_3 in player.inventory:
        print("you've collected all eyeballs! \nYOU WON!!!")
        with open('history.txt', 'a') as hist_file:
            hist_file.write(player.commands)
        hist_file.close()

# game setup

# set up rooms with names and desc

main_room = Room("main room", "You are at the entrance of a room that looks like someone's living room. There is a coffee table with a small box at the center of the room, there's also a chair in the corner. There's also some trash just laying around. This room is very dusty. It looks like there's a door leading to the west and the south.", )

small_room = Room("small room", "You are in the small room. It's so tiny that there's only space for one person to turn around. Not much going on here. Seems more like space between rooms instead of a room. There's a door to the north and the east.")

red_room = Room("red room", "You are in a red room. The walls are violently red it's almost agitating. There are pillows laying around randomly. Feels like this used to be a bedroom but now the bed is gone. You can also see a sack leaning against the wall to your right. The door leads to the east.")

blue_room = Room("blue room", "You are in a blue room. It's very cozy and feels less disturbing than the other rooms. There's a chest under a table that seems pretty old. On the desk stands a bottle that says 'Empty'. You see the door you came through to the west.")

# set up neighbors of rooms
# each neighbor is connected with a pointer to that object
main_room.s = small_room
main_room.w = red_room

small_room.n = main_room
small_room.e = blue_room

red_room.e = main_room

blue_room.w = small_room

# 3 objects to collect
eyeball_1 = Item("eyeball", "Just a fresh, slimy eyeball.")
eyeball_2 = Item("eyeball", "Just an eyeball, dry and pruned.")
eyeball_3 = Item("eyeball", "It's made of gold. Still looks gross though.")

# children of rooms
small_box = Item("small box", "This is a very strange looking box and it seems to be easy to open. You opened it and there was an eyeball.")
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

# print intro and help to start game
print("You must have slept for days. You woke up and found yourself in a strange place. The wall in front of you says 'collect 3 eyeballs and you can leave'. You think it must be a prank but you decided to play along.")
print("\nHelp: use s,n,w,e to move, l to look around the room and x to examine, p to pick up, i to check inventory. Use ctrl+c to exit.\n")

# initialize player to start 
player = Player()
player.pos = main_room
look()










