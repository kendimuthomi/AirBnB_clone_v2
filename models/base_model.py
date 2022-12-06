#!/usr/bin/python3
"""Defines the FileStorage class."""
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is not None:
            new_dictionary = {}
            for key, values in FileStorage.__objects.items():
                #print("Clase: {}".format(cls.__name__))
                if (type(cls) is str):
                    #print("String: {}".format(cls))
                    cls = eval(cls)
                if (cls.__name__ in key):
                    new_dictionary.update({key: values})
            return new_dictionary
        else:
            return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        """serialize the file path to JSON file path
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            return
            pass

    def delete(self, obj=None):
        """ Delete object
        """
        if obj is not None:
            key = (type(obj).__name__) + '.' + obj.__dict__['id']
            del self.__objects[key]

    def close(self):
        """
        call reload() method for deserializing the JSON file to objects
        """
        self.reload()
