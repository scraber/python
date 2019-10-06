import itertools


class Category:
    id_iter = itertools.count()

    def __init__(self, category: str):
        self.id = next(self.id_iter)
        self.category = category

    def __str__(self):
        return f"{self.category}"

    def to_json(self):
        return {self.id: self.category}