from abstract_database import AbstractDatabase
from category import Category
import json


class CategoryDatabase(AbstractDatabase):

    def load_from_file(self):
        with open(self.db_filename) as json_db:
            data = json.load(json_db)
        for uid in data:
            self.data[int(uid)] = Category(data[uid])

#
# db = CategoryDatabase("category_database.json")
# db.add(Category("Cookbook"))
# db.add(Category("Romance"))
# db.add(Category("SciFi"))
# db.add(Category("Fantasy"))
# db.add(Category("Crime"))
# db.add(Category("Historical"))
# db.add(Category("Biography"))
# db.add(Category("Science"))
# db.add(Category("Travel"))
# db.save_db()
