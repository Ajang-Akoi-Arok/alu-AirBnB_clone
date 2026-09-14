#!/usr/bin/python3
"""
This module defines the Amenity class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that represents an amenity.

    Attributes:
        name (str): the name of the amenity.
    """

    name = ""
