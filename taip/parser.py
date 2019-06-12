def parse(command):
    if command == "go east":
        print(">")
    elif command == "go west":
        print("<")
    elif command == "go north":
        print("^")
    elif command == "go south":
        print("v")
    else:
        print("invalid command")