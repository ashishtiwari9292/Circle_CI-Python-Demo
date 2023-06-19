import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtraction(self):
        result = self.calculator.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiplication(self):
        result = self.calculator.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_division(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
