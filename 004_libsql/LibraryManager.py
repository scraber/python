from Database import Database


class LibraryManager:
    def __init__(self, host: str, user: str, database_name: str = "library_db"):
        self.libDB = Database(host, user, database_name)
        self.libDB.connect()
        self.libDB.prepare_database()

    def add_author(self, firstname: str, lastname: str):
        self.libDB.add_entry("author", firstname, lastname)

    def add_user(self, firstname: str, lastname: str):
        self.libDB.add_entry("user", firstname, lastname)

    def add_category(self, name: str):
        self.libDB.add_entry("category", name)

    def add_book(self, title: str, id_category: int, isbn: int, id_author: int):
        self.libDB.add_entry("book", title, id_category, isbn, id_author)

    def remove_author(self, id_author):
        self.libDB.remove_entry("author", id_author)

    def remove_user(self, id_user, remove: str = "soft"):
        if "soft" == remove:
            self.libDB.update_user_active(id_user, False)
        elif "hard" == remove:
            self.libDB.remove_entry("user", id_user)

    def remove_category(self, id_category):
        self.libDB.remove_entry("category", id_category)

    def remove_book(self, id_book):
        self.libDB.remove_entry("book", id_book)

    def borrow_book(self, id_user, id_book):
        self.libDB.add_entry("history", id_user, id_book)

    def return_book(self, id_user, id_book):
        self.libDB.update_history_returned(id_user, id_book)

    def get_author_by_id(self, idx: int):
        return self.libDB.select_by_id("author", idx)

    def get_user_by_id(self, idx: int):
        return self.libDB.select_by_id("user", idx)

    def get_category_by_id(self, idx: int):
        return self.libDB.select_by_id("category", idx)

    def get_book_by_id(self, idx: int):
        return self.libDB.select_by_id("book", idx)

    def get_all_authors(self):
        return self.libDB.select_all("authors")

    def get_all_users(self):
        return self.libDB.select_all("user")

    def get_all_categories(self):
        return self.libDB.select_all("category")

    def get_all_books(self):
        return self.libDB.select_all("book")

# test = LibraryManager("localhost", "root")
# test.add_user("Jan", "Nowak")
# test.add_author("Jan", "Nowak")
# test.add_category("SciFi")
# test.add_book("Ciekawy tytul", 1, 12341, 1)
#
# test.libDB.execute("SELECT COUNT(*) FROM category")
# print(test.libDB.single_response())
# test.libDB.execute("SELECT COUNT(1) FROM category")
# print(test.libDB.response())
#
# test.borrow_book(1, 1)
# test.return_book(1, 1)
