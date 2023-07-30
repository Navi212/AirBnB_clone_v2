#!/usr/bin/python3
""" Review module for the HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Review class to store review information
    Class Attributes:
    __tablename__ : Table named `reviews`
    text          : String input=> text review
    place_id      : represents a foreignkey to the Place.id class/instance
    user_id       : represents a foreignkey to the User.id class/instance
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
