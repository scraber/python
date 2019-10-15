from basic.user import User


class UserDatabase:

    def __init__(self, database):
        self.database = database

    def add_user(self, firstname: str, lastname: str):
        self.database.add_entry("user", firstname, lastname)

    def remove_user(self, id_user, remove: str = "soft"):
        if "soft" == remove:
            self.database.update_user_active(id_user, False)
        elif "hard" == remove:
            self.database.remove_entry("user", id_user)

    def get_user_specific_fields(self, *args):
        return self.database.select_specific_fields("user", *args)

    def get_user_by_id(self, idx: int):
        return self.database.select_by_id("user", idx)

    def get_all_users(self):
        user_list = list()
        for response in self.database.select_all("user"):
            id, firstname, lastname, _ = response
            user_list.append(User(id, firstname, lastname))
        return user_list

    def get_all_users_by_activity(self, is_active:bool):
        user_list = list()
        self.database.execute(f"SELECT * FROM user where active = {is_active}")
        for response in self.database.response():
            id, firstname, lastname, _ = response
            user_list.append(User(id, firstname, lastname))
        return user_list
