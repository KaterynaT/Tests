import unittest
import fib


class TestFib(unittest.TestCase):
    def test_fib_numbers_1(self):
        r = fib.fibonacci(10)
        self.assertEqual(r, 55)


    def test_fib_numbers_2(self):
        r = fib.fibonacci(15)
        self.assertEqual(r, 610)


    def test_fib_numbers_3(self):
        r = fib.fibonacci(-10)
        self.assertEqual(r, '"Fibonacci function works only on positive numbers"')

