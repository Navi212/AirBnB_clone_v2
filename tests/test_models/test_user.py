#!/usr/bin/python3
"""The `test_user` module supplies a test class `test_User`"""


import unittest
from models import user
from models.base_model import BaseModel, Base
from models.user import User
from datetime import datetime
import pep8


class test_User(unittest.TestCase):
    """
    Defines a `test_User` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.user_obj = User()

    @classmethod
    def tearDownClass(cls):
        del cls.user_obj

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/user.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(user.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(User.__doc__)

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.user_obj).__dict__)
        self.assertTrue("email" in type(self.user_obj).__dict__)
        self.assertTrue("first_name" in type(self.user_obj).__dict__)
        self.assertTrue("last_name" in type(self.user_obj).__dict__)
        self.assertTrue("places" in type(self.user_obj).__dict__)
        self.assertTrue("reviews" in type(self.user_obj).__dict__)

    def test_class_inherits_from_BaseModel(self):
        """Tests `User` inherits from `BaseModel`"""
        self.assertTrue(issubclass(type(self.user_obj), BaseModel))

    def test_class_inherits_from_base(self):
        """Tests `User` also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.user_obj), Base))

    def test_table_name(self):
        """Tests table name is `users`"""
        self.assertEqual(self.user_obj.__tablename__, "users")

    def test_attribute_type(self):
        """Test attributes Type"""
        self.assertTrue(type(self.user_obj.__tablename__), str)
        self.assertTrue(type(self.user_obj.email), str)
        self.assertTrue(type(self.user_obj.password), str)
        self.assertTrue(type(self.user_obj.first_name), str)
        self.assertTrue(type(self.user_obj.last_name), str)

    def test_id_created_updated(self):
        """
        Tests presence of id, created_at and updated_at
        on `User` objects
        """
        self.assertTrue("id" in self.user_obj.__dict__)
        self.assertTrue("created_at" in self.user_obj.__dict__)
        self.assertTrue("updated_at" in self.user_obj.__dict__)

    def test_type_id_created_updated(self):
        """Tests Types of id, created_at and updated_at"""
        self.assertTrue(type(self.user_obj.id) is str)
        self.assertTrue(type(self.user_obj.created_at) is datetime)
        self.assertTrue(type(self.user_obj.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()
