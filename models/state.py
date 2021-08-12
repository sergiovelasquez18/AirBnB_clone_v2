#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='State', cascade='all, delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of
            City instances with state_id equals to the current State.id"""
            from models import storage
            new = []
            new_dic = storage.all(City)
            for city in new_dic.value():
                if city.state_id == self.id:
                    new.append(city)
            return new
