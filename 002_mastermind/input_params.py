def length():
    try:
        len = int(input("Password length: "))
    except ValueError:
        print("Expecting numbers!")
        return length()
    else:
        return len


def chars():
    char = tuple(input("Available password characters: "))
    if 0 != len(char):
        return char
    else:
        print("No characters passed!")
        return chars()


def attempts():
    try:
        att = int(input("Attempts: "))
    except ValueError:
        print("Expecting numbers!")
        return attempts()
    else:
        return att
