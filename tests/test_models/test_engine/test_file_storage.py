#!/usr/bin/python3
"""
The `test_file_storage` module supplies a test class for the `FileStorage`
class.
This implements tests for all class attributes and methods, documentation
tests, and pep8 conformance.
"""


import os
import pep8
import unittest
from os import getenv
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.amenity import Amenity


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
class Test_FileStorage(unittest.TestCase):
    """
    Defines a `Test_FileStorage` class that tests
    all class attributes and methods.
    """

    @classmethod
    def setUpClass(cls):
        """
        Defines a setup class that performs a one time
        operation on program startup
        """
        try:
            os.rename("file.json", "tmp_file.json")
        except IOError:
            pass
        cls.storage = FileStorage()
        cls.base = BaseModel()
        cls.storage.new(cls.base)
        cls.t_base = BaseModel()
        cls.storage.new(cls.t_base)
        cls.state = State()
        cls.storage.new(cls.state)
        cls.city = City()
        cls.storage.new(cls.city)
        cls.review = Review()
        cls.storage.new(cls.review)
        cls.user = User()
        cls.storage.new(cls.user)
        cls.place = Place()
        cls.storage.new(cls.place)
        cls.amenity = Amenity()
        cls.storage.new(cls.amenity)

    @classmethod
    def tearDownClass(cls):
        """
        Defines a method that performs a one time operation
        after execution of all programs
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp_file.json", "file.json")
        except IOError:
            pass
        del cls.base
        del cls.t_base
        del cls.state
        del cls.city
        del cls.review
        del cls.user
        del cls.place
        del cls.amenity

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(pep.total_errors, 0, "fix pep8 error")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_class_documentation(self):
        """Tests documentation for `FileStorage` class"""
        self.assertIsNotNone(FileStorage.__doc__)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_class_methods_doc(self):
        """Tests class methods has documentations"""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_class_attributes_doc(self):
        """Tests class attributes documentation"""
        self.assertTrue(hasattr(self.storage, "all"))
        self.assertTrue(hasattr(self.storage, "new"))
        self.assertTrue(hasattr(self.storage, "save"))
        self.assertTrue(hasattr(self.storage, "reload"))
        self.assertTrue(hasattr(self.storage, "delete"))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_isinstance(self):
        """Tests object is instance of `FileStorage`"""
        self.assertIsInstance(self.storage, FileStorage)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_all(self):
        """Tests all method"""
        result = self.storage.all(self.state)
        self.assertTrue(type(result), dict)
        self.assertIsNotNone(result)
        self.assertTrue("BaseModel." +
                        self.base.id in FileStorage._FileStorage__objects)
        self.assertTrue("State." +
                        self.state.id in FileStorage._FileStorage__objects)
        self.assertTrue("City." +
                        self.city.id in FileStorage._FileStorage__objects)
        self.assertTrue("Review." +
                        self.review.id in FileStorage._FileStorage__objects)
        self.assertTrue("User." +
                        self.user.id in FileStorage._FileStorage__objects)
        self.assertTrue("Place." +
                        self.place.id in FileStorage._FileStorage__objects)
        self.assertTrue("Amenity." +
                        self.amenity.id in FileStorage._FileStorage__objects)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_save(self):
        """Tests save method for presence of instance ids"""
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as file:
            textFile = file.read()
        self.assertTrue("BaseModel." + self.base.id in textFile)
        self.assertTrue("State." + self.state.id in textFile)
        self.assertTrue("City." + self.city.id in textFile)
        self.assertTrue("Review." + self.review.id in textFile)
        self.assertTrue("User." + self.user.id in textFile)
        self.assertTrue("Place." + self.place.id in textFile)
        self.assertTrue("Amenity." + self.amenity.id in textFile)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_reload(self):
        """Tests reload method"""
        self.storage.reload()
        self.assertTrue("BaseModel." +
                        self.base.id in FileStorage._FileStorage__objects)
        self.assertTrue("State." +
                        self.state.id in FileStorage._FileStorage__objects)
        self.assertTrue("City." +
                        self.city.id in FileStorage._FileStorage__objects)
        self.assertTrue("Review." +
                        self.review.id in FileStorage._FileStorage__objects)
        self.assertTrue("User." +
                        self.user.id in FileStorage._FileStorage__objects)
        self.assertTrue("Place." +
                        self.place.id in FileStorage._FileStorage__objects)
        self.assertTrue("Amenity." +
                        self.amenity.id in FileStorage._FileStorage__objects)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_delete(self):
        """Tests delete method"""
        self.storage.save()
        self.storage.delete(self.t_base)
        self.storage.save()
        self.assertNotIn(self.t_base, FileStorage._FileStorage__objects)
        self.assertFalse(self.t_base in FileStorage._FileStorage__objects)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_created_updated_at(self):
        """
        Tests presence created_at, updated_at
        """
        self.assertTrue("created_at", self.storage.__dict__)
        self.assertTrue("updated_at", self.storage.__dict__)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "FileStorage")
    def test_id_created_at_updated_at(self):
        """
        Tests presence of id, created_at and updated_at
        on instances of child classes
        """
        self.assertIn("id", self.base.__dict__)
        self.assertIn("created_at", self.base.__dict__)
        self.assertIn("updated_at", self.base.__dict__)
        self.assertIn("id", self.state.__dict__)
        self.assertIn("created_at", self.state.__dict__)
        self.assertIn("updated_at", self.state.__dict__)
        self.assertIn("id", self.city.__dict__)
        self.assertIn("created_at", self.city.__dict__)
        self.assertIn("updated_at", self.city.__dict__)
        self.assertIn("id", self.review.__dict__)
        self.assertIn("created_at", self.review.__dict__)
        self.assertIn("updated_at", self.review.__dict__)
        self.assertIn("id", self.user.__dict__)
        self.assertIn("created_at", self.user.__dict__)
        self.assertIn("updated_at", self.user.__dict__)
        self.assertIn("id", self.place.__dict__)
        self.assertIn("created_at", self.place.__dict__)
        self.assertIn("updated_at", self.place.__dict__)
        self.assertIn("id", self.amenity.__dict__)
        self.assertIn("created_at", self.amenity.__dict__)
        self.assertIn("updated_at", self.amenity.__dict__)


if __name__ == "__main__":
    unittest.main()
