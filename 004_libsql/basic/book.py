from basic.author import Author
import itertools


class Book:
    __id_iter = itertools.count()

    def __init__(self, uid: int, title: str, category: str, isbn: int, author: Author, available: bool = True):
        self.uid = uid
        self.title = title
        self.category = category
        self.isbn = isbn
        self.author = author
        self.available = available
        self.currently_owning = None

    def __str__(self):
        return f"{self.uid}: {self.title} by Author: {self.author.__str__()}, Category: {self.category}, ISBN: {self.isbn}, Available: {self.available}"

    def __eq__(self, other):
        return self.title == other.title and self.isbn == other.isbn and self.author == other.author

    def get_name(self):
        return f"{self.title}"

    def to_json(self):
        return {"title": self.title, "isbn": self.isbn, "category": self.category,
                "author": vars(self.author), "available": self.available}
