#!/usr/bin/python3
"""
This module contains unit tests for the City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_inherits_base_model(self):
        """Test that City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_defaults(self):
        """Test the default attributes of City."""
        c = City()
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


if __name__ == "__main__":
    unittest.main()
