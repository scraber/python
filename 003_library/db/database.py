from book import Book, Author, Category
from user import User
import logging
import json
import copy


class Database:

    def __init__(self, db_filename: str = "database.json"):
        logging.basicConfig(level=logging.DEBUG)

        self.users = list()
        self.books = list()
        self.db = {"users": self.users, "books": self.books}

        with open(db_filename, 'a+') as json_db:
            try:
                self.db = json.load(json_db)
            except ValueError:
                logging.error("Cannot parse %s", db_filename)

    def add_user(self, new_user: User):
        self.users.append(new_user)
        logging.debug("User %s added to database", new_user)

    def add_book(self, new_book: Book):
        self.books.append(new_book)
        logging.debug("Book %s added to database", new_book.title)

    def save_db(self, db_filename: str = "database.json"):
        # new_db = dict()
        # new_db = self.db["books"][-1].to_json()
        # print(new_db)
        with open(db_filename, 'w') as json_db:
            json.dump(self.db, json_db, indent=4)


db = Database()
db.add_user(User("Marek", "Kowalski"))
db.add_user(User("Maciej", "Rek"))
test_book = (Book("dupa", Category("Fantasy", 1), 546, Author("jan", "dupa")))
db.add_book(test_book)

db.save_db()
