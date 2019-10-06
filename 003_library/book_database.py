from book import Book, Author, Category
import logging
import json


class BookDatabase:

    def __init__(self, db_filename: str = "book_database.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.books = dict()

        try:
            with open(db_filename) as json_db:
                data = json.load(json_db)
            for uid in data:
                test = data[uid]["category"]
                self.books[int(uid)] = Book(data[uid]["title"], data[uid]["category"], data[uid]["isbn"],
                                            Author(data[uid]["author"]["firstname"], data[uid]["author"]["lastname"]),
                                            data[uid]["available"])
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

    def list_by_category(self, category):
        book_list = list()

        for uid in self.books:
            book = self.books.get(uid)
            if category == book.category:
                book_list.append(book.__str__())

        return book_list

    def get_book_list(self):

        book_list = list()

        for uid in self.books:
            single_book = self.books.get(uid)
            tostrbook = single_book.__str__()
            book_list.append(tostrbook)

        return book_list


# u = BookDatabase()
# u.add_book(Book("The Three Musketeers", "Thriller", 54734534756, Author("Alexandre", "Dumas")))
# u.add_book(Book("Life of Pi", "Drama", 235264563563, Author("Yann", "Martel")))
# u.add_book(Book("V for Vendetta", "Thriller", 849837498, Author("Alan", "Moore")))
# u.save_db()
