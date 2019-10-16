import os, sys
from mysql.connector import errors
from LibraryManager import LibraryManager


class Menu:

    def __init__(self):
        self.manager = LibraryManager("localhost", "root")
        self.menu = [["1: User Database", "2: Book Database", "3: Category Database", "4: Author Database", "0: Exit"]]
        self.user_submenu = ["1: Add user", "2: Remove user", "3: View users", "4: View active users",
                             "5: Toggle inactive users", "0: Return"]
        self.user_operations_submenu = ["1: Borrow book", "2: Return book", "0: Return"]
        self.book_submenu = ["1: Add book", "2: Remove book", "3: View all books", "4: View all books by category",
                             "5: View borrow history", "0: Return"]
        self.category_submenu = ["1: Add category", "2: Remove category", "3: View categories", "0: Return"]
        self.author_submenu = ["1: Add author", "2: Remove author", "3: View authors", "0: Return"]

    def enter_submenu(self, submenu):
        self.menu.append(submenu)
        os.system('cls||clear')
        self.show(self.menu)

    def exit_submenu(self):
        self.menu.pop()

    def show(self, menu: list):
        if 0 == len(menu[-1]):
            print("Empty")
        else:
            for entry in menu[-1]:
                print(f"{entry}")

    def selection(self, entry):
        pass

    def main_menu_selection(self):
        os.system('cls||clear')
        m.show(m.menu)
        key = input(">> ")

        if '1' == key:
            self.enter_submenu(self.user_submenu)
            self.user_submenu_selection()
        elif '2' == key:
            self.enter_submenu(self.book_submenu)
            self.book_submenu_selection()
        elif '3' == key:
            self.enter_submenu(self.category_submenu)
            self.category_submenu_selection()
        elif '4' == key:
            self.enter_submenu(self.author_submenu)
            self.author_submenu_selection()
        elif '0' == key:
            sys.exit()

    def user_submenu_selection(self):
        while True:
            os.system('cls||clear')
            self.show(self.menu)
            key = input(">> ")

            if '1' == key:
                os.system('cls||clear')
                firstname = input("New user firstname: ")
                lastname = input("New user lastname: ")
                self.manager.userDB.add_user(firstname, lastname)
                print(f"User {firstname} {lastname} added")
                input(">> ")
            elif '2' == key:
                user_list = self.manager.userDB.get_all_users()
                self.enter_submenu(user_list)
                self.manager.userDB.remove_user(input("Id of user to remove: "))
                print(f"User removed")
                input(">> ")
                self.exit_submenu()
            elif '3' == key:
                user_list = self.manager.userDB.get_all_users()
                self.enter_submenu(user_list)
                input(">> ")
                self.exit_submenu()
            elif '4' == key:
                user_list = self.manager.userDB.get_all_users_by_activity(True)
                user_list.append("0: Return")
                self.enter_submenu(user_list)
                key = input(">> ")
                self.exit_submenu()
                if '0' != key:
                    self.enter_submenu(self.user_operations_submenu)
                    self.user_operations_selection(key)
            elif '5' == key:
                user_list = self.manager.userDB.get_all_users_by_activity(False)
                self.enter_submenu(user_list)
                self.manager.libDB.update_user_active(input("Id of user to activate: "), True)
                input(">> ")
                self.exit_submenu()
            elif '0' == key:
                self.exit_submenu()
                break

    def user_operations_selection(self, id_user):
        while True:
            os.system('cls||clear')
            self.show(self.menu)
            key = input(">> ")
            if '1' == key:
                book_list = self.manager.get_available_books()
                self.enter_submenu(book_list)
                id_book = input(">> ")
                self.manager.historyDB.borrow_book(id_user, id_book)
                input(">> ")
                self.exit_submenu()
            elif '2' == key:
                input(">> ")
                self.exit_submenu()
            elif '0' == key:
                self.exit_submenu()
                break

    def book_submenu_selection(self):
        while True:
            os.system('cls||clear')
            self.show(self.menu)
            key = input(">> ")

            if '1' == key:
                os.system('cls||clear')
                title = input("New book title: ")
                category_list = self.manager.categoryDB.get_all_categories()
                self.enter_submenu(category_list)
                try:
                    category = int(input("New book category: "))
                    os.system('cls||clear')
                    isbn = int(input("New book isbn: "))
                    os.system('cls||clear')
                    author = int(input("New book author: "))
                    os.system('cls||clear')
                    self.manager.bookDB.add_book(title, category, isbn, author)
                    print(f"Book {title} by {author} Category: {category} {isbn} added")
                except ValueError:
                    print("Pick correct number!")
                except errors.DatabaseError:
                    print("Invalid selection!")
                input(">> ")
                self.exit_submenu()
            elif '2' == key:
                book_list = self.manager.get_all_books()
                self.enter_submenu(book_list)
                try:
                    self.manager.bookDB.remove_book(int(input("Id of book to remove: ")))
                    print(f"Book removed")
                except ValueError:
                    print("Pick correct number!")
                input(">> ")
                self.exit_submenu()
            elif '3' == key:
                book_list = self.manager.get_all_books()
                self.enter_submenu(book_list)
                input(">> ")
                self.exit_submenu()
            elif '4' == key:
                category_list = self.manager.categoryDB.get_all_categories()
                self.enter_submenu(category_list)
                try:
                    search_category = int(input("Id of category : "))
                    book_list = self.manager.get_all_books_by_category(search_category)
                    self.exit_submenu()
                    self.enter_submenu(book_list)
                except ValueError:
                    print("Pick correct number!")
                input(">> ")
                self.exit_submenu()
            elif '5' == key:
                hist_list = self.manager.get_whole_book_history()
                self.enter_submenu(hist_list)
                input(">> ")
                self.exit_submenu()
            elif '0' == key:
                self.exit_submenu()
                break

    def category_submenu_selection(self):
        while True:
            os.system('cls||clear')
            self.show(self.menu)
            key = input(">> ")

            if '1' == key:
                os.system('cls||clear')
                name = input("New category name: ")
                self.manager.categoryDB.add_category(name)
                print(f"Category {name} added")
                input(">> ")
            elif '2' == key:
                category_list = self.manager.categoryDB.get_all_categories()
                self.enter_submenu(category_list)
                try:
                    self.manager.categoryDB.remove_category(int(input("Id of category to remove: ")))
                    print(f"Category removed")
                except ValueError:
                    print("Pick correct number!")
                except errors.IntegrityError:
                    print(f"Category bound to books, can't remove")
                input(">> ")
                self.exit_submenu()
            elif '3' == key:
                category_list = self.manager.categoryDB.get_all_categories()
                self.enter_submenu(category_list)
                input(">> ")
                self.exit_submenu()
            elif '0' == key:
                self.exit_submenu()
                break

    def author_submenu_selection(self):
        while True:
            os.system('cls||clear')
            self.show(self.menu)
            key = input(">> ")

            if '1' == key:
                os.system('cls||clear')
                firstname = input("New author firstname: ")
                lastname = input("New author lastname: ")
                self.manager.authorDB.add_author(firstname, lastname)
                print(f"Author {firstname} {lastname} added")
                input(">> ")
            elif '2' == key:
                user_list = self.manager.authorDB.get_all_authors()
                self.enter_submenu(user_list)
                self.manager.authorDB.remove_author(input("Id of author to remove: "))
                print(f"Author removed")
                input(">> ")
                self.exit_submenu()
            elif '3' == key:
                user_list = self.manager.authorDB.get_all_authors()
                self.enter_submenu(user_list)
                input(">> ")
                self.exit_submenu()
            elif '0' == key:
                self.exit_submenu()
                break


m = Menu()

while (True):
    m.main_menu_selection()
