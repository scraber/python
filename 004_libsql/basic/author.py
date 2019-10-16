class Author:

    def __init__(self, uid: int, firstname: str, lastname: str):
        self.uid = uid
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname + " " + self.lastname

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname

    def __str__(self):
        return f"{self.uid}: {self.fullname}"
