#!/usr/bin/python3
""" """


import unittest
from models import base_model
from models.base_model import BaseModel
import unittest
import datetime
import pep8


class test_basemodel(unittest.TestCase):
    """Defines a test class for `BaseModel` attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Calls the init method of the `BaseModel` class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Defines an empty setup method"""
        pass

    def tearDown(self):
        del self.value

    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/base_model.py"])
        self.assertEqual(pep.total_errors, 0, "Fix PEP8: Error")

    def test_module_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(base_model.__doc__)

    def test_class_documentation(self):
        """Tests module documentation"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_class_method_documentation(self):
        """Tests documentations for class methods"""
        self.assertIsNotNone(self.value.__str__.__doc__)
        self.assertIsNotNone(self.value.save.__doc__)
        self.assertIsNotNone(self.value.to_dict.__doc__)
        self.assertIsNotNone(self.value.delete.__doc__)

    def test_class_attributes(self):
        """Tests presence of class attributes"""
        self.assertTrue(hasattr(self.value, "__init__"))
        self.assertTrue(hasattr(self.value, "__str__"))
        self.assertTrue(hasattr(self.value, "save"))
        self.assertTrue(hasattr(self.value, "to_dict"))
        self.assertTrue(hasattr(self.value, "delete"))

    def test_default(self):
        """Tests object of `BaseModel` is Type `BaseModel`"""
        i = self.value()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Tests obj is not dict"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Tests dicts can not contain non-strings as keys"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """Tests the instance method __str__ return value is same"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Tests difference in created_at/updated_at time"""
        i = self.value()
        n = i.to_dict()
        self.assertNotEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Tests dict can not have None type as key/value"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Tests key in object dict"""
        n = {'Name': 'test'}
        new = BaseModel(**n)
        self.assertIn("Name", new.__dict__)

    def test_kwargs_invalid_key(self):
        """Tests for invalid key in object dict"""
        n = {'Name': 'test'}
        new = BaseModel(**n)
        self.assertNotIn("Nam", new.__dict__)

    def test_id_in_obj(self):
        """Tests obj id is string"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_id_created_updated_at(self):
        """Tests created_at in all objects created"""
        new = self.value()
        self.assertIn("created_at", new.__dict__)
        self.assertIn("updated_at", new.__dict__)
        self.assertIn("id", new.__dict__)

    def test_created_at(self):
        """Tests created_at are datetime objects"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Tests updated_at are datetime objects"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_delete(self):
        """Tests delete method on an instance"""
        new = self.value()
        new.delete()
        self.assertNotIn(new, self.value.__dict__)

    def test_save_method(self):
        """
        Tests updated_at of save method and updated_at during
        intantiation are not equal
        """
        new_1 = self.value()
        new_1.save()
        new_2 = self.value()
        self.assertNotEqual(new_1.updated_at, new_2.updated_at)
