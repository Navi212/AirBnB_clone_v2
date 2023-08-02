#!/usr/bin/python3
"""The `test_city` module supplies a test class `test_City`"""


import unittest
from models import city
from models.base_model import BaseModel, Base
from models.city import City
from datetime import datetime
import pep8


class test_City(unittest.TestCase):
    """
    Defines a `test_City` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.city_obj = City()

    @classmethod
    def tearDownClass(cls):
        del cls.city_obj

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/city.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(city.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(City.__doc__)

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.city_obj).__dict__)
        self.assertTrue("name" in type(self.city_obj).__dict__)
        self.assertTrue("state_id" in type(self.city_obj).__dict__)
        self.assertTrue("places" in type(self.city_obj).__dict__)

    def test_class_inherits_from_BaseModel(self):
        """Tests `City` inherits from `BaseModel`"""
        self.assertTrue(issubclass(type(self.city_obj), BaseModel))

    def test_class_inherits_from_base(self):
        """Tests `City` also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.city_obj), Base))

    def test_table_name(self):
        """Tests table name is `cities`"""
        self.assertEqual(self.city_obj.__tablename__, "cities")

    def test_attribute_type(self):
        """Test attributes Type"""
        self.assertTrue(type(self.city_obj.__tablename__), str)
        self.assertTrue(type(self.city_obj.name), str)
        self.assertTrue(type(self.city_obj.state_id), str)

    def test_id_created_updated(self):
        """
        Tests presence of id, created_at and updated_at
        on `City` objects
        """
        self.assertTrue("id" in self.city_obj.__dict__)
        self.assertTrue("created_at" in self.city_obj.__dict__)
        self.assertTrue("updated_at" in self.city_obj.__dict__)

    def test_type_id_created_updated(self):
        """Tests Types of id, created_at and updated_at"""
        self.assertTrue(type(self.city_obj.id) is str)
        self.assertTrue(type(self.city_obj.created_at) is datetime)
        self.assertTrue(type(self.city_obj.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()
