class AuthorDatabase:

    def __init__(self, database):
        self.database = database

    def add_author(self, firstname: str, lastname: str):
        self.database.add_entry("author", firstname, lastname)

    def remove_author(self, id_author):
        self.database.remove_entry("author", id_author)

    def get_author_specific_fields(self, *args):
        return self.database.select_specific_fields("author", *args)

    def get_author_by_id(self, idx: int):
        _, firstname, lastname = self.database.select_by_id("author", idx)
        return f"{firstname} {lastname}"

    def get_all_authors(self):
        return self.database.select_all("author")
