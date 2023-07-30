#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity


# Creates a `metadata` object that maps each Table
# foreignkey to their respective remote tables
metadata = Base.metadata


# An association table for many-many relationship
# between the `Place` and `Amenity` class or tables
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """
    A place to stay
    Class Attributes:
    __tablename__   : Table named `places`
    city_id         : A foreignkey to the City.id (Class/instance id)
    user_id         : A foreignkey to the User.id (Class/instance id)
    name            : String Input=> (Name of the place)
    description     : String Input=> Description about the place
    number_rooms    : Int input=> Number of rooms in the place
    number_bathrooms: Int input=> Number of bathrooms in the place
    max_guest       : Int input=> Maximum number of guests allowed
    price_by_night  : Int input=> Price by night of the place
    latitude        : Float input=> latitude of the place
    longitude       : Float input=> longitude of the place
    amenity_ids     : List=> list of amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    # For DB storage
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        reviews = relationship("Review",
                               cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

    # For FileStorage
    else:
        @property
        def reviews(self):
            """
            Returns the list of Review instances with
            place_id equals to the current Place.id
            """
            from models import storage
            review_li = []
            review_objs = storage.all(Review).values()
            for obj in review_objs:
                if obj.place_id == self.id:
                    review_li.append(obj)
            return (review_li)

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the
            attribute amenity_ids that contains all
            Amenity.id linked to the Place
            """
            from models import storage
            amenity_li = []
            amenity_objs = storage.all(Amenity).values()
            for obj in amenity_objs:
                if Amenity.id in Place.amenity_ids:
                    amenity_li.append(obj)
            return (amenity_li)

        @amenities.setter
        def amenities(self, value):
            """
            Handles append method for adding an Amenity.id to
            the attribute amenity_ids
            """
            if (type(value) == Amenity):
                Place.amenity_ids.append(value.id)
