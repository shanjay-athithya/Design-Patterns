import unittest

# Code and test class in the same file

class Calculator:
    def add_numbers(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_numbers(self):
        self.assertEqual(self.calculator.add_numbers(2, 3), 5)
        self.assertEqual(self.calculator.add_numbers(-1, 1), 0)
        self.assertEqual(self.calculator.add_numbers(0, 0), 0)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
