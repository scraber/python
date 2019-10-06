import itertools


class Category:
    __id_iter = itertools.count()

    def __init__(self, category: str):
        self.uid = next(self.__id_iter)
        self.category = category

    def __eq__(self, other):
        if self.category == other.category:
            return True
        else:
            return False

    def get_name(self):
        return f"{self.category}"

    def to_json(self):
        return f"{self.category}"
