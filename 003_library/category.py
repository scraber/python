class Category:

    def __init__(self, category: str, id: int):
        self.category = category
        self.id = id

    def __str__(self):
        return f"{self.category}"

    def to_json(self):
        return {self.category, self.id}
