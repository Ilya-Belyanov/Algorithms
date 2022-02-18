import unittest

from src.alg.sorting import fast_sort, select_sort, bubble_sort
from src.alg.greedy import max_activities


class AlgTests(unittest.TestCase):
    """A dummy docstring."""

    def test_fast_sort(self):
        self.assertEqual(fast_sort([2, 3, 1, 9, 4, 5], False),
                         [9, 5, 4, 3, 2, 1],
                         "Should be [9, 5, 4, 3, 2, 1]")
        self.assertEqual(fast_sort([2, 3, 1, 9, 4, 5], True),
                         [1, 2, 3, 4, 5, 9],
                         "Should be [1, 2, 3, 4, 5, 9]")

    def test_select_sort(self):
        self.assertEqual(select_sort([2, 3, 1, 9, 4, 5], False),
                         [9, 5, 4, 3, 2, 1],
                         "Should be [9, 5, 4, 3, 2, 1]")
        self.assertEqual(select_sort([2, 3, 1, 9, 4, 5], True),
                         [1, 2, 3, 4, 5, 9],
                         "Should be [1, 2, 3, 4, 5, 9]")

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([2, 3, 1, 9, 4, 5], False),
                         [9, 5, 4, 3, 2, 1],
                         "Should be [9, 5, 4, 3, 2, 1]")
        self.assertEqual(bubble_sort([2, 3, 1, 9, 4, 5], True),
                         [1, 2, 3, 4, 5, 9],
                         "Should be [1, 2, 3, 4, 5, 9]")

    def test_max_activities(self):
        self.assertEqual(max_activities([[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]),
                         [[1, 2], [3, 4], [5, 7], [8, 9]],
                         "Should be [[1, 2], [3, 4], [5, 7], [8, 9]]")


if __name__ == '__main__':
    unittest.main()
