import unittest
from main import StringCalculator
class TestStringCalculator(unittest.TestCase):
    def test_empty_str(self):
            calculator = StringCalculator()
            self.assertEqual(calculator.add(""), 0)
    
    def test_single_number(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1"), 1)
        
    def test_number_with_delimiter(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1,2"), 3)
        self.assertEqual(calculator.add("1,2,3"), 6)