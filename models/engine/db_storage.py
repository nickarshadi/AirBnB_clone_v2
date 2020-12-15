#!/usr/bin/python3
"""Contains DBSTORAGE Module."""
from os import getenv
from sqlalchemy import create_engine, MetaData
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
	"""Create Database Storage Class."""
	__engine = None
	__session = None
	def __init__(self):
		"""Initialize Storage."""
		self.__engine = create_engine(
			'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

    def all(self, cls=None):
		"""Return all objects of cls."""
