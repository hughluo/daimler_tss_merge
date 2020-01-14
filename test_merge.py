import unittest
from merge import is_overlapping, merge_interval, merge
from Error import InputError

"""
Unittest of merge.
"""
__author__ = "Yinchi Wexort Luo"
__email__ = "yinchi.luo@gmail.com"


class TestMerge(unittest.TestCase):
    def setUp(self):

        # testcase that not overlap
        self.case0 = ([1, 5], [10, 12])
        self.case0_res = [[1, 5], [10, 12]]
        self.case1 = ([-10, 5], [-100, -11])
        self.case1_res = [[-100, -11], [-10, 5]]

        # testcase that overlap
        self.case2 = ([1, 5], [5, 12])
        self.case2_res = [1, 12]
        self.case3 = ([-10, 5], [-100, -10])
        self.case3_res = [-100, 5]

        # intergrate test
        self.case_long_0 = [[25, 30], [2, 19], [14, 23], [4, 8]]
        self.case_long_0_res = [[2, 23], [25, 30]]
        self.case_long_1 = []
        self.case_long_1_res = []

        # invalid input test
        self.case_invalid_0 = [[25, 30], [2, 19], [23, 14], [4, 8]]
        self.case_invalid_1 = [[25, 30], [2, 19, 18], [23, 14], [4, 8]]

    def test_is_overlapping(self):
        self.assertTrue(not is_overlapping(*self.case0))
        self.assertTrue(not is_overlapping(*self.case1))
        self.assertTrue(is_overlapping(*self.case2))
        self.assertTrue(is_overlapping(*self.case3))

    def test_merge_interval(self):
        self.assertEqual(merge_interval(*self.case2), self.case2_res)
        self.assertEqual(merge_interval(*self.case3), self.case3_res)

    def test_merge(self):
        self.assertEqual(merge(list(self.case0)), self.case0_res)
        self.assertEqual(merge(self.case_long_0), self.case_long_0_res)
        self.assertEqual(merge(self.case_long_1), self.case_long_1_res)
        self.assertRaisesRegex(InputError, "invalid input",
                               merge, self.case_invalid_0)
        self.assertRaisesRegex(InputError, "invalid input",
                               merge, self.case_invalid_1)


if __name__ == '__main__':
    unittest.main()
