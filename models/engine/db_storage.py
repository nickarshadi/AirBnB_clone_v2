#!/usr/bin/python3
"""Contains DBSTORAGE Module."""

import models
from os import getenv
import sqlalchemy
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Create DBStorage class."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the DB Storage object."""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        self.__engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@{}/{},'
                                                 'pool_pre_ping=True'.
                                                 format(HBNB_MYSQL_USER,
                                                        HBNB_MYSQL_PWD,
                                                        HBNB_MYSQL_HOST,
                                                        HBNB_MYSQL_DB))
        if HBNB_ENV == 'test':
            Base.metadata.drop__all(self.__engine)

        def all(self, cls=None):
            """Query on the current database session."""
            new_dict = {}
            for klasse in classes:
                if cls is None or cls is classes[klasse] or cls is klasse:
                    objs = self.__session.query(classes[klasse]).all()
                    for obj in objs:
                        key = obj.__class__.__name__ + '.' + obj.id
                        new_dict[key] = obj
            return new_dict
