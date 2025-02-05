import unittest
from main import StringCalculator
class TestStringCalculator(unittest.TestCase):
    def test_empty_str(self):
            calculator = StringCalculator()
            self.assertEqual(calculator.add(""), 0)
    