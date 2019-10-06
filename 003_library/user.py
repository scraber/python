import itertools


class User:
    __id_iter = itertools.count()

    def __init__(self, firstname: str, lastname: str):
        self.uid = next(self.__id_iter)
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self, view: str = "user"):
        if "user" == view:
            return f"{self.firstname} {self.lastname}"
        elif "admin" == view:
            return f"{self.uid}: {self.firstname} {self.lastname}"

    def __eq__(self, other):
        if self.firstname == other.firstname and self.lastname == other.lastname:
            return True
        else:
            return False

    def get_name(self):
        return f"{self.firstname} {self.lastname}"

    def to_json(self):
        return {"firstname": self.firstname, "lastname": self.lastname}
