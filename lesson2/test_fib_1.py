import unittest
from ddt import ddt, data, unpack
import fib


@ddt
class FooTestCase(unittest.TestCase):


    @data((10, 55),(15,610),(-10, "Fibonacci function works only on positive numbers"))
    @unpack
    def test_check(self, number, output):
        pass
        self.assertEqual((output), fib.fibonacci(number))

