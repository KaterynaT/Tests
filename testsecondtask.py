import unittest
import secondtask


class TestFillWithZeroes(unittest.TestCase):
    def testzeroes(self):
        r = secondtask.digstr(345)
        self.assertEqual(r, '000345')

if __name__ == "__main__":
    unittest.main()

