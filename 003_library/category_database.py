from category import Category
import json
import logging


class CategoryDatabase:

    def __init__(self, db_filename: str = "category_database.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.categories = dict()

        try:
            with open(db_filename) as json_db:
                data = json.load(json_db)
            for uid in data:
                self.categories[int(uid)] = Category(data[uid])

        except ValueError:
            logging.error("Cannot parse %s", db_filename)
        except FileNotFoundError:
            logging.warning("Couldn't find %s", db_filename)

    def add_category(self, add_new: Category):
        if add_new not in self.categories:
            self.categories[add_new.id] = add_new
            logging.debug("Added %s category", add_new.category)
        else:
            logging.warning("%s category already exists", add_new.category)

    def remove_category(self, remove: Category):
        if remove in self.categories:
            del self.categories[remove.id]
            logging.debug("User %s removed from database", remove.category)
        else:
            logging.warning("User %s doesn't exists!", remove.category)

    def save_db(self, db_filename: str = "category_database.json"):
        update_db = dict()
        for uid in self.categories:
            update_db[uid] = self.categories.get(uid).__str__()

        with open(db_filename, 'w') as json_db:
            json.dump(update_db, json_db, indent=4)




db = CategoryDatabase()
# db.add_category(Category("Cookbook"))
# db.add_category(Category("Romance"))
# db.add_category(Category("SciFi"))
# db.add_category(Category("Fantasy"))
# db.add_category(Category("Crime"))
# db.add_category(Category("Historical"))
# db.add_category(Category("Biography"))
# db.add_category(Category("Science"))
# db.add_category(Category("Travel"))
db.save_db()
