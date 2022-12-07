#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.place import place_amenity

models = {User, State, City, Place, Review, Amenity}


class DBStorage:
    """
    Database Engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """i
        Starts the DB engine
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, db), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary
        """
        sql_dict = {}
        if cls is None:
            for model in models:
                objects = self.__session.query(model).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    sql_dict[key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = obj.__class__.__name__ + '.' + obj.id
                sql_dict[key] = obj
        return sql_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def reload(self):
        """
        create all tables in the database
        create the current database scoped session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
        call remove() method on the private session attribute (self.__session)
        """
        self.__session.close()
