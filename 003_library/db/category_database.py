import json
import logging


class CategoryDatabase:

    def __init__(self, db_filename: str = "json/category_database.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.categories = dict()

        try:
            with open(db_filename) as json_db:
                self.categories = json.load(json_db)
        except ValueError:
            logging.error("Cannot parse %s", db_filename)
        except FileNotFoundError:
            logging.warning("Couldn't find %s", db_filename)

    def add_category(self, new_category: str, new_id: int):
        if new_category not in self.categories:
            self.categories[new_category] = new_id
            logging.debug("Added %s category", new_category)
        else:
            logging.warning("%s category already exists", new_category)

    def remove_category(self, remove_category: str):
        if remove_category in self.categories:
            del self.categories[remove_category]
            logging.debug("User %s removed from database", remove_category)
        else:
            logging.warning("User %s doesn't exists!", remove_category)

    def save_db(self, db_filename: str = "json/category_database.json"):
        with open(db_filename, 'w') as json_db:
            json.dump(self.categories, json_db, indent=4)


test = CategoryDatabase()
test.add_category("Romance", 1)
test.add_category("SciFi", 2)
test.save_db()
