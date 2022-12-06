#!/usr/bin/python3
"""This module defines a class User"""
<<<<<<< HEAD
from models.base_model import BaseModel
=======
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> e996d60e2e7d37773f51ba3aabe24c3fe2ad3cce
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    places = relationship("Place", backref="user', cascade="delete")
=======
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user', cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """
        inherit from base  and Basemodel init
        """
        super().__init__(*args, **kwargs)
>>>>>>> e996d60e2e7d37773f51ba3aabe24c3fe2ad3cce
