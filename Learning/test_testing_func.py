from unittest import TestCase
from typing import Union

def divide(dividend: Union[int, float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError('The division by zero!')
    return dividend / divisor


def multiply(*args: Union[int, float]):
    if len(args) == 0:
        raise ValueError('At least one value to multiply')
    total = 1
    for arg in args:
        total *= arg

    return total



class TestFunction(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_on_zero(self):
        self.assertRaises(ValueError, lambda: divide(23,0))
        with self.assertRaises(ValueError):
            divide(24,0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        input = (2,5)
        expected = 10
        self.assertEqual(multiply(*input), expected)