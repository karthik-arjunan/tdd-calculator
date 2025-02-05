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
        
    def test_number_with_newline_delimiter(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1\n2,3"), 6)
        
    def test_custom_delimiter(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("//;\n1;2"), 3)
        self.assertEqual(calculator.add("//|\n1|2|3"), 6)
    
    def test_negative_number(self):
        calculator = StringCalculator()
        with self.assertRaises(ValueError) as context:
            calculator.add("-1")
        self.assertEqual(str(context.exception), "negatives not allowed: -1")
        with self.assertRaises(ValueError) as context:
            calculator.add("-1,2,-3")
        self.assertTrue("negative numbers not allowed" in str(context.exception))
        self.assertTrue("-2,-3" in str(context.exception))
        
    
        