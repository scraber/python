from basic.author import Author
import unittest

class TestAuthor(unittest.TestCase):
    def test_init(self):
        test_author = Author("Jan", "Nowak")
        self.assertEqual(test_author.firstname, "Jan")
        self.assertEqual(test_author.lastname, "Nowak")