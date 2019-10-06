class Author:

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def __eq__(self, other):
        if self.firstname == other.firstname and self.lastname == other.lastname:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
