def print_red(text):
    """Prints text in red"""
    print("\033[91m {}\033[00m".format(text), end='')


def print_green(text):
    """Prints text in green"""
    print("\033[96m {}\033[00m".format(text), end='')


def print_yellow(text):
    """Prints text in yellow"""
    print("\033[93m {}\033[00m".format(text), end='')
