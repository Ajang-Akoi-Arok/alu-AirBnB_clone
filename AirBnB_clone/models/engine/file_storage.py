#!/usr/bin/python3
"""
This module defines the FileStorage class which handles
serialization of instances to a JSON file and deserialization
of JSON file to instances.
"""
import json
import os


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON file
    and deserializes JSON file to instances.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): stores all objects by <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file.
        """
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        If the file doesn't exist, do nothing and don't raise exceptions.
        """
        if not os.path.exists(FileStorage.__file_path):
            return

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return

        for key, value in data.items():
            cls_name = value.get("__class__")
            if cls_name in classes:
                obj = classes[cls_name](**value)
                FileStorage.__objects[key] = obj
