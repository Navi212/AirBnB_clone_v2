#!/usr/bin/python3
"""The `state` Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """
    State class contains name and cities
    cities as relationship to 'City' class
    Class Attributes:
    __tablename__ : Table named `states`
    name          : String input=> name of State
    cities        : relationship to the `City` class or table
    """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        name = ''

    @property
    def cities(self):
        """Returns the list of `City` instances
        with `state_id` equals to the current
        """
        cities = list()

        for _id, city in models.storage.all(City).items():
            if city.state_id == self.id:
                cities.append(city)
        return cities
