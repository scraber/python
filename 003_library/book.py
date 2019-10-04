from category import Category
from author import Author


class Book:
    def __init__(self, uid: int, title: str, category: Category, isbn: int, author: Author):
        self.uid = uid
        self.title = title
        self.category = category
        self.isbn = isbn
        self.author = author
        altor = self.author.__str__()

    def __str__(self):
        return f"{self.uid}: {self.title} by Author: {self.author.__str__()}, Genre: {self.category.__str__()}, ISBN: {self.isbn}"

    def to_json(self):
        return {"title": self.title, "isbn": self.isbn, "genre": vars(self.category),
                "author": vars(self.author)}
