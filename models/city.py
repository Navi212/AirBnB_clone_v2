#!/usr/bin/python3
""" City Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    Class Attributes:
    __tablename__   : Table named `cities`
    name            : String input=> Name of city
    state_id        : id of the state object which is assigned
                      at the time of object creation implicitly
                      by `BaseModel`.
                      Its a ForeignKey to the State.id
    places          : A relationship to the `Place` class or table
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place",
                          cascade="all, delete, delete-orphan",
                          backref="cities")
