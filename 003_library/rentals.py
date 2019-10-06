from book_database import BookDatabase, Book
from user_database import UserDatabase, User


class Rentals:
    def __init__(self, book_db: BookDatabase, user_db: UserDatabase):
        self.book_db = book_db
        self.user_db = user_db

    def rent_book(self, user: User, book: Book):
        book.available = False

    def return_book(self, user: User, book: Book):
        book.available = True
