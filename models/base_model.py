#!/usr/bin/python3
"""Defines the BaseModel"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represenst the BaseModel for the AirBnB Project"""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel
        Args:
            *args: (won't be used) positional argument list
            **kwargs: key word arguments
        """

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updtaed = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisofformat(value)
                else:
                    self.__dict__[key] = value
                    
        else:
            models.storage.new(self)
    
    def __str__(self):
        """Sets/Provides the string representation"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def save(self):
        """Updates updated_at timestamp to reflect changes"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Converts model data into a dictionary format for serialzation"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict



