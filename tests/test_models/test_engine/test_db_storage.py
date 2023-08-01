#!/usr/bin/python3
"""A test module for `DBStorage` class"""


import MySQLdb
import pep8
import unittest
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.engine.db_storage import DBStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
class Test_db_storage(unittest.TestCase):
    """
    Defines a `Test_db_storage` test class
    that tests class attributes and methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Defines a setup method that performs a one
        time operation on program startup.
        Initializes all class objects that inherits
        from `BaseModel`.
        """
        cls.storage = DBStorage()
        Base.metadata.create_all(cls.storage.__engine)
        cls.session = sessionmaker(bind=cls.storage.__engine)
        cls.Session = cls.session()
        cls.basemodel = BaseModel(name="Base", duty="parent_class")
        cls.Session.add(cls.basemodel)
        cls.amenity = Amenity(name="Free_Wifi")
        cls.Session.add(cls.amenity)
        cls.review = Review(text="Nice_place")
        cls.Session.add(cls.review)
        cls.city = City(name="Ikeja", state_id=cls.state.id)
        cls.Session.add(cls.city)
        cls.state = State(name="Lagos")
        cls.Session.add(cls.state)
        cls.user = User(email="joe@alx.com", password="betty",
                        first_name="Joe", last_name="Navi")
        cls.Session.add(cls.user)
        cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                          name="Joe", description="Eko-Hotel")
        cls.Session.add(cls.place)
        cls.Session.commit()
        # cls.storage.save()

    def tearDownClass(cls):
        """
        Defines a teardown method that deletes all
        created objects, closes open connection to
        databases at the end of program execution
        """
        cls.storage.delete(cls.basemodel)
        cls.storage.delete(cls.amenity)
        cls.storage.delete(cls.review)
        cls.storage.delete(cls.city)
        cls.storage.delete(cls.state)
        cls.storage.delete(cls.user)
        cls.storage.delete(cls.place)
        cls.storage.save()
        del cls.basemodel
        del cls.amenity
        del cls.review
        del cls.city
        del cls.state
        del cls.user
        del cls.place
        cls.storage.close()
        del cls.storage

    def setUp(self):
        """Creates a usable instance of a class for test"""
        self.cls_obj = DBStorage()
        self.state_obj = DBStorage.all(State)
        self.all_obj = DBStorage.all()

    def tearDown(self):
        """Deletes the usable instance of a class per run"""
        del self.cls_obj
        del self.state_obj
        del self.all_obj

    # @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_pep8(self):
        """Tests pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(pep.total_errors, 0, "fix pep8 errors")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_class_documentation(self):
        """Tests class documentation"""
        self.assertIsNotNone(DBStorage.__doc__)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_class_method_documentation(self):
        """Tests class methods documentation"""
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertIsNotNone(DBStorage.close.__doc__)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_class_attributes(self):
        """Tests class has attributes"""
        self.assertTrue(hasattr(self.cls_obj, "__init__"))
        self.assertTrue(hasattr(self.cls_obj, "all"))
        self.assertTrue(hasattr(self.cls_obj, "new"))
        self.assertTrue(hasattr(self.cls_obj, "save"))
        self.assertTrue(hasattr(self.cls_obj, "delete"))
        self.assertTrue(hasattr(self.cls_obj, "reload"))
        self.assertTrue(hasattr(self.cls_obj, "close"))
        self.assertTrue(hasattr(self.cls_obj, "__engine"))
        self.assertTrue(hasattr(self.cls_obj, "__session"))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_init(self):
        """Tests object created from `DBStorage` is not None"""
        self.assertIsNotNone(self.cls_obj)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_all(self):
        """Tests all method"""
        self.assertIsNotNone(self.state_obj)
        self.assertTrue(type(self.state_obj), dict)
        self.assertEqual(len(self.state_obj), 1)
        self.assertTrue(type(self.all_obj), dict)
        self.assertEqual(len(self.cls_obj), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_class_instance(self):
        """Tests class object is instance of `DBStorage`"""
        self.assertTrue(isinstance(type(self.cls_obj)), DBStorage)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_new(self):
        """Tests new method"""
        self.cls_obj.new(self.state_obj)
        self.assertTrue(self.state_obj in self.cls_obj.new)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_save_and_delete(self):
        """Tests save and delete method"""
        state_obj = State(name="Lagos")
        DBStorage.new(state_obj)
        city_obj = City(name="Ikeja")
        DBStorage.new(city_obj)
        DBStorage.save()
        db = MySQLdb.connect(user=getenv("HBNB_MYSQL_USER"),
                             password=getenv("HBNB_MYSQL_PWD"),
                             host=getenv("HBNB_MYSQL_HOST"),
                             db=getenv("HBNB_MYSQL_DB"))
        query_obj = db.cursor()
        query_obj.execute("SELECT * FROM states WHERE name = 'Lagos'")
        result = query_obj.fetchall()
        self.assertEqual(len(result), 1)
        query_obj.close()
        query_obj = db.cursor()
        query_obj.execute("SELECT * FROM cities WHERE name = 'cities'")
        result = query_obj.fetchall()
        self.assertEqual(len(result), 0)
        query_obj.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_delete_None(self):
        """Tests delete method with None"""
        try:
            DBStorage.delete(None)
        except Exception:
            self.fail

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_reload(self):
        """Tests reload method"""
        DBStorage.reload()
        self.assertTrue(isinstance(DBStorage.__session, Session))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "No DB")
    def test_id_created_at_updated_at(self):
        """
        Tests presence of id, created_at and updated_at
        on instances of child classes
        """
        self.assertIn("id", self.basemodel.__dict__)
        self.assertIn("created_at", self.basemodel.__dict__)
        self.assertIn("updated_at", self.basemodel.__dict__)
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
