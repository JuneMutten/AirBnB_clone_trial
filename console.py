#!/usr/bin/python3
"""Defines the HBnB console which is the entry point"""

import cmd 
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State 
from models.city import City  
from models.review import Review 
from shlex import shlex

class HBNBCommand(cmd.Cmd):
    """
    Defines the BnB command interpreter
    
    Attributes:
        prompt(str): The command prompt
    """
    prompt = '(hbnb) '
    class_list = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "Place": Place,
        "State": State,
        "City": City,
        "Reviiew": Review,
        }
    
    def emptyline(self):
        """Doesn't execute anything after receiving an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command that exits the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True
    
    def default (self, arg):
       """Default behaviour for cmd module when input is invalid"""
       arg_dict = {
          "show": self.do_show,
          "destroy": self.do_destroy,
          "all": self.do_all,
          "update": self.do_update
       }
       match = re.search(r"\.", arg)
       if match is not None:
           arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
           match = re.search(r"\((.*?)\)", arg1[1])
           if match is not None:
               command = [arg1[1][:match.span()[0:]], match.group()[1:-1]]
               if command[0] in arg_dict.keys():
                   call = "{} {}".format(arg1[0], command[1])
                   return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
       return False
    
    def do_create(self, class_name):
        """Creates an instance of BaseModel, saves it and prints the id"""
        if not class_name:
            print("** class name missing **")
        elif not self.class_list[class_name]():
            print("** class doesn't exist **")
        else:
          obj = self.class_list[class_name]()
          models.storage.save()
          print(obj.id)

 

     

    



