#!/usr/bin/python3
"""
The `db_storage` module supplies a class `DBStorage` that
implements a database storage for our class objects
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.base_model import Base


class DBStorage:
    """Defines a database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        mysql_db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, passwd, host, mysql_db), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current database session all objects of
        the given class.
        If cls is None, queries all types of objects.
        Return:
        Dict of queried classes in the format below:
        <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs = objs.extend(self.__session.query(City).all())
            objs = objs.extend(self.__session.query(Review).all())
            objs = objs.extend(self.__session.query(User).all())
            objs = objs.extend(self.__session.query(Amenity).all())
            objs = objs.extend(self.__session.query(Place).all())
            return (objs)
        else:
            obj_dict = {}
            if (type(cls) is str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dict[key] = obj
            return (obj_dict)

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
