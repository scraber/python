from basic.category import Category
import unittest


class TestCategory(unittest.TestCase):
    def test_init(self):
        test_category = Category(1, "Fantasy")
        self.assertEqual(test_category.uid, 1)
        self.assertEqual(test_category.name, "Fantasy")

    def test_eq(self):
        test_eq1 = Category(1, "History")
        test_eq2 = Category(2, "History")
        test_eq3 = Category(3, "Novel")

        self.assertEqual((test_eq1 == test_eq2), True)
        self.assertEqual((test_eq2 == test_eq3), False)
