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
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """
        Returns the list of City instances with state_id
        equals to the current State.id => This will be the
        FileStorage relationship between State and City
        """
        from models import storage
        city_li = []
        city_objs = storage.all(City).values()
        for obj in city_objs:
            if obj.state_id == self.id:
                city_li.append(obj)
        return (city_li)
