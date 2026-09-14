#!/usr/bin/python3
"""
This module defines the User class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that represents a user of the AirBnB platform.

    Attributes:
        email (str): the user's email.
        password (str): the user's password.
        first_name (str): the user's first name.
        last_name (str): the user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
