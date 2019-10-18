from basic.book import Book
from basic.author import Author
import unittest


class TestBook(unittest.TestCase):
    test_author = Author(1, "Jan", "Nowak")

    def test_init(self):
        test_book = Book(1, "Very nice title", "Fantasy",
                         1512315, self.test_author)
        self.assertEqual(test_book.uid, 1)
        self.assertEqual(test_book.title, "Very nice title")
        self.assertEqual(test_book.category, "Fantasy")
        self.assertEqual(test_book.isbn, 1512315)
        self.assertEqual(test_book.author, self.test_author)

    def test_to_str(self):
        test_book = Book(2, "Another title", "Historical",
                         421423, self.test_author)
        self.assertEqual(test_book.__str__(),
                         f"{test_book.uid}: Another title by Author: 1: Jan Nowak, Category: Historical, ISBN: 421423")

    def test_eq(self):
        test_eq1 = Book(1, "Short live the king", "Fantasy",
                        234236234, self.test_author)
        test_eq2 = Book(2, "Short live the king", "Fantasy",
                        234236234, self.test_author)
        test_eq3 = Book(3, "Short the king", "Fantasy",
                        3456456, self.test_author)

        self.assertEqual((test_eq1 == test_eq2), True)
        self.assertEqual((test_eq2 == test_eq3), False)

    def test_get_name(self):
        test_book = test_book = Book(
            4, "And Another title", "SciFi", 345346, self.test_author)
        self.assertEqual(test_book.get_name(), "And Another title")
