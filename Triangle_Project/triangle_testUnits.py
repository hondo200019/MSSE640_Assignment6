import unittest
from unittest.mock import patch
from triangleIdentifier import triangle

class TestTriangle(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '7', '6', '5', # Scalese Test 1
        '6', '5', '7', # Scalese Test 2
        '5', '7', '6', # Scalese Test 3
        '6', '7', '5', # Scalese Test 4
        '3', '0', '5', # Zero as input
        '7', '7', '7', # Equilateral Triangle
        '3', '1', '3', # Isosceles Triangle
        '2', '3', '5', # Invalid Triangle with non-zero lengths
        '1', '1', '1', # 1-1-1 Equilateral Triangle
        '0.3', '0.8', '0.8', # Sides less than 1
        '75', '34', '90' # Large Scalene Triangle
    ])
    def test_multiple_units(self, mock_input):
        self.assertEqual(triangle(), 'This is a Scalene Triangle')
        print("Testing Scalese Triangle with inputs: 7, 6, 5")
        self.assertEqual(triangle(), 'This is a Scalene Triangle')
        print("Testing Scalese Triangle with inputs: 6, 5, 7")
        self.assertEqual(triangle(), 'This is a Scalene Triangle')
        print("Testing Scalese Triangle with inputs: 5, 7, 6")
        self.assertEqual(triangle(), 'This is a Scalene Triangle')
        print("Testing Scalese Triangle with inputs: 6, 7, 5")
        self.assertEqual(triangle(), "This triangle is invalid!")
        print("Testing invalid triangle with zero as an input: 3, 0, 5")
        self.assertEqual(triangle(), 'This is an Equilateral Triangle')
        print("Testing Equilateral Triangle with inputs: 7, 7, 7")
        self.assertEqual(triangle(), 'This is an Isosceles Triangle')
        print("Testing Isosceles Triangle with inputs: 3, 1, 3")
        self.assertEqual(triangle(), "This triangle is invalid!")
        print("Testing invalid triangle with inputs: 2, 3, 5 (does not satisfy triangle inequality)")
        self.assertEqual(triangle(), 'This is an Equilateral Triangle')
        print("Testing a 1-1-1 Equilateral Triangle")
        self.assertEqual(triangle(), 'This is an Isosceles Triangle')
        print("Testing a valid triangle with side lengths less than 1")
        self.assertEqual(triangle(), 'This is a Scalene Triangle')
        print("Testing large valid triangle")
        


if __name__ == '__main__' :
    unittest.main()