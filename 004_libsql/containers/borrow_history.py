class BorrowHistory:

    def __init__(self, database):
        self.database = database

    def borrow_book(self, id_user, id_book):
        self.database.add_entry("history", id_user, id_book)

    def return_book(self, id_user, id_book):
        self.database.update_history_returned(id_user, id_book)
