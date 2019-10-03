from book import Book, Author, Category
import logging
import json


class BookDatabase:

    def __init__(self, db_filename: str = "book_database.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.books = dict()

        with open(db_filename) as json_db:
            try:
                data = json.load(json_db)
                for uid in data:
                    self.books[int(uid)] = Book(uid, data[uid]["title"], data[uid]["genre"], data[uid]["isbn"],
                                                data[uid]["author"])
            except ValueError:
                logging.error("Cannot parse %s", db_filename)
            except FileNotFoundError:
                logging.warning("Couldn't find %s", db_filename)

    def add_book(self, new_book: Book):
        if new_book not in self.books:
            self.books[int(new_book.uid)] = new_book
            logging.debug("Book %s added to database", new_book.title)
        else:
            logging.warning("Book %s already exists!", new_book.title)

    def remove_book(self, remove_book: Book):
        if remove_book in self.books:
            del self.books[int(remove_book.uid)]
            logging.debug("Book %s removed from database", remove_book.title)
        else:
            logging.warning("Book %s doesn't exists!", remove_book.title)

    def save_db(self, db_filename: str = "book_database.json"):
        update_db = dict()
        for uid in self.books:
            update_db[uid] = self.books.get(uid).to_json()
        with open(db_filename, 'w') as json_db:
            json.dump(update_db, json_db, indent=4)


test = BookDatabase()
test.add_book(Book(1, "dupa", Category("Fantasy", 1), 546, Author("jan", "dupa")))
test.add_book(Book(2, "elo", Category("romance", 1), 546, Author("jan", "dupa")))
test.save_db()
