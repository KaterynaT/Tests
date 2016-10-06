import sys
sys.path.append('../')
import unittest
import split_string


class TestSplitFunction(unittest.TestCase):
    def testseparator(self):
        r = split_string.revline("AAA BBB CCC DDD EEE FFF GGG", separator=' ')
        self.assertEqual(r, ['GGG', 'FFF', 'EEE', 'DDD', 'CCC', 'BBB', 'AAA'])

    def testreversedlist(self):
        r = split_string.revline("AAA BBB CCC DDD EEE FFF GGG")
        self.assertEqual(r,['GGG', 'FFF', 'EEE', 'DDD', 'CCC', 'BBB', 'AAA'])

    def testseparator1(self):
        r = split_string.revline("AAA BBB CCC DDD EEE FFF GGG", separator='9')
        self.assertEqual(r, ['GGG', 'FFF', 'EEE', 'DDD', 'CCC', 'BBB', 'AAA'])

