from book import Book
from author import Author
import unittest


class TestBook(unittest.TestCase):
    def test_init(self):
        test_book1 = Book("Very nice title", "Fantasy", 1512315, Author("Jan", "Nowak"))
        book1_uid = test_book1.uid
        self.assertEqual(test_book1.title, "Very nice title")
        self.assertEqual(test_book1.category, "Fantasy")
        self.assertEqual(test_book1.isbn, 1512315)
        self.assertEqual(test_book1.author, Author("Jan", "Nowak"))

        test_book2 = Book("Long live the king", "SciFi", 46353234, Author("Marek", "Konrad"))
        book2_uid = test_book2.uid
        self.assertEqual(test_book2.title, "Long live the king")
        self.assertEqual(test_book2.category, "SciFi")
        self.assertEqual(test_book2.isbn, 46353234)
        self.assertEqual(test_book2.author, Author("Marek", "Konrad"))

        self.assertEqual(book1_uid + 1, book2_uid)

    def test_to_str(self):
        test_book = Book("Another title", "Historical", 421423, Author("Borys", "Szyc"))
        self.assertEqual(test_book.__str__(),
                         f"{test_book.uid}: Another title by Author: Borys Szyc, Category: Historical, ISBN: 421423, Available: True")

    def test_eq(self):
        test_eq1 = Book("Short live the king", "Fantasy", 234236234, Author("Marek", "Konrad"))
        test_eq2 = Book("Short live the king", "Fantasy", 234236234, Author("Marek", "Konrad"))
        test_eq3 = Book("Short the king", "Fantasy", 3456456, Author("Jan", "Konrad"))

        self.assertEqual((test_eq1 == test_eq2), True)
        self.assertEqual((test_eq2 == test_eq3), False)

    def test_get_name(self):
        test_book = test_book = Book("And Another title", "SciFi", 345346, Author("Borys", "Szyc"))
        self.assertEqual(test_book.get_name(), "And Another title")
