#!/usr/bin/python3
"""Defines the file storage class"""

import json
from models.base_model import BaseModel
from models.user import user
from models.state import state
from models.city import city
from models.place import place
from models.amenity import amenity
from models.review import review

class FileStorage:
    """
    Defines a file storage module for serializing instances to a JSON file and deserializing JSON files to instances
    
    Attributes:
        __file__path (str): name of the file to save objects to
        __objects (dict): Dictionary of instantiated objects
    """

    __file__path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects 
        
        Returns:
            A dictionary containing all objects
        """

        return self.__objects
    
    def new(self, obj):
        """Set in __objects obj with key
        
        Args:
            obj: Object to be added
        """

        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """Serializes the object to a JSON file
        JSON file pathis specified by __file__path
        """
        
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file__path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
       """
       Deserializes the JSON file and updates the objects dictionary.
       If the JSON file (__file_path) exists it reads the file and loads objects.
       If the file doesn't exist, it does nothing.
       """

       try:
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass


