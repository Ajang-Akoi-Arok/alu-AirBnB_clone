#!/usr/bin/python3
"""
This module defines the State class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that represents a state.

    Attributes:
        name (str): the name of the state.
    """

    name = ""
