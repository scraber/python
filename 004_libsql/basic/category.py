import itertools


class Category:
    __id_iter = itertools.count()

    def __init__(self, uid: int, name: str):
        self.uid = uid
        self.name = name

    def __str__(self):
        return f"{self.uid}: {self.name}"

    def __eq__(self, other):
        return self.name == other.name
