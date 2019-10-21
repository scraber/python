from Database import Database
from basic.book import Book
from containers.borrow_history import BorrowHistory
from containers.category_database import CategoryDatabase
from containers.book_database import BookDatabase
from containers.author_database import AuthorDatabase
from containers.user_database import UserDatabase


class LibraryManager:
    def __init__(
            self, host: str, user: str, database_name: str = "library_db"
    ):
        self.libDB = Database(host, user, database_name)
        self.libDB.connect()
        self.libDB.prepare_database()
        self.bookDB = BookDatabase(self.libDB)
        self.authorDB = AuthorDatabase(self.libDB)
        self.userDB = UserDatabase(self.libDB)
        self.categoryDB = CategoryDatabase(self.libDB)
        self.historyDB = BorrowHistory(self.libDB)

    def get_book_by_id(self, idx):
        uid, title, id_category, isbn, id_author = self.libDB.select_by_id("book", idx)
        book = Book(uid, title, self.categoryDB.get_category_by_id(id_category), isbn,
                    self.authorDB.get_author_by_id(id_author))
        return book

    def get_all_books(self):
        book_list = list()
        for response in self.bookDB.get_all():
            uid, title, id_category, isbn, id_author = response
            book_list.append(Book(uid, title, self.categoryDB.get_category_by_id(id_category), isbn,
                                  self.authorDB.get_author_by_id(id_author)))
        return book_list

    def get_all_books_selection(self):
        book_list = list()
        for response in self.bookDB.get_all():
            uid, title, id_category, isbn, id_author = response
            book = Book(uid, title, self.categoryDB.get_category_by_id(id_category), isbn,
                        self.authorDB.get_author_by_id(id_author))
            book_list.append((uid, f"{book}"))
        return book_list

    def get_all_books_by_category(self, id_category):
        book_list = list()
        for response in self.bookDB.get_by_category(id_category):
            uid, title, id_category, isbn, id_author = response
            book_list.append(Book(uid, title, self.categoryDB.get_category_by_id(id_category), isbn,
                                  self.authorDB.get_author_by_id(id_author)))
        return book_list

    def get_available_books(self):
        book_list = list()
        for response in self.bookDB.get_all_available():
            uid, title, id_category, isbn, id_author = response
            book_list.append(Book(uid, title, self.categoryDB.get_category_by_id(id_category), isbn,
                                  self.authorDB.get_author_by_id(id_author), ))
        return book_list

    def get_whole_book_history(self):
        history_list = list()
        for response in self.historyDB.get_all():
            uid, id_user, id_book, borrow_date, returned = response
            user = self.userDB.get_user_by_id(id_user)
            uid_book, title, id_category, isbn, id_author = self.bookDB.get_book_by_id(id_book)
            book = Book(uid_book, title, self.categoryDB.get_category_by_id(id_category), isbn,
                        self.authorDB.get_author_by_id(id_author), )
            history_list.append(
                {
                    "id": uid,
                    "user": user,
                    "book": book,
                    "date": borrow_date,
                    "returned": bool(returned),
                }
            )
            return history_list
