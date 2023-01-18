#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship('Place',
                              backref='cities',
                              cascade='all, delete, delete-orphan')
        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)
    else:
        name = ''
        state_id = ''
