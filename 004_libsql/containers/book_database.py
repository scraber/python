class BookDatabase:
    def __init__(self, database):
        self.database = database

    def add_book(self, title: str, id_category: int, isbn: int, id_author: int):
        self.database.add_entry("book", title, id_category, isbn, id_author)

    def remove_book(self, id_author: int):
        self.database.remove_entry("book", id_author)

    def get_book_specific_fields(self, *args):
        return self.database.select_specific_fields("book", *args)

    # def get_book_by_id(self, idx: int):
    #     return self.database.select_by_id("book", idx)

    def get_all(self):
        return self.database.select_all("book")

    def get_by_category(self, idx: int):
        self.database.execute(f"SELECT * FROM book where id_category = {idx}")
        return self.database.response()

    def get_all_available(self):
        self.database.execute(
            f"SELECT * FROM book where id NOT IN (SELECT id_book from history where returned = False)")
        return self.database.response()
