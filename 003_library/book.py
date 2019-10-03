from category import Category
from author import Author
from category_manager import Manager
import json


class Book:
    def __init__(self, title: str, category: Category, isbn: int, author: Author):
        self.title = title
        self.category = category
        self.isbn = isbn
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, ISBN: {self.isbn}, Author: {self.author}"

    def to_json(self):
        return {"title": self.title, "isbn": self.isbn, "category": vars(self.category),
                "author": vars(self.author)}
