from abstract_database import AbstractDatabase
from book import Book, Author, Category
import json


class BookDatabase(AbstractDatabase):

    def load_from_file(self):
        with open(self.db_filename) as json_db:
            data = json.load(json_db)
        for uid in data:
            self.data[int(uid)] = Book(data[uid]["title"], data[uid]["category"], data[uid]["isbn"],
                                       Author(data[uid]["author"]["firstname"], data[uid]["author"]["lastname"]),
                                       data[uid]["available"])

    def list_by_category(self, category):
        book_list = list()

        for uid in self.data:
            book = self.data.get(uid)
            if category == book.category:
                book_list.append(book.__str__())

        return book_list

    def get_book_list(self):
        book_list = list()

        for uid in self.data:
            single_book = self.data.get(uid)
            tostrbook = single_book.__str__()
            book_list.append(tostrbook)

        return book_list

# u = BookDatabase("book_database.json")
# u.add(Book("The Three Musketeers", "Thriller", 54734534756, Author("Alexandre", "Dumas")))
# u.add(Book("Life of Pi", "Drama", 235264563563, Author("Yann", "Martel")))
# u.add(Book("V for Vendetta", "Thriller", 849837498, Author("Alan", "Moore")))
# u.save_db()
