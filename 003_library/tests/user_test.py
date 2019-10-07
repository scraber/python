from user import User
import unittest


class TestUser(unittest.TestCase):
    def test_init(self):
        test_user1 = User("Marek", "Kowalski")
        user1_uid = test_user1.uid
        self.assertEqual(test_user1.firstname, "Marek")
        self.assertEqual(test_user1.lastname, "Kowalski")

        test_user2 = User("Jack", "Blacksmith")
        user2_uid = test_user2.uid
        self.assertEqual(test_user2.firstname, "Jack")
        self.assertEqual(test_user2.lastname, "Blacksmith")

        self.assertEqual(user1_uid + 1, user2_uid)
