#!/usr/bin/python3
"""
The `test_state` module supplies a test class
`test_State` that tests class attributes, methods,
documentations and pep8 conformance
"""


import unittest
import pep8
from models.base_model import BaseModel, Base
from models.state import State
from models import state
from datetime import datetime


class test_State(unittest.TestCase):
    """
    Defines a `test_State` test class that tests
    class attributes and methods
    """
    @classmethod
    def setUpClass(cls):
        cls.state_obj = State()

    @classmethod
    def tearDownClass(cls):
        del cls.state_obj

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/state.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(state.__doc__)

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(State.__doc__)

    def test_class_inherits_from_BaseModel(self):
        """Tests `Place` inherits from `BaseModel`"""
        self.assertTrue(issubclass(type(self.state_obj), BaseModel))
    
    def test_class_inherits_from_BaseModel(self):
        """Tests `Place` also inherits from `Base` declarative_base"""
        self.assertTrue(issubclass(type(self.state_obj), Base))

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue("__tablename__" in type(self.state_obj).__dict__)
        self.assertTrue("name" in type(self.state_obj).__dict__)
        self.assertTrue("cities" in type(self.state_obj).__dict__)

    def test_id_created_updated(self):
        """
        Tests presence of id, created_at and updated_at
        on `Place` objects
        """
        self.assertTrue("id" in self.state_obj.__dict__)
        self.assertTrue("created_at" in self.state_obj.__dict__)
        self.assertTrue("updated_at" in self.state_obj.__dict__)
    
    def test_type_id_created_updated(self):
        """Tests Types of id, created_at and updated_at"""
        self.assertTrue(type(self.state_obj.id) is str)
        self.assertTrue(type(self.state_obj.created_at) is datetime)
        self.assertTrue(type(self.state_obj.updated_at) is datetime)


if __name__ == "__main__":
    unittest.main()