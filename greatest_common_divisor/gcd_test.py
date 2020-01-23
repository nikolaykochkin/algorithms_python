import gcd
import unittest


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd.gcd(18, 35), 1)
        self.assertEqual(gcd.gcd(14159572, 63967072), 4)


if __name__ == '__main__':
    unittest.main()
