from points_cover import *
from knapsack import *
import unittest


class TestGreedy(unittest.TestCase):
    def test_points_cover(self):
        self.assertEqual(points_cover([[1, 3], [2, 5], [3, 6]]), [3])
        self.assertEqual(points_cover([[4, 7], [1, 3], [2, 5], [5, 6]]), [3, 6])

    def test_knapsack(self):
        self.assertEqual(knapsack(50, [[60, 20], [100, 50], [120, 30]]), 180.000)


if __name__ == '__main__':
    unittest.main()
