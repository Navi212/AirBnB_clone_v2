#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


# Creates a `Base` object that configures our table
# and map class names to tables
Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    Class Attributes:
    id              : Unique id shared thats unique for each
                      object/instance created from any class
                      that inherits from `BaseModel`
    created_at      : Time when an object is created.
                      All classes that inherits from `BaseModel`
                      will have this implicitly
    Updated_at      : Time when an object is updated.
                      All classes that inherits from `BaseModel`
                      will have this implicitly
    """
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            fm = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key in {"created_at", "updated_at"}:
                    kwargs[key] = datetime.strptime(value, fm)
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary['created_at'] = datetime.now().isoformat()
        dictionary['updated_at'] = datetime.now().isoformat()
        if ("_sa_instance_state") in dictionary:
            try:
                del dictionary["_sa_instance_state"]
            except KeyError:
                pass
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage."""
        from models import storage
        storage.delete(self)
