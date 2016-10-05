import unittest
import thirdtask


class TestCheckFile(unittest.TestCase):
    def testcheck(self):
        r = thirdtask.check_files(["thirdtask.py"])
        self.assertEqual(r, ["./thirdtask.py"])

if __name__ == "__main__":
    unittest.main()
