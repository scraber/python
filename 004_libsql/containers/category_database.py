from basic.category import Category


class CategoryDatabase:
    def __init__(self, database):
        self.database = database

    def add_category(self, name: str):
        self.database.add_entry("category", name)

    def remove_category(self, id_category: int):
        self.database.remove_entry("category", id_category)

    def get_category_specific_fields(self, *args):
        return self.database.select_specific_fields("category", *args)

    def get_category_by_id(self, idx: int):
        uid, name = self.database.select_by_id("category", idx)
        return Category(uid, name)

    def get_all_categories(self):
        category_list = list()
        for response in self.database.select_all("category"):
            uid, name = response
            category_list.append(Category(uid, name))
        return category_list

    def get_categories_selection(self):
        return self.database.select_all("category")
