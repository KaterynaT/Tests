import unittest
import quantity


class TestQuantity(unittest.TestCase):
    def testcheck(self):
        r = quantity.products('ring.json')
        self.assertEqual(r, -9)
    #
    # def testcheck(self):
    #     with self.assertRaises(IOError):
    #         r = quantity.products('ring')



