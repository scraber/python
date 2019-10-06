from book_database import Book, BookDatabase
from user_database import User, UserDatabase
import json
import logging


class Rentals:
    def __init__(self, user_db: UserDatabase, book_db: BookDatabase, db_filename: str = "rentals_history.json"):
        logging.basicConfig(level=logging.DEBUG)

        self.rentals = {"users": {str(user_db.db[idx].uid): list() for idx in user_db.db},
                        "books": {str(book_db.db[idx].uid): list() for idx in book_db.db}}

        try:
            with open(db_filename) as json_db:
                self.rentals = json.load(json_db)

        except ValueError:
            logging.error("Cannot parse %s", db_filename)
        except FileNotFoundError:
            logging.warning("Couldn't find %s", db_filename)

    def rent_book(self, user: User, book: Book):
        self.rentals.get("users").get(str(user.uid)).append(book.uid)
        self.rentals.get("books").get(str(book.uid)).append(user.uid)
        book.currently_owning = {user.uid: user.__str__()}
        book.available = False

    def return_book(self, book: Book):
        book.currently_owning = None
        book.available = True

    def save_db(self, db_filename: str = "rentals_history.json"):
        with open(db_filename, 'w') as json_db:
            json.dump(self.rentals, json_db, indent=4)

