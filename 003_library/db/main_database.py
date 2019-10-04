import json
import logging


class Database:

    def __init__(self, db_filename: str = "json/database.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.db = dict()

        try:
            with open(db_filename) as json_db:
                self.db = json.load(json_db)
        except ValueError:
            logging.error("Cannot parse %s", db_filename)
        except FileNotFoundError:
            logging.warning("Couldn't find %s", db_filename)

    def save_db(self, db_filename: str = "json/database.json"):
        with open(db_filename, 'w') as json_db:
            json.dump(self.db, json_db, indent=4)


test = Database()
test.save_db()
