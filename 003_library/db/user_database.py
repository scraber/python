from user import User
import logging
import json


class UserDatabase:

    def __init__(self, db_filename: str = "user_database.json"):
        logging.basicConfig(level=logging.DEBUG)
        self.users = dict()

        with open(db_filename) as json_db:
            try:
                data = json.load(json_db)
                for uid in data:
                    self.users[int(uid)] = User(uid, data[uid]["firstname"], data[uid]["lastname"])
            except ValueError:
                logging.error("Couldn't parse %s", db_filename)
            except FileNotFoundError:
                logging.warning("Couldn't find %s", db_filename)

    def add_user(self, new_user: User):
        if new_user not in self.users:
            self.users[int(new_user.uid)] = new_user
            logging.debug("User %s added to database", new_user)
        else:
            logging.warning("User %s already exists!", new_user)

    def remove_user(self, remove_user: User):
        if remove_user in self.users:
            del self.users[int(remove_user.uid)]
            logging.debug("User %s removed from database", remove_user)
        else:
            logging.warning("User %s doesn't exists!", remove_user)

    def save_db(self, db_filename: str = "user_database.json"):
        update_db = dict()
        for uid in self.users:
            update_db[uid] = self.users.get(uid).to_json()
        with open(db_filename, 'w') as json_db:
            json.dump(update_db, json_db, indent=4)


test = UserDatabase()
test.add_user(User(1, "Maciej", "Rek"))
test.add_user(User(2, "Marcin", "Przepiorkowski"))
test.add_user(User(1, "Maciej", "Rek"))
test.save_db()
