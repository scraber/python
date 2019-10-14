from LibraryManager import LibraryManager
import unittest


class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.test = LibraryManager("localhost", "root", "test_lib")

    def test_add_author(self):
        self.test.libDB.mycursor.execute("SELECT COUNT(1) FROM author")
        len_before_add, = self.test.libDB.single_response()
        self.test.add_author("Jan", "Nowak")
        self.test.libDB.mycursor.execute("SELECT COUNT(1) FROM author")
        self_after_add, = self.test.libDB.single_response()
        self.assertEqual(len_before_add + 1, self_after_add)
        self.test.libDB.mycursor.execute("SELECT firstname,lastname FROM author")
        author_firstname, author_lastname = self.test.libDB.single_response()
        self.assertEqual(author_firstname, "Jan")
        self.assertEqual(author_lastname, "Nowak")

    def test_add_user(self):
        self.test.libDB.mycursor.execute("SELECT COUNT(1) FROM user")
        len_before_add, = self.test.libDB.single_response()
        self.test.add_user("Jan", "Nowak")
        self.test.libDB.mycursor.execute("SELECT COUNT(1) FROM user")
        self_after_add, = self.test.libDB.single_response()
        self.assertEqual(len_before_add + 1, self_after_add)
        self.test.libDB.mycursor.execute("SELECT firstname,lastname FROM user")
        user_firstname, user_lastname = self.test.libDB.single_response()
        self.assertEqual(user_firstname, "Jan")
        self.assertEqual(user_lastname, "Nowak")

    # def tearDown(self):
    #     self.test.libDB.mycursor.execute("DROP DATABASE test_lib")
    #     self.test.libDB.response()
