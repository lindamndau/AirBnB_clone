#!/usr/bin/python3
import models
from datetime import datetime
from uuid import uuid4
""" Parent class BaseModel defines all other common attributes and instance for other classes"""
class BaseModel():
    """ definition of BaseModel class for AirBnB project"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key), '%Y-%m-%dT%H:%M:%S.%f')
                if key == "id":
                    self.id = kwargs.get(key)
                if key == "name":
                    self.name = kwargs.get(key)

        else:
            self.id = id.uuid4()
            self.created_at = datetime.now()
            self.update_at = datetime.now()
            models.storage.new(self)

    @class_method
    def __str__(self):
        """ __str__ method"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))


    @method
    def save(self):
        """ update, update_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

   @method
   def to_dict(self):
       my_dict = self.__dict__.copy()
       my_dict['created_at'] = self.created_at.isoformat()
       my_dict['updated_at'] = self.updated_at.isoformat()
       my_dict['__class__'] = self.__class__.__name__
       return my_dict
