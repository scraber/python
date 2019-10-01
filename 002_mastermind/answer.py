def correct_char_correct_pos(char, index, passphrase: tuple):
    if char == passphrase[index]:
        return True
    else:
        return False


def correct_char_wrong_pos(char, passphrase: tuple):
    if char in passphrase:
        return True
    else:
        return False


def wrong_char(char, passphrase: tuple):
    if char not in passphrase:
        return True
    else:
        return False
