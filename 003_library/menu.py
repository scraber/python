import curses
from library_manager import LibraryManager, Book, User
from author import Author


class Menu:
    def __init__(self):
        self.menu = [["Users", "Admin"]]
        self.admin_login = ["Book Database", "User Database", "Manage Books", "Manage Users"]
        self.books_menu = ["View all", "By category"]
        self.manage_books = ["Add Book", "Remove Book"]
        self.manage_users = ["Add User", "Remove User"]
        self.manager = LibraryManager()
        self.book_list = self.manager.book_db.get_book_list()
        self.user_list = self.manager.user_db.get_users_list()

        # specify the current selected row
        self.current_row = 0

    def enter_submenu(self, submenu_to_add):
        self.current_row = 0
        self.menu.append(submenu_to_add)

    def exit_submenu(self):
        self.current_row = 0
        self.menu.pop()

    def menu_select_entry(self, position):
        return self.menu[-1][position]

    def print_menu(self, menu_to_print: list, stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(menu_to_print[-1]):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu_to_print[-1]) // 2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    def print_center(self, stdscr, text):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x = w // 2 - len(text) // 2
        y = h // 2
        stdscr.addstr(y, x, text)
        stdscr.refresh()

    def print_submenu_text(self, stdscr, text):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x = w // 2
        y = h * 3 // 7
        stdscr.addstr(y, x, text)
        stdscr.refresh()

    def move_selection_down(self):
        self.current_row += 1
        if self.current_row > len(self.menu[-1]) - 1:
            self.current_row = 0

    def move_selection_up(self):
        self.current_row -= 1
        if self.current_row < 0:
            self.current_row = len(self.menu[-1]) - 1

    def console_input(self, stdscr, text: str):
        word = str()
        self.print_submenu_text(stdscr, text)
        h, w = stdscr.getmaxyx()
        x = w // 2
        y = h // 2
        stdscr.addstr(y, x, word)
        curses.curs_set(2)

        while True:
            key = stdscr.getch()

            if key == curses.KEY_ENTER or key in [10, 13]:
                break
            elif key == curses.KEY_BACKSPACE:
                word = word[:-1]
                stdscr.clear()
                self.print_submenu_text(stdscr, text)
            else:
                word += chr(key)

            x = w // 2 - len(word) // 2
            stdscr.addstr(y, x, word)

        curses.curs_set(0)
        return word

    def submenu_selection(self, stdscr, submenu: list):
        self.enter_submenu(submenu)
        while True:
            self.print_menu(self.menu, stdscr, self.current_row)
            key = stdscr.getch()
            if key == curses.KEY_UP:
                self.move_selection_up()
            elif key == curses.KEY_DOWN:
                self.move_selection_down()
            elif key == curses.KEY_ENTER or key in [10, 13]:
                selection = self.menu_select_entry(self.current_row)
                self.exit_submenu()
                return selection
            elif key == 27:
                self.exit_submenu()
                break

    def main(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)

        # print the menu
        self.print_menu(self.menu, stdscr, self.current_row)

        while True:

            key = stdscr.getch()

            if key == curses.KEY_UP:
                self.move_selection_up()
            elif key == curses.KEY_DOWN:
                self.move_selection_down()
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # print_center(stdscr, "You selected '{}'".format(menu[current_row]))
                if self.menu_select_entry(self.current_row) == "User":
                    self.enter_submenu(self.manager.user_db.get_users_list())
                elif self.menu_select_entry(self.current_row) == "Admin":
                    self.enter_submenu(self.admin_login)
                elif self.menu_select_entry(self.current_row) == "Book Database":
                    self.enter_submenu(self.books_menu)
                elif self.menu_select_entry(self.current_row) == "View all":
                    self.enter_submenu(self.manager.book_db.get_book_list())
                elif self.menu_select_entry(self.current_row) == "By category":
                    self.view_books_by_selection(stdscr)
                # self.enter_submenu(books.list_by_category(self.console_input(stdscr, "Category:")))
                elif self.menu_select_entry(self.current_row) == "User Database":
                    self.enter_submenu(self.manager.user_db.get_users_list("admin"))
                elif self.menu_select_entry(self.current_row) == "Manage Books":
                    self.enter_submenu(self.manage_books)
                elif self.menu_select_entry(self.current_row) == "Add Book":
                    self.add_book(stdscr)
                elif self.menu_select_entry(self.current_row) == "Remove Book":
                    self.remove_book(stdscr)
                elif self.menu_select_entry(self.current_row) == "Manage Users":
                    self.enter_submenu(self.manage_users)
                elif self.menu_select_entry(self.current_row) == "Add User":
                    self.add_user(stdscr)
                elif self.menu_select_entry(self.current_row) == "Remove User":
                    self.remove_user(stdscr)
                elif self.menu_select_entry(self.current_row) == "Exit":
                    break
            elif key == 27:  # ESC key
                if len(self.menu) == 1:
                    break
                else:
                    self.exit_submenu()
            elif key == 113:  # q key
                break

            self.print_menu(self.menu, stdscr, self.current_row)

    def run(self):
        curses.wrapper(self.main)

    ######## to pewnie możnabyło gdzieś upchnąć ##########

    def add_book(self, stdscr):

        new_book = Book(str(self.console_input(stdscr, "Title")),
                        str(self.submenu_selection(stdscr, self.manager.category_db.get_category_list())),
                        int(self.console_input(stdscr, "ISBN")),
                        Author(str(self.console_input(stdscr, "Author's firstname")),
                               str(self.console_input(stdscr, "Author's lastname"))))

        self.manager.book_db.add(new_book)
        self.print_center(stdscr, f"Book {new_book.title} added to database")
        stdscr.getch()

    def remove_book(self, stdscr):
        self.enter_submenu(self.manager.book_db.get_book_list())
        while True:
            self.print_menu(self.menu, stdscr, self.current_row)
            key = stdscr.getch()
            if key == curses.KEY_UP:
                self.move_selection_up()
            elif key == curses.KEY_DOWN:
                self.move_selection_down()
            elif key == curses.KEY_ENTER or key in [10, 13]:
                self.manager.book_db.remove()
                self.exit_submenu()
                break
            elif key == 27:
                self.exit_submenu()
                break

    def view_books_by_selection(self, stdscr):
        self.enter_submenu(self.manager.category_db.get_category_list())

        while True:
            self.print_menu(self.menu, stdscr, self.current_row)
            key = stdscr.getch()
            if key == curses.KEY_UP:
                self.move_selection_up()
            elif key == curses.KEY_DOWN:
                self.move_selection_down()
            elif key == curses.KEY_ENTER or key in [10, 13]:
                selection = self.menu_select_entry(self.current_row)
                if 0 == len(self.manager.book_db.list_by_category(selection)):
                    self.print_center(stdscr, f"No books matching {selection} category")
                    stdscr.getch()
                else:
                    self.exit_submenu()
                    self.enter_submenu(self.manager.book_db.list_by_category(selection))
                    break
            elif key == 27:
                self.exit_submenu()
                break

    def add_user(self, stdscr):
        new_user = User(str(self.console_input(stdscr, "Firstname")), str(self.console_input(stdscr, "Lastname")))

        self.manager.user_db.add(new_user)
        self.print_center(stdscr, f"User {new_user.get_name()} added to database")
        stdscr.getch()

    def remove_user(self, stdscr):
        remove_user = self.manager.user_db.get_by_name(
            self.submenu_selection(stdscr, self.manager.user_db.get_users_list()))
        self.manager.user_db.remove(remove_user)

        self.print_center(stdscr, f"User {remove_user} remove from database")
        stdscr.getch()


main = Menu()
main.run()
