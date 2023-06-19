import unittest
import tkinter as tk
from tkinter import messagebox
from main import *

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.calculator = Calculator(self.window)

    def tearDown(self):
        self.window.destroy()

    def test_button_click(self):
        self.calculator.button_click(1)
        self.assertEqual(self.calculator.get_display(), "1")

    def test_button_clear(self):
        self.calculator.button_click(5)
        self.calculator.button_clear()
        self.assertEqual(self.calculator.get_display(), "")

    def test_button_equal(self):
        self.calculator.button_click(2)
        self.calculator.button_click("+")
        self.calculator.button_click(3)
        self.calculator.button_equal()
        self.assertEqual(self.calculator.get_display(), "5")

    def test_add_trig_table(self):
        self.calculator.add_trig_table()
        self.assertEqual(self.calculator.get_display(), "sin(0°) = 0.0\ncos(0°) = 1.0\ntan(0°) = 0.0\n--------------------\n"
                                                     "sin(10°) = 0.1736\ncos(10°) = 0.9848\ntan(10°) = 0.1763\n--------------------\n"
                                                     "sin(20°) = 0.342\ncos(20°) = 0.9397\ntan(20°) = 0.3639\n--------------------\n"
                                                     "sin(30°) = 0.5\ncos(30°) = 0.866\ntan(30°) = 0.5774\n--------------------\n"
                                                     "sin(40°) = 0.6428\ncos(40°) = 0.766\ntan(40°) = 0.8391\n--------------------\n"
                                                     "sin(50°) = 0.766\ncos(50°) = 0.6428\ntan(50°) = 1.1918\n--------------------\n"
                                                     "sin(60°) = 0.866\ncos(60°) = 0.5\ntan(60°) = 1.7321\n--------------------\n"
                                                     "sin(70°) = 0.9397\ncos(70°) = 0.342\ntan(70°) = 2.7475\n--------------------\n"
                                                     "sin(80°) = 0.9848\ncos(80°) = 0.1736\ntan(80°) = 5.6713\n--------------------\n"
                                                     "sin(90°) = 1.0\ncos(90°) = 0.0\ntan(90°) = inf\n--------------------\n")

    def test_calculate_trig_ratio(self):
        self.calculator.button_click("sin(")
        self.calculator.button_click(45)
        self.calculator.button_click(")")
        self.calculator.button_equal()
        self.assertAlmostEqual(float(self.calculator.get_display()), 0.7071, places=4)

if __name__ == '__main__':
    unittest.main()
