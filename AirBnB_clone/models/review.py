#!/usr/bin/python3
"""
This module defines the Review class which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that represents a review of a place.

    Attributes:
        place_id (str): the id of the Place being reviewed.
        user_id (str): the id of the User who wrote the review.
        text (str): the review text.
    """

    place_id = ""
    user_id = ""
    text = ""
