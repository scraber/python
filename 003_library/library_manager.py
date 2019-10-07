from book_database import BookDatabase, Book
from category_database import CategoryDatabase, Category
from user_database import UserDatabase, User
from rentals import Rentals
import logging


class LibraryManager:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.book_db = BookDatabase("json/book_database.json")
        self.category_db = CategoryDatabase("json/category_database.json")
        self.user_db = UserDatabase("json/user_database.json")
        self.rental = Rentals(self.user_db, self.book_db)
        self.book_limit = 5

    def check_if_exists(self, item, db):
        for idx in db:
            if item == db[idx]:
                return True
        else:
            return False

    def rent_book(self, user: User, book: Book):
        if self.book_limit > self.rental.count_currently_owning(user, self.book_db):
            self.rental.rent_book(user, book, self.book_db)
            logging.debug("User %s rent book %s", user.__str__(), book.title)
        else:
            logging.warning("User %s already at max book limit of %d", user.__str__(), self.book_limit)

    def add_user(self, new_user: User):
        if not self.check_if_exists(new_user, self.user_db.data):
            self.user_db.add(new_user)

            logging.debug("Added %s user to database", new_user.__str__())
        else:
            logging.warning("User %s already exists in database!", new_user.__str__())
        # self.user_db.save_db()

    def remove_user(self, old_user: User):
        if self.check_if_exists(old_user, self.user_db.data):
            del self.user_db.data[old_user.uid]
            logging.debug("Removed %s user from database", old_user.__str__())
        else:
            logging.warning("User %s not found, cant remove!", old_user.__str__())
        # self.user_db.save_db()

    def add_category(self, new_category: Category):
        if not self.check_if_exists(new_category, self.category_db.data):
            self.category_db.add(new_category)
            logging.debug("Added %s category to database", new_category.to_json())
        else:
            logging.warning("Category %s already exists in database!", new_category.to_json())
        # self.category_db.save_db()

    def remove_category(self, old_category: Category):
        if self.check_if_exists(old_category, self.category_db.data):
            del self.category_db.data[old_category.uid]
            logging.debug("Removed %s category from database", old_category.to_json())
        else:
            logging.warning("Category %s not found, cant remove!", old_category.to_json())
        # self.category_db.save_db()

    def add_book(self, new_book: Book):
        if not self.check_if_exists(new_book, self.book_db.data):
            self.book_db.add(new_book)
            logging.debug("Added %s book to database", new_book.title)
        else:
            logging.warning("Book %s already exists in database!", new_book.title)
            # self.book_db.save_db()

    def remove_book(self, old_book: Book):
        if self.check_if_exists(old_book, self.book_db.data):
            del self.book_db.data[old_book.uid]
            logging.debug("Removed %s category from database", old_book.title)
        else:
            logging.warning("Category %s not found, cant remove!", old_book.title)
        # self.book_db.save_db()


test = LibraryManager()
usr = test.user_db.get_by_name("Maciej Rek")
book = test.book_db.get_by_name("The Three Musketeers")
test.remove_book(book)
test.add_book(book)
test.rent_book(usr, book)
print(test)
