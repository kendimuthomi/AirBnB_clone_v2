#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
