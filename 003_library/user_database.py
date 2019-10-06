from abstract_database import AbstractDatabase
from user import User
import json


class UserDatabase(AbstractDatabase):

    def load_from_file(self):
        with open(self.db_filename) as json_db:
            data = json.load(json_db)
        for uid in data:
            self.data[int(uid)] = User(data[uid]["firstname"], data[uid]["lastname"])

    def get_users_list(self, view: str = "user"):
        user_list = list()

        for uid in self.data:
            user_list.append(self.data.get(uid).__str__(view))

        return user_list

#
# test = UserDatabase("user_database.json")
# test.add(User("Maciej", "Rek"))
# test.add(User("Marcin", "Przepiorkowski"))
# test.add(User("Marcin", "Szeryf"))
# test.save_db()
