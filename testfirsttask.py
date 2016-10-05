import unittest
import firsttask

class TestSplitFunction(unittest.TestCase):
    def testseparator(self):
        r = firsttask.revline("AAA BBB CCC DDD EEE FFF GGG", separator=' ')
        self.assertEqual(r, ['GGG', 'FFF', 'EEE', 'DDD', 'CCC', 'BBB', 'AAA'])

    def testreversedlist(self):
        r = firsttask.revline("AAA BBB CCC DDD EEE FFF GGG")
        self.assertEqual(r,['GGG', 'FFF', 'EEE', 'DDD', 'CCC', 'BBB', 'AAA'])

if __name__ == "__main__":
    unittest.main()