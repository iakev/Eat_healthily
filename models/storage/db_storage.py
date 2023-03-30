#!/usr/bin/env python
"""Module that describes the dbstorage"""
from models.base_model import Base
from models.consumers import Consumer
from models.farmers import Farmer
from models.farms import Farm, FarmProduce, FarmOperation, FarmProduceOperation
from models.inputs import Input
from models.operations import Operation
from models.products import Produce
from models.users import User
from os import getenv
import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Consumer": Consumer, "Farmer": Farmer, "Produce":Produce,
            "Farm": Farm, "Operation": Operation, 
            "User": User, "Input": Input, "FarmProduce" : FarmProduce, 
            "FarmOperation": FarmOperation, "FarmProduceOperation" : FarmProduceOperation}

class DBStorage:
    """Interacting with MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize a DBStorage object"""
        EH_MYSQL_USER = getenv('EH_MYSQL_USER')
        EH_MYSQL_PWD = getenv('EH_MYSQL_PWD')
        EH_MYSQL_HOST = getenv('EH_MYSQL_HOST')
        EH_MYSQL_DB = getenv('EH_MYSQL_DB')
        EH_ENV = getenv('EH_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                    .format(EH_MYSQL_USER, EH_MYSQL_PWD,
                                    EH_MYSQL_HOST,EH_MYSQL_DB))
    
    def all(self, cls=None):
        """query on current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        """add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj if present from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """returns obj based on class name and id or None"""
        if cls not in classes.values():
            return (None)

        all_cls = self.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return (value)
        
        return (None)

    def count(self, cls=None):
        """returns count of all objects or objects in class specified"""
        if not cls:
            count = 0
            for clss in classes.values():
                count += len(self.all(clss))
        else:
            count += len(self.all(clss)) 

        return (count)     
    
    def query_user_login(self, query_field=None):
        """Performs a query for a user login attempt"""
        user = self.__session.query(User).filter_by(email=query_field).first()
        if not user:
            return (None)
        return (user)
