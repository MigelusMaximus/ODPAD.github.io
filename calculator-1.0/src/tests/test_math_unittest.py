"""
@file test_math_unittest.py

@brief Tests for math library
"""

import unittest
from builtins import Exception

from src.math_library.math_library import MathLibrary


class MathTests(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(MathLibrary().sum(3, 5), 8, "Expected value: 8")
        self.assertEqual(MathLibrary().sum(23456789, 123456789), 146913578, "Expected value: 146913578 ")
        self.assertEqual(MathLibrary().sum(-10, 5), -5, "Expected value: -5")
        self.assertEqual(MathLibrary().sum(-10, 10), 0, "Expected value: 0")
        self.assertEqual(MathLibrary().sum(10, -10), 0, "Expected value: 0")

        self.assertEqual(MathLibrary().sum(3.5, 5.3), 8.8, "Expected value: 8.8")
        self.assertEqual(round(MathLibrary().sum(-21.81, 1.71), 1), -20.1, "Expected value: -20.10")
        self.assertEqual(MathLibrary().sum(-21.818989898989, 21.818989898989), 0, "Expected value: 0")
        self.assertEqual(MathLibrary().sum(-21.818989898989, -21.818989898989), -43.637979797978, "Expected value: -43.637979797978")
        self.assertEqual(MathLibrary().sum(21.818989898989, -21.818989898989), 0, "Expected value: 0")

    def test_difference(self):
        self.assertEqual(MathLibrary().difference(5, 5), 0, "Expected value: 0")
        self.assertEqual(MathLibrary().difference(5, -5), 10, "Expected value: 10")
        self.assertEqual(MathLibrary().difference(-5, -5), 0, "Expected value: 0")
        self.assertEqual(MathLibrary().difference(0, 0), 0, "Expected value: 0")

        self.assertEqual(MathLibrary().difference(3.5, 6.3), -2.8, "Expected value: -2.8")
        self.assertEqual(MathLibrary().difference(-21.81, 1.71), -23.52, "Expected value: -23.52")
        self.assertEqual(MathLibrary().difference(-21.818989898989, 21.818989898989), -43.637979797978, "Expected value: -43.637979797978")
        self.assertEqual(MathLibrary().difference(-21.818989898989, -21.818989898989), 0, "Expected value: 0")
        self.assertEqual(MathLibrary().difference(21.818989898989, -21.818989898989), 43.637979797978, "Expected value: 43.637979797978")

    def test_multiplication(self):
        self.assertEqual(MathLibrary().multiplication(5, 5), 25, "Expected value: 25")
        self.assertEqual(MathLibrary().multiplication(5, -5), -25, "Expected value: -25")
        self.assertEqual(MathLibrary().multiplication(-5, -5), 25, "Expected value: 25")
        self.assertEqual(MathLibrary().multiplication(-5, 0), 0, "Expected value: 0")
        self.assertEqual(MathLibrary().multiplication(0, 5), 0, "Expected value: 0")

        self.assertEqual(MathLibrary().multiplication(5, 2.5), 12.5, "Expected value: 12.5")
        self.assertEqual(MathLibrary().multiplication(5, -2.5), -12.5, "Expected value: -12.5")
        self.assertEqual(MathLibrary().multiplication(-5, -2.5), 12.5, "Expected value: 12.5")
        self.assertEqual(MathLibrary().multiplication(6.9, 2.5), 17.25, "Expected value: 17.25")
        self.assertEqual(MathLibrary().multiplication(6.9696969, 2.57777), 17.966275577913, "Expected value: 17.966275577913")

    def test_division(self):
        self.assertRaises(Exception, MathLibrary().division(5, 0), "Expected math error")
        self.assertEqual(MathLibrary().division(5, 5), 1, "Expected value: 1")
        self.assertEqual(MathLibrary().division(5, -5), -1, "Expected value: -1")
        self.assertEqual(MathLibrary().division(5, 1), 5, "Expected value: 5")
        self.assertEqual(MathLibrary().division(5, -1), -5, "Expected value: -5")

        self.assertEqual(MathLibrary().division(5, 2), 2.5, "Expected value: 2.5")
        self.assertEqual(MathLibrary().division(5, -2), -2.5, "Expected value: -2.5")
        self.assertEqual(MathLibrary().division(-5, -2), 2.5, "Expected value: 2.5")
        self.assertEqual(MathLibrary().division(10.75, 3), 3.5833333333333335, "Expected value: 3.5833333333333335")
        self.assertEqual(MathLibrary().division(10.75, -3), -3.5833333333333335, "Expected value: -3.5833333333333335")

    def test_Factorial(self):
        self.assertRaises(Exception, MathLibrary().factorial(5.5555))
        self.assertEqual(MathLibrary().factorial(5), 120, "Expected value: 120")
        self.assertEqual(MathLibrary().factorial(-5), -120, "Expected value: -120")
        self.assertEqual(MathLibrary().factorial(0), 1, "Expected value: 1")
        self.assertEqual(MathLibrary().factorial(1), 1, "Expected value: 1")
        self.assertEqual(MathLibrary().factorial(-1), -1, "Expected value: -1")

    def test_powerOF(self):
        self.assertEqual(MathLibrary().powerOf(5, 5), 3125, "Expected value: 3125")
        self.assertEqual(MathLibrary().powerOf(5, 1), 5, "Expected value: 5")
        self.assertEqual(MathLibrary().powerOf(5, 0), 1, "Expected value: 1")
        self.assertEqual(MathLibrary().powerOf(0, 0), 1, "Expected value: 1")
        self.assertEqual(MathLibrary().powerOf(1, 5), 1, "Expected value: 1")

        self.assertEqual(round(MathLibrary().powerOf(2.2, 2), 2), 4.84, "Expected value: 4.84")
        self.assertEqual(MathLibrary().powerOf(2.2, -2), 0.20661157024793386, "Expected value: 0.20661157024793386")
        self.assertEqual(MathLibrary().powerOf(-2.2, -2), 0.20661157024793386, "Expected value: 0.20661157024793386")
        self.assertEqual(round(MathLibrary().powerOf(-2.2, 3), 3), -10.648, "Expected value: -10.648")
        self.assertEqual(MathLibrary().powerOf(2.2159, 3), 10.880540565679, "Expected value: 10.880540565679")

    def test_squareroot(self):
        self.assertRaises(Exception, MathLibrary().squareroot(3, -8), "Expected math error")
        self.assertEqual(MathLibrary().squareroot(2, 4), 2, "Expected value: 2")
        self.assertEqual(MathLibrary().squareroot(2, 5), 2.23606797749979, "Expected value: 2.23606797749979")
        self.assertEqual(MathLibrary().squareroot(-2, 5), 0.4472135954999579, "Expected value: 0.4472135954999579")

        self.assertEqual(MathLibrary().squareroot(2, 2.5), 1.5811388300841898, "Expected value: 1.5811388300841898")
        self.assertEqual(MathLibrary().squareroot(-2, 5.5), 0.4264014327112209, "Expected value: 0.4264014327112209")

    def test_percent(self):
        self.assertEqual(MathLibrary().percent(100, 100), 100, "Expected value: 100")
        self.assertEqual(MathLibrary().percent(-100, 100), -100, "Expected value: -100")
        self.assertEqual(MathLibrary().percent(200, 100), 200, "Expected value: 200")
        self.assertEqual(MathLibrary().percent(200, 10), 20, "Expected value: 20")
        self.assertEqual(MathLibrary().percent(200, 1000), 2000, "Expected value: 2000")
        self.assertEqual(MathLibrary().percent(200, 1000), 2000, "Expected value: 2000")
        self.assertEqual(MathLibrary().percent(200, 0), 0, "Expected value: 0")

        self.assertEqual(MathLibrary().percent(100, 15.5), 15.5, "Expected value: 15.5")
        self.assertEqual(MathLibrary().percent(-100, 15.5), -15.5, "Expected value: -15.5")
        self.assertEqual(MathLibrary().percent(100, 20.1234679), 20.1234679, "Expected value: 20.1234679")
        self.assertEqual(MathLibrary().percent(-100, 20.1234679), -20.1234679, "Expected value: -20.1234679")

    def test_modulo(self):
        self.assertRaises(Exception, MathLibrary().modulo(5, 0), 0, "Expected Error")
        self.assertEqual(MathLibrary().modulo(5, 3), 2, "Expected value: 2")
        self.assertEqual(MathLibrary().modulo(-5, 3), 1, "Expected value: 1")
        self.assertEqual(MathLibrary().modulo(5, -3), -1, "Expected value: 1")
        self.assertEqual(MathLibrary().modulo(-5, -3), -2, "Expected value: -2")
        self.assertEqual(MathLibrary().modulo(0, 1), 0, "Expected value: 0")

        self.assertEqual(MathLibrary().modulo(10.5, 2), 0.5, "Expected value: 0.5")
        self.assertEqual(MathLibrary().modulo(-10.5, 2), 1.5, "Expected value: 1.5")
        self.assertEqual(MathLibrary().modulo(-10.5, -2), -0.5, "Expected value: -0.5")
        self.assertEqual(MathLibrary().modulo(10.56969, 2.56969), 0.29092999999999947, "Expected value: 0.29092999999999947")

    def test_standart_deviation(self):  # TODO
        pass

if __name__ == '__main__':
    unittest.main()
