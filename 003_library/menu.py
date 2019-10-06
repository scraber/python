import curses
from user_database import UserDatabase
from book_database import BookDatabase, Book, Author, Category

users = UserDatabase("user_database.json")
books = BookDatabase("book_database.json")

login = ["User", "Admin", "Exit"]
admin_login = ["Book Database", "User Database", "Manage Books", "Manage Users"]
book_sort_by = ['View all', 'By category']
manage_books = ["Add Book", "Remove Book"]
manage_users = ["Add User", "Remove User"]
book_menu = books.get_book_list()
menu = [login]


def print_menu(menu_to_print: list, stdscr, selected_row_idx):
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


def print_submenu_text(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2
    y = h * 3 // 7
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def enter_submenu(submenu_to_add):
    menu.append(submenu_to_add)


def exit_submenu():
    menu.pop()


def menu_select(position):
    return menu[-1][position]


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def row_out_of_bounds(row, menu_to_print):
    if row < 0:
        row = len(menu_to_print[-1]) - 1
    elif row > len(menu_to_print[-1]) - 1:
        row = 0
    return row


def console_input(stdscr, text: str):
    word = str()
    print_submenu_text(stdscr, text)
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
            print_submenu_text(stdscr, text)
        else:
            word += chr(key)

        x = w // 2 - len(word) // 2
        stdscr.addstr(y, x, word)

    curses.curs_set(0)
    return word


def add_book(stdscr):
    # new_book_id = int(console_input(stdscr))
    # new_book_category = console_input(stdscr)
    # new_book_isbn = console_input(stdscr)
    # new_book_author = str(console_input(stdscr))
    # new_cat = str(console_input(stdscr))
    # new_book_category = Category(new_cat, )
    # new_book = Book(new_book_id, new_book_title, Category(new_book_category, new_book_category_id), new_book_isbn,
    #             Author(new_book_author_first, new_book_author_last))
    new_book = Book(str(console_input(stdscr, "Title")), "SciFi",
                    534635345, Author("Borys", "Szyc"), True)
    books.add(new_book)
    books.save_db()
    print_center(stdscr, f"Book '{new_book.title}' added")
    stdscr.getch()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_CYAN)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(menu, stdscr, current_row)

    while True:

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu[-1]) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            if menu_select(current_row) == "User":
                enter_submenu(users.get_users_list())
            elif menu_select(current_row) == "Admin":
                enter_submenu(admin_login)
            elif menu_select(current_row) == "Book Database":
                enter_submenu(book_sort_by)
            elif menu_select(current_row) == "View all":
                enter_submenu(books.get_book_list())
            elif menu_select(current_row) == "By category":
                enter_submenu(books.list_by_category(console_input(stdscr, "Category:")))
            elif menu_select(current_row) == "User Database":
                enter_submenu(users.get_users_list("admin"))
            elif menu_select(current_row) == "Manage Books":
                enter_submenu(manage_books)
                current_row = 0
            elif menu_select(current_row) == "Add Book":
                add_book(stdscr)
            elif menu_select(current_row) == "Manage Users":
                enter_submenu(manage_users)
            elif menu_select(current_row) == "Exit":
                break
        elif key == 27:  # ESC key
            if len(menu) == 1:
                break
            else:
                exit_submenu()
        elif key == 113:  # q key
            break

        print_menu(menu, stdscr, current_row)


curses.wrapper(main)
