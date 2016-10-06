import sys
sys.path.append('../')
import unittest
from progs import digstring_zeroes


class TestFillWithZeroes(unittest.TestCase):
    def testzeroes(self):
        r = digstring_zeroes.digstr(345)
        self.assertEqual(r, '000345')

    def testzeroes1(self):
        r = digstring_zeroes.digstr(345, 7)
        self.assertEqual(r, '000345')

    def testzeroes2(self):
        r = digstring_zeroes.digstr(345, 0)
        self.assertEqual(r, '000345')


