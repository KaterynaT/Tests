import unittest
from ddt import ddt, data, unpack
import dif_dig


@ddt
class FooTestCase(unittest.TestCase):


    @data(([2, 2, 2, 3], [5, 5, 5, 3], [2,2,2], [5,5,5]),([1, 2, 3, 4], [5, 2, 4, 3], [1], [5]))
    @unpack
    def test_check(self, first_list, second_list, first_output, second_output):
        pass
        self.assertEqual((first_output, second_output), dif_dig.unique_lists(first_list, second_list))