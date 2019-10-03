import json
import logging


class Manager:

    def __init__(self):
        self.json_file = None
        self.categories = dict()

    def read_categories_file(self, filename: str = "categories.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.json_file = open(filename, 'r')
        try:
            self.categories = json.load(self.json_file)
        except ValueError:
            logging.error("Cannot parse %s", filename)
        self.json_file.close()

    def add_category_to_file(self, new_category: str, new_id: int, filename: str = "categories.json"):
        if new_category not in self.categories:
            self.json_file = open(filename, 'w')
            self.categories[new_category] = new_id
            json.dump(self.categories, self.json_file)
            logging.debug("Added %s category", new_category)
        else:
            logging.warning("%s category already exists", new_category)

    def get_category_id(self, category: str):
        return self.categories.get(category)
