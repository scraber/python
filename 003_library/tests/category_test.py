from category import Category
import unittest


class TestCategory(unittest.TestCase):
    def test_init(self):
        test_category1 = Category("Fantasy")
        category1_uid = test_category1.uid
        self.assertEqual(test_category1.category, "Fantasy")

        test_category2 = Category("SciFi")
        category2_uid = test_category2.uid
        self.assertEqual(test_category2.category, "SciFi")

        self.assertEqual(category1_uid + 1, category2_uid)

    def test_eq(self):
        test_eq1 = Category("History")
        test_eq2 = Category("History")
        test_eq3 = Category("Novel")

        self.assertEqual((test_eq1 == test_eq2), True)
        self.assertEqual((test_eq2 == test_eq3), False)

    def to_json_get_name(self):
        test_category = Category("Romance")
        self.assertEqual(test_category.to_json(), "Romance")
        self.assertEqual(test_category.get_name(), "Romance")
