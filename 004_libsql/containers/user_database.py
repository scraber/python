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
        uid, firstname, lastname, active = self.database.select_by_id("user", idx)
        return User(uid, firstname, lastname, active)

    def get_all_users(self):
        user_list = list()
        for response in self.database.select_all("user"):
            uid, firstname, lastname, _ = response
            user_list.append(User(uid, firstname, lastname))
        return user_list

    def get_all_users_by_activity(self, is_active: bool):
        user_list = list()
        self.database.execute(f"SELECT * FROM user where active = {is_active}")
        for response in self.database.response():
            uid, firstname, lastname, _ = response
            user_list.append(User(uid, firstname, lastname))
        return user_list

    def get_users_selection(self):
        user_list = list()
        for response in self.database.select_all("user"):
            uid, firstname, lastname, _ = response
            user_list.append((uid, f"{firstname} {lastname}"))
        return user_list
