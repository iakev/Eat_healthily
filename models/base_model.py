#!/usr/bin/env python
"""Module describing basemodel from which all other models derive from"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime 
from sqlalchemy.orm import DeclarativeBase


time = "%Y-%m-%dT%H:%M:%S.%f"
class Base(DeclarativeBase):
    """metadata class and the base model from which other models derive from"""
    id = Column(String(64), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of base model"""
        if kwargs:
            for k,v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get('id', None) is None:
                self.id = uuid.uuid4()
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
    
    def __str__(self):
        """string representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the 'updated_at' attribute with current datetime and saves instance to db"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary constaining all key values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict.keys():
            del new_dict["_sa_instance_state"]
        return new_dict
    
    def delete(self):
        """delete current instance from database"""
        models.storage.delete(self)
        models.storage.save()
