#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if models.storage_t == "db":
        cities = relationship("City", backref="state")

    if models.storage_t != 'db':
        @property
        def cities(self):
            """Return list of city instances related to this state."""
            city_list = []
            all_cities = models.storage.all(City)
