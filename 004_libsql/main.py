from flask import Flask, request, render_template, url_for, redirect, flash, escape
from mysql.connector import errors
from forms import AddAuthorForm, AddUserForm, AddBookForm, AddCategoryForm, RemoveUserForm, RemoveAuthorForm, \
    RemoveCategoryForm, RemoveBookForm
from LibraryManager import LibraryManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "2b52b699599a77ca01125ff5fcd6c45a"
db = LibraryManager("localhost", "root")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/userdb", methods=["GET", "POST"])
def userdb():
    add = AddUserForm(request.form)
    remove = RemoveUserForm(request.form)
    remove.fullname.choices = db.userDB.get_users_selection()
    if add.validate_on_submit():
        db.userDB.add_user(add.firstname.data, add.lastname.data)
        flash(f"User {add.firstname.data} {add.lastname.data} added", "success")
        return redirect(url_for("userdb"))
    if remove.validate_on_submit():
        user = db.userDB.get_user_by_id(remove.fullname.data)
        try:
            db.userDB.remove_user(user.uid, "hard")
            flash(f"User {user} removed", "warning")
        except errors.IntegrityError:
            flash(f"User {user} currently owns book, cannot remove!", "danger")
        return redirect(url_for("userdb"))
    return render_template("userdb.html", menu_name="User Database", users=db.userDB.get_all_users(), addform=add,
                           removeform=remove)


@app.route("/userdb/activate/<uid>", methods=["POST"])
def activate(uid=None):
    db.libDB.update_user_active(int(uid), True)
    return redirect(url_for("userdb"))


@app.route("/userdb/deactivate/<uid>", methods=["POST"])
def deactivate(uid=None):
    db.libDB.update_user_active(int(uid), False)
    return redirect(url_for("userdb"))


@app.route("/sort_by_categories", methods=["GET"])
def sort_by_categories():
    id_category = int(request.args.get("category"))
    if 0 == id_category:
        id_category = None
    return redirect(url_for('bookdb', category=id_category))


@app.route("/bookdb", methods=["GET", "POST"])
def bookdb():
    id_category = request.args.get("category")
    if None is id_category:
        book_list = db.get_all_books()
        category = None
    else:
        book_list = db.get_all_books_by_category(id_category)
        category = db.categoryDB.get_category_by_id(id_category)
    add = AddBookForm(request.form)
    remove = RemoveBookForm(request.form)
    add.category.choices = db.categoryDB.get_categories_selection()
    add.author.choices = db.authorDB.get_authors_selection()
    remove.book.choices = db.get_all_books_selection()
    if add.validate_on_submit():
        db.bookDB.add_book(add.title.data, add.category.data, add.isbn.data, add.author.data)
        flash(f"Book {add.title.data} {add.isbn.data} added", "success")
        return redirect(url_for("bookdb"))
    if remove.validate_on_submit():
        book = db.get_book_by_id(remove.book.data)
        db.bookDB.remove_book(book.uid)
        flash(f"Book {book} removed", "warning")
    return render_template("bookdb.html", menu_name="Book Database", books=book_list, addform=add,
                           removeform=remove, categories=db.categoryDB.get_all_categories(),
                           category=category)


@app.route("/categorydb", methods=["GET", "POST"])
def categorydb():
    add = AddCategoryForm(request.form)
    remove = RemoveCategoryForm(request.form)
    remove.name.choices = db.categoryDB.get_categories_selection()
    if add.validate_on_submit():
        db.categoryDB.add_category(add.name.data)
        flash(f"Category {add.name.data} added", "success")
        return redirect(url_for("categorydb"))
    if remove.validate_on_submit():
        category = db.categoryDB.get_category_by_id(remove.name.data)
        try:
            db.categoryDB.remove_category(category.uid)
            flash(f"Category {category} removed", "warning")
        except errors.IntegrityError:
            flash(f"Category {category} is being used, cannot remove!", "danger")
        return redirect(url_for("categorydb"))
    return render_template("categorydb.html", menu_name="Category Database",
                           categories=db.categoryDB.get_all_categories(), addform=add, removeform=remove)


@app.route("/authordb", methods=["GET", "POST"])
def authordb():
    add = AddAuthorForm(request.form)
    remove = RemoveAuthorForm(request.form)
    remove.fullname.choices = db.authorDB.get_authors_selection()
    if add.validate_on_submit():
        db.authorDB.add_author(add.firstname.data, add.lastname.data)
        flash(f"Author {add.firstname.data} {add.lastname.data} added", "success")
        return redirect(url_for("authordb"))
    if remove.validate_on_submit():
        author = db.authorDB.get_author_by_id(remove.fullname.data)
        try:
            db.authorDB.remove_author(author.uid)
            flash(f"Author {author} removed", "warning")
        except errors.IntegrityError:
            flash(f"Author {author} is being used, cannot remove!", "danger")
        return redirect(url_for("authordb"))
    return render_template("authordb.html", menu_name="Author Database", authors=db.authorDB.get_all_authors(),
                           addform=add, removeform=remove)


@app.route("/return_book/<uid_user>/<uid_book>", methods=["POST"])
def return_book(uid_user=None, uid_book=None):
    db.historyDB.return_book(uid_user, uid_book)
    return redirect(url_for("history"))


@app.route("/borrow_book")
def borrow_book():
    db.libDB.mydb.commit()
    return render_template("borrow.html", menu_name="Borrow Book", users=db.userDB.get_all_users_by_activity(True))


@app.route("/borrow_book/<uid_user>", methods=["POST"])
def borrow_book_user(uid_user=None):
    return render_template("borrow.html", menu_name="Borrow Book", books=db.get_available_books(), user=uid_user)


@app.route("/borrow_book/<uid_user>/<uid_book>", methods=["POST"])
def borrow_book_user_book(uid_user=None, uid_book=None):
    db.historyDB.borrow_book(uid_user, uid_book)
    return redirect(url_for("history"))


@app.route("/history")
def history():
    db.libDB.mydb.commit()
    return render_template("history.html", menu_name="Borrow History", history=db.get_whole_book_history())


if __name__ == "__main__":
    app.run(debug=True)
