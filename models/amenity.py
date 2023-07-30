#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Defines `Amenity` class
    Class Attributes:
    __tablename__   : table named `amenities`
    name            : String input=> Amenity name
    place_amenities : relationship to a `Place` class or table
                      Also points to the `place_amenity` association
                      table between the `Place` and `Amenity`
                      class or tables
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
