#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
<<<<<<< HEAD
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
=======
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
>>>>>>> e996d60e2e7d37773f51ba3aabe24c3fe2ad3cce
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities', cascade="delete")
=======
    """Represents a city for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table cities.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
>>>>>>> e996d60e2e7d37773f51ba3aabe24c3fe2ad3cce
