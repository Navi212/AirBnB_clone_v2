#!/usr/bin/python3
"""The `test_amenity` module supplies a test class `test_Amenity`"""


from models import amenity
from models.base_model import Base
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class test_Amenity(test_basemodel):
    """
    Defines a `test_Amenity` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.class_name = Amenity()

    @classmethod
    def tearDownClass(cls):
        del cls.class_name

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/amenity.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(self.class_name.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(amenity.__doc__)

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.class_name).__dict__)
        self.assertTrue("name" in type(self.class_name).__dict__)
        self.assertTrue("place_amenities" in type(self.class_name).__dict__)

    def test_class_inherits_from_base(self):
        """Tests Amenity also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.class_name), Base))
