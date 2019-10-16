from basic.user import User
import unittest


class TestUser(unittest.TestCase):
    def test_init(self):
        test_user1 = User(1, "Marek", "Kowalski")
        self.assertEqual(test_user1.uid, 1)
        self.assertEqual(test_user1.firstname, "Marek")
        self.assertEqual(test_user1.lastname, "Kowalski")
