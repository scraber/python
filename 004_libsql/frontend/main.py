from flask import Flask, render_template, url_for, redirect, flash
from frontend.forms import AddAuthorForm, AddUserForm, AddBookForm, AddCategoryForm
from LibraryManager import LibraryManager

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
    db.libDB.mydb.commit()
    add = AddUserForm()
    if add.validate_on_submit():
        db.userDB.add_user(add.firstname.data, add.lastname.data)
        flash(f'User {add.firstname.data} {add.lastname.data} added', 'success')
        return redirect(url_for('userdb'))
    return render_template('userdb.html', menu_name="User Database", users=db.userDB.get_all_users(), form=add)


@app.route('/bookdb', methods=['GET', 'POST'])
def bookdb():
    db.libDB.mydb.commit()
    add = AddBookForm()
    add.category.choices = db.categoryDB.get_categories_selection()
    add.author.choices = db.authorDB.get_authors_selection()
    if add.validate_on_submit():
        db.bookDB.add_book(add.title.data, add.category.data, add.isbn.data, add.author.data)
        flash(f'Book {add.title.data} {add.isbn.data} added', 'success')
        return redirect(url_for('bookdb'))
    return render_template('bookdb.html', menu_name="Book Database", books=db.get_all_books(), form=add)


@app.route('/categorydb', methods=['GET', 'POST'])
def categorydb():
    db.libDB.mydb.commit()
    add = AddCategoryForm()
    if add.validate_on_submit():
        db.categoryDB.add_category(add.name.data)
        flash(f'Category {add.name.data} added', 'success')
        return redirect(url_for('categorydb'))
    return render_template('categorydb.html', menu_name="Category Database",
                           categories=db.categoryDB.get_all_categories(), form=add)


@app.route('/authordb', methods=['GET', 'POST'])
def authordb():
    db.libDB.mydb.commit()
    add = AddAuthorForm()
    if add.validate_on_submit():
        db.authorDB.add_author(add.firstname.data, add.lastname.data)
        flash(f'Author {add.firstname.data} {add.lastname.data} added', 'success')
        return redirect(url_for('authordb'))
    return render_template('authordb.html', menu_name="Author Database", authors=db.authorDB.get_all_authors(),
                           form=add)


@app.route('/history')
def history():
    return render_template('history.html', menu_name="Borrow History", history=db.get_whole_book_history())


if __name__ == '__main__':
    app.run(debug=True)
