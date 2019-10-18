from basic.author import Author
from basic.category import Category
import itertools


class Book:
    __id_iter = itertools.count()

    def __init__(self, uid: int, title: str, category: Category, isbn: int, author: Author):
        self.uid = uid
        self.title = title
        self.category = category
        self.isbn = isbn
        self.author = author

    def __str__(self):
        return f"{self.title} by Author: {self.author}, ISBN: {self.isbn}"

    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn and self.author == other.author

    def get_name(self):
        return f"{self.title}"

    def to_json(self):
        return {"title": self.title, "isbn": self.isbn, "category": self.category,
                "author": vars(self.author)}
