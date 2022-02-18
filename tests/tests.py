import unittest

from src.alg.sorting import *
from src.alg.greedy import *


class AlgTests(unittest.TestCase):

    def test_fastSort(self):
        self.assertEqual(fast_sort([2, 3, 1, 9, 4, 5], False), [9, 5, 4, 3, 2, 1], "Should be [9, 5, 4, 3, 2, 1]")
        self.assertEqual(fast_sort([2, 3, 1, 9, 4, 5], True), [1, 2, 3, 4, 5, 9], "Should be [1, 2, 3, 4, 5, 9]")

    def test_selectSort(self):
        self.assertEqual(select_sort([2, 3, 1, 9, 4, 5], False), [9, 5, 4, 3, 2, 1], "Should be [9, 5, 4, 3, 2, 1]")
        self.assertEqual(select_sort([2, 3, 1, 9, 4, 5], True), [1, 2, 3, 4, 5, 9], "Should be [1, 2, 3, 4, 5, 9]")

    def test_bubbleSort(self):
        self.assertEqual(bubble_sort([2, 3, 1, 9, 4, 5], False), [9, 5, 4, 3, 2, 1], "Should be [9, 5, 4, 3, 2, 1]")
        self.assertEqual(bubble_sort([2, 3, 1, 9, 4, 5], True), [1, 2, 3, 4, 5, 9], "Should be [1, 2, 3, 4, 5, 9]")

    def test_maxActivities(self):
        self.assertEqual(maxActivities([[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]),
                         [[1, 2], [3, 4], [5, 7], [8, 9]], "Should be [[1, 2], [3, 4], [5, 7], [8, 9]]")


if __name__ == '__main__':
    unittest.main()
