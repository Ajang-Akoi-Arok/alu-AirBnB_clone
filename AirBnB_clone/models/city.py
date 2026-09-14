#!/usr/bin/python3
"""
This module defines the City class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that represents a city.

    Attributes:
        state_id (str): the id of the State this city belongs to.
        name (str): the name of the city.
    """

    state_id = ""
    name = ""
