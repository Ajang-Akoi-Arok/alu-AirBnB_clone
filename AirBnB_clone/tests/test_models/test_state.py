#!/usr/bin/python3
"""
This module contains unit tests for the State class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_inherits_base_model(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_default_name(self):
        """Test that the default name is an empty string."""
        s = State()
        self.assertEqual(s.name, "")


if __name__ == "__main__":
    unittest.main()
