#!/usr/bin/python3
"""
This module contains unit tests for the Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_inherits_base_model(self):
        """Test that Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_defaults(self):
        """Test the default attributes of Review."""
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")


if __name__ == "__main__":
    unittest.main()
