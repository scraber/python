from Database import Database
from basic.book import Book
from containers.borrow_history import BorrowHistory
from containers.category_database import CategoryDatabase
from containers.book_database import BookDatabase
from containers.author_database import AuthorDatabase
from containers.user_database import UserDatabase


class LibraryManager:
    def __init__(self, host: str, user: str, database_name: str = "library_db"):
        self.libDB = Database(host, user, database_name)
        self.libDB.connect()
        self.libDB.prepare_database()
        self.bookDB = BookDatabase(self.libDB)
        self.authorDB = AuthorDatabase(self.libDB)
        self.userDB = UserDatabase(self.libDB)
        self.categoryDB = CategoryDatabase(self.libDB)
        self.historyDB = BorrowHistory(self.libDB)

    def get_all_books(self):
        book_list = list()
        for response in self.bookDB.get_all():
            uid, title, id_category, isbn, id_author = response
            category = self.categoryDB.get_category_by_id(id_category)
            author = self.authorDB.get_author_by_id(id_author)
            book_list.append(Book(uid, title, category, isbn, author))
        return book_list

    def get_all_books_by_category(self, id_category):
        book_list = list()
        for response in self.bookDB.get_by_category(id_category):
            uid, title, id_category, isbn, id_author = response
            category = self.categoryDB.get_category_by_id(id_category)
            author = self.authorDB.get_author_by_id(id_author)
            book_list.append(Book(uid, title, category, isbn, author))
        return book_list

    def get_available_books(self):
        book_list = list()
        for response in self.bookDB.get_all_available():
            uid, title, id_category, isbn, id_author = response
            category = self.categoryDB.get_category_by_id(id_category)
            author = self.authorDB.get_author_by_id(id_author)
            book_list.append(Book(uid, title, category, isbn, author))
        return book_list


    def get_whole_book_history(self):
        history_list = list()
        for response in self.historyDB.get_all():
            _, id_user, id_book, borrow_date, returned = response
            _, firstname, lastname, _ = self.userDB.get_user_by_id(id_user)
            _, title, _, isbn, _ = self.bookDB.get_book_by_id(id_book)
            history_list.append(
                f"User: {firstname} {lastname} borrowed book '{title}' isbn: {isbn} at: {borrow_date}, returned: {bool(returned)}")
        return history_list

# test = LibraryManager("localhost", "root")
#
# test.userDB.add_user("Jan", "Nowak")
#
# test.authorDB.add_author("Jan", "Nowak")
#
# test.categoryDB.add_category("SciFi")
#
# test.bookDB.add_book("Ciekawy tytul", 1, 12341, 1)
#
# test.libDB.execute("SELECT COUNT(*) FROM category")
#
# print(test.libDB.single_response())
#
# test.libDB.execute("SELECT COUNT(1) FROM category")
#
# print(test.libDB.response())
#
# print(test.userDB.get_user_by_id(1))
#
#
# print(test.userDB.get_user_specific_fields("firstname", "lastname"))
#
# test.borrowHist.borrow_book(1, 1)
#
# test.borrowHist.return_book(1, 1)
