#!/usr/bin/python3
"""This module defines a class User"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    Class Attributes:
    __tablename__ : Table named `users`
    email         : String input=> users email address
    password      : String input=> users password
    first_name    : String input=> users first name
    last_name     : String input=> users last name
    places        : relationship to the `Place` table/class
    reviews       : relationship to the `Review` table/class
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place",
                          cascade="all, delete, delete-orphan",
                          backref="user")
    reviews = relationship("Review",
                           cascade="all, delete, delete-orphan",
                           backref="user")
