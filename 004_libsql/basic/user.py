import itertools


class User:
    __id_iter = itertools.count()

    def __init__(self, uid: int, firstname: str, lastname: str):
        self.uid = uid
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self, view: str = "user"):
        if "user" == view:
            return f"{self.uid}: {self.firstname} {self.lastname}"
        elif "admin" == view:
            return f"{self.uid}: {self.firstname} {self.lastname}"

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname

    def get_name(self):
        return f"{self.firstname} {self.lastname}"

    def to_json(self):
        return {"firstname": self.firstname, "lastname": self.lastname}
