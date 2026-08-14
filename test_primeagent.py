# test_primeagent.py
"""
Tests for PrimeAgent module.
"""

import unittest
from primeagent import PrimeAgent

class TestPrimeAgent(unittest.TestCase):
    """Test cases for PrimeAgent class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeAgent()
        self.assertIsInstance(instance, PrimeAgent)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeAgent()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
