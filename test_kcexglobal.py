# test_kcexglobal.py
"""
Tests for KCEXGlobal module.
"""

import unittest
from kcexglobal import KCEXGlobal

class TestKCEXGlobal(unittest.TestCase):
    """Test cases for KCEXGlobal class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KCEXGlobal()
        self.assertIsInstance(instance, KCEXGlobal)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KCEXGlobal()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
