from flask import Flask, render_template, url_for
from frontend.forms import AddUserForm
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


@app.route('/userdb')
def userdb():
    add = AddUserForm()
    return render_template('userdb.html', menu_name="User Database", users=db.userDB.get_all_users(), form=add)


@app.route('/bookdb')
def bookdb():
    return render_template('bookdb.html', menu_name="Book Database", books=db.get_all_books())


@app.route('/categorydb')
def categorydb():
    return render_template('categorydb.html', menu_name="Category Database",
                           categories=db.categoryDB.get_all_categories())


@app.route('/authordb')
def authordb():
    return render_template('authordb.html', menu_name="Author Database", authors=db.authorDB.get_all_authors())


@app.route('/history')
def history():
    return render_template('history.html', menu_name="Borrow History", history=db.get_whole_book_history())


if __name__ == '__main__':
    app.run(debug=True)
