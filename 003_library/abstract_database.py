from abc import ABC, abstractmethod
import logging
import json


class AbstractDatabase(ABC):

    @abstractmethod
    def load_from_file(self):
        pass

    def __init__(self, db_filename: str):
        logging.basicConfig(level=logging.DEBUG)
        self.data = dict()
        self.db_filename = db_filename
        try:
            self.load_from_file()

        except ValueError:
            logging.error("Cannot parse %s", db_filename)
        except FileNotFoundError:
            logging.warning("Couldn't find %s", db_filename)

    def add(self, add_new):
        self.data[add_new.uid] = add_new

    def remove_category(self, remove):
        del self.data[remove.uid]

    def save_db(self):
        update_db = dict()
        for uid in self.data:
            update_db[uid] = self.data.get(uid).to_json()

        with open(self.db_filename, 'w') as json_db:
            json.dump(update_db, json_db, indent=4)

    def get_by_name(self, name):
        for idx in self.data:
            if name == self.data[idx].get_name():
                return self.data[idx]
