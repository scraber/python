def length():
    try:
        len = int(input("Password length: "))
    except ValueError:
        print("Expecting numbers!")
        return length()
    else:
        return len


def chars():
    return tuple(input("Available password characters: "))


def attempts():
    try:
        att = int(input("Attempts: "))
    except ValueError:
        print("Expecting numbers!")
        return attempts()
    else:
        return att
