#!/usr/bin/python3
"""The `test_amenity` module supplies a test class `test_Amenity`"""


import unittest
from models import amenity
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from datetime import datetime
import pep8


class test_Amenity(unittest.TestCase):
    """
    Defines a `test_Amenity` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.amenity_obj = Amenity()

    @classmethod
    def tearDownClass(cls):
        del cls.amenity_obj

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/amenity.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(amenity.__doc__)

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.amenity_obj).__dict__)
        self.assertTrue("name" in type(self.amenity_obj).__dict__)
        self.assertTrue("place_amenities" in type(self.amenity_obj).__dict__)

    def test_class_inherits_from_BaseModel(self):
        """Tests Amenity inherits from `BaseModel`"""
        self.assertTrue(issubclass(type(self.amenity_obj), BaseModel))

    def test_class_inherits_from_base(self):
        """Tests Amenity also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.amenity_obj), Base))

    def test_table_name(self):
        """Tests table name is `amenities`"""
        self.assertEqual(self.amenity_obj.__tablename__, "amenities")

    def test_attribute_type(self):
        """Test attributes Type"""
        self.assertTrue(type(self.amenity_obj.name), str)
        self.assertTrue(type(self.amenity_obj.__tablename__), str)

    def test_id_created_updated(self):
        """
        Tests presence of id, created_at and updated_at
        on `Amenity` objects
        """
        self.assertTrue("id" in self.amenity_obj.__dict__)
        self.assertTrue("created_at" in self.amenity_obj.__dict__)
        self.assertTrue("updated_at" in self.amenity_obj.__dict__)

    def test_type_id_created_updated(self):
        """Tests Types of id, created_at and updated_at"""
        self.assertTrue(type(self.amenity_obj.id) is str)
        self.assertTrue(type(self.amenity_obj.created_at) is datetime)
        self.assertTrue(type(self.amenity_obj.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()
