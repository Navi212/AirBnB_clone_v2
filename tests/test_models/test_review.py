#!/usr/bin/python3
"""The `test_review` module supplies a test class `test_Review`"""


import unittest
from models import review
from models.base_model import BaseModel, Base
from models.review import Review
from datetime import datetime
import pep8


class test_Review(unittest.TestCase):
    """
    Defines a `test_Review` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.review_obj = Review()

    @classmethod
    def tearDownClass(cls):
        del cls.review_obj

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/review.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(review.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(Review.__doc__)

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.review_obj).__dict__)
        self.assertTrue("text" in type(self.review_obj).__dict__)
        self.assertTrue("place_id" in type(self.review_obj).__dict__)
        self.assertTrue("user_id" in type(self.review_obj).__dict__)

    def test_class_inherits_from_BaseModel(self):
        """Tests `Review` inherits from `BaseModel`"""
        self.assertTrue(issubclass(type(self.review_obj), BaseModel))

    def test_class_inherits_from_base(self):
        """Tests `Review` also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.review_obj), Base))

    def test_table_name(self):
        """Tests table name is `reviews`"""
        self.assertEqual(self.review_obj.__tablename__, "reviews")

    def test_attribute_type(self):
        """Test attributes Type"""
        self.assertTrue(type(self.review_obj.__tablename__), str)
        self.assertTrue(type(self.review_obj.text), str)
        self.assertTrue(type(self.review_obj.place_id), str)
        self.assertTrue(type(self.review_obj.user_id), str)

    def test_id_created_updated(self):
        """
        Tests presence of id, created_at and updated_at
        on `Review` objects
        """
        self.assertTrue("id" in self.review_obj.__dict__)
        self.assertTrue("created_at" in self.review_obj.__dict__)
        self.assertTrue("updated_at" in self.review_obj.__dict__)

    def test_type_id_created_updated(self):
        """Tests Types of id, created_at and updated_at"""
        self.assertTrue(type(self.review_obj.id) is str)
        self.assertTrue(type(self.review_obj.created_at) is datetime)
        self.assertTrue(type(self.review_obj.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()
