from category import Category
from author import Author
from category_manager import Manager


class Book:
    def __init__(self, title: str, book_category: str, isbn: str, author: Author):
        self.title = title
        self.isbn = isbn
        self.category = book_category
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, ISBN: {self.isbn}, Author: {self.author.firstname} {self.author.lastname}"


