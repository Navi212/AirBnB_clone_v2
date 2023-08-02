#!/usr/bin/python3
"""
The `test_place` module supplies a test class
`test_Place` that tests class attributes, methods,
documentations and pep8 conformance
"""


import unittest
import pep8
from models.base_model import BaseModel, Base
from models.place import Place
from models import place
from datetime import datetime


class test_Place(unittest.TestCase):
    """
    Defines a `test_Place` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.place_obj = Place()

    @classmethod
    def tearDownClass(cls):
        del cls.place_obj

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/place.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(place.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(Place.__doc__)

    def test_class_inherits_from_BaseModel(self):
        """Tests `Place` inherits from `BaseModel`"""
        self.assertTrue(issubclass(type(self.place_obj), BaseModel))
    
    def test_class_inherits_from_BaseModel(self):
        """Tests `Place` also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.place_obj), Base))

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.place_obj).__dict__)
        self.assertTrue("city_id" in type(self.place_obj).__dict__)
        self.assertTrue("user_id" in type(self.place_obj).__dict__)
        self.assertTrue("name" in type(self.place_obj).__dict__)
        self.assertTrue("description" in type(self.place_obj).__dict__)
        self.assertTrue("number_rooms" in type(self.place_obj).__dict__)
        self.assertTrue("number_bathrooms" in type(self.place_obj).__dict__)
        self.assertTrue("max_guest" in type(self.place_obj).__dict__)
        self.assertTrue("price_by_night" in type(self.place_obj).__dict__)
        self.assertTrue("latitude" in type(self.place_obj).__dict__)
        self.assertTrue("longitude" in type(self.place_obj).__dict__)
        self.assertTrue("amenity_ids" in type(self.place_obj).__dict__)

    def test_id_created_updated(self):
        """
        Tests presence of id, created_at and updated_at
        on `Place` objects
        """
        self.assertTrue("id" in self.place_obj.__dict__)
        self.assertTrue("created_at" in self.place_obj.__dict__)
        self.assertTrue("updated_at" in self.place_obj.__dict__)
    
    def test_type_id_created_updated(self):
        """Tests Types of id, created_at and updated_at"""
        self.assertTrue(type(self.place_obj.id) is str)
        self.assertTrue(type(self.place_obj.created_at) is datetime)
        self.assertTrue(type(self.place_obj.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()