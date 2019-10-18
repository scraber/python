import mysql.connector
import sys
import getpass
import logging


class Database:

    def __init__(self, host: str, user: str, database_name: str):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s:%(message)s')
        self.host = host
        self.user = user
        self.passwd = None
        self.mydb = None
        self.mycursor = None
        self.database_name = database_name

    def connect(self):
        try:

            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                # passwd=getpass.getpass("password: ")
                passwd="root"
            )
            self.mycursor = self.mydb.cursor()
            logging.debug(f"Connected to {self.host}")
        except mysql.connector.Error as err:
            logging.error(f"Couldn't connect to {self.host}: {err}")
            sys.exit(1)

    def execute(self, query: str):
        self.mycursor.execute(query)

    def single_response(self):
        return self.mycursor.fetchone()

    def response(self):
        return self.mycursor.fetchall()

    def prepare_database(self):
        self.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name} ")
        self.execute(f"USE {self.database_name}")
        logging.debug(f"Using {self.database_name}")
        self.execute(
            "CREATE TABLE IF NOT EXISTS author (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255) NOT NULL, "
            "lastname VARCHAR(255) NOT NULL)")
        self.execute(
            "CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255) NOT NULL, "
            "lastname VARCHAR(255) NOT NULL, active BIT NOT NULL DEFAULT True)")
        self.execute(
            "CREATE TABLE IF NOT EXISTS category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL)")
        self.execute(
            "CREATE TABLE IF NOT EXISTS book (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, "
            "id_category INT NOT NULL, isbn INT NOT NULL, id_author INT NOT NULL, FOREIGN KEY (id_category) "
            "REFERENCES category(id), FOREIGN KEY (id_author) REFERENCES author(id))")
        self.execute(
            "CREATE TABLE IF NOT EXISTS history (id INT AUTO_INCREMENT PRIMARY KEY, id_user INT NOT NULL, "
            "id_book INT NOT NULL, borrow_date DATE NOT NULL, returned BIT NOT NULL DEFAULT False,"
            "FOREIGN KEY (id_user) REFERENCES user(id), FOREIGN KEY (id_book) REFERENCES book(id))")

    def add_entry(self, table: str, *args):
        if "author" == table or "user" == table:
            self.execute(
                f"INSERT INTO {table} (firstname, lastname) VALUES {args}")
        elif "category" == table:
            local, = args
            self.execute(f"INSERT INTO {table} (name) VALUES ('{local}')")
        elif "book" == table:
            self.execute(
                f"INSERT INTO {table} (title, id_category, isbn, id_author) VALUES {args}")
        elif "history" == table:
            id_user, id_book = args
            self.execute(
                f"INSERT INTO {table} (id_user, id_book, borrow_date,returned) VALUES ({id_user}, {id_book}, (SELECT CURDATE()), False)")
        self.mydb.commit()
        logging.debug(f"Added {args} to {table}")

    def remove_entry(self, table: str, idx: int):
        self.execute(f"DELETE FROM {table} WHERE id = '{idx}'")
        self.mydb.commit()
        logging.debug(f"Removed {table} with id: {idx} from  {table}")

    def update_user_active(self, id_user: int, active: bool):
        self.execute(f"UPDATE user SET active = {active} WHERE id = {id_user}")
        self.mydb.commit()

    def update_history_returned(self, id_user, id_book):
        self.execute(
            f"UPDATE history SET returned = True WHERE id_user = {id_user} AND  id_book = {id_book}")
        self.mydb.commit()

    def select_specific_fields(self, table: str, *args):
        fields = ",".join(args)
        self.execute(f"SELECT {fields} FROM {table}")
        return self.response()

    def select_by_id(self, table: str, idx: int):
        self.execute(f"SELECT * FROM {table} where id = {idx}")
        return self.single_response()

    def select_all(self, table: str):
        self.execute(f"SELECT * FROM {table}")
        return self.response()
