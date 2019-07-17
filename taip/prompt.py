def prompt():
    while True:
        command = input(">>> ")
        parse(command)

def parse(command):
    if command == "go east" or command == "e":
        print(">")
    elif command == "go west" or command == "w":
        print("<")
    elif command == "go north" or command == "n":
        print("^")
    elif command == "go south" or command == "s":
        print("v")
    elif command.startswith("pick up"):
        item = command.lstrip("pick up ")
        print(item)
    else:
        print("invalid command")