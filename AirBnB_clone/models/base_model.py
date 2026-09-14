#!/usr/bin/python3
"""
This module defines the BaseModel class, which is the parent class
of all other model classes in the AirBnB clone project.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    for other classes.

    Attributes:
        id (str): unique identifier generated with uuid4.
        created_at (datetime): the datetime when instance was created.
        updated_at (datetime): the datetime when instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        If kwargs is provided, rebuild the instance from a dictionary.
        Otherwise, create a new instance with a new id and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the string representation of the instance.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with
        the current datetime and save the object to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__
        of the instance, with datetimes converted to ISO strings
        and a __class__ key added.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
