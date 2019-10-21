from flask import Flask, request, render_template, url_for, redirect, flash
from frontend.forms import AddAuthorForm, AddUserForm, AddBookForm, AddCategoryForm, RemoveUserForm
from LibraryManager import LibraryManager
from mysql.connector import errors

app = Flask(__name__)
app.config['SECRET_KEY'] = "2b52b699599a77ca01125ff5fcd6c45a"
db = LibraryManager("localhost", "root")

posts = [
    {
        "id": 1,
        "firstname": "Jan",
        "lastname": "Rzeźnik",
        "active": True
    },
    {
        "id": 2,
        "firstname": "Piort",
        "lastname": "Usiod",
        "active": False
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/userdb', methods=['GET', 'POST'])
def userdb():
    add = AddUserForm(request.form)
    remove = RemoveUserForm(request.form)
    remove.fullname.choices = db.userDB.get_users_selection()
    if add.validate_on_submit():
        db.userDB.add_user(add.firstname.data, add.lastname.data)
        flash(f'User {add.firstname.data} {add.lastname.data} added', 'success')
        return redirect(url_for('userdb'))
    if remove.validate_on_submit():
        user = db.userDB.get_user_by_id(remove.fullname.data)
        try:
            db.userDB.remove_user(user.uid, "hard")
            flash(f'User {user} removed', 'warning')
        except errors.IntegrityError:
            flash(f'Cannot remove {user}!', 'danger')
        return redirect(url_for('userdb'))
    return render_template('userdb.html', menu_name="User Database", users=db.userDB.get_all_users(), addform=add,
                           removeform=remove)


@app.route('/bookdb', methods=['GET', 'POST'])
def bookdb():
    add = AddBookForm(request.form)
    add.category.choices = db.categoryDB.get_categories_selection()
    add.author.choices = db.authorDB.get_authors_selection()
    if add.validate_on_submit():
        db.bookDB.add_book(add.title.data, add.category.data, add.isbn.data, add.author.data)
        flash(f'Book {add.title.data} {add.isbn.data} added', 'success')
        return redirect(url_for('bookdb'))
    return render_template('bookdb.html', menu_name="Book Database", books=db.get_all_books(), addform=add)


@app.route('/categorydb', methods=['GET', 'POST'])
def categorydb():
    add = AddCategoryForm(request.form)
    if add.validate_on_submit():
        db.categoryDB.add_category(add.name.data)
        flash(f'Category {add.name.data} added', 'success')
        return redirect(url_for('categorydb'))
    return render_template('categorydb.html', menu_name="Category Database",
                           categories=db.categoryDB.get_all_categories(), addform=add)


@app.route('/authordb', methods=['GET', 'POST'])
def authordb():
    add = AddAuthorForm(request.form)
    if add.validate_on_submit():
        db.authorDB.add_author(add.firstname.data, add.lastname.data)
        flash(f'Author {add.firstname.data} {add.lastname.data} added', 'success')
        return redirect(url_for('authordb'))
    return render_template('authordb.html', menu_name="Author Database", authors=db.authorDB.get_all_authors(),
                           addform=add)


@app.route('/history')
def history():
    return render_template('history.html', menu_name="Borrow History", history=db.get_whole_book_history())


if __name__ == '__main__':
    app.run(debug=True)
