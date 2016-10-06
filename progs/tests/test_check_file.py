import sys
sys.path.append('../')
import unittest
from progs import check_file


class TestCheckFile(unittest.TestCase):
    def testcheck(self):
        r = check_file.check_files(["test_check_file.py"])
        self.assertEqual(r, ["./test_check_file.py"])

    def testcheck1(self):
        r = check_file.check_files(["test_check_file.py"])
        self.assertEqual(r, [])

