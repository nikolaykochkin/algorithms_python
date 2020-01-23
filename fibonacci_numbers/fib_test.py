import fib
import unittest


class TestFib(unittest.TestCase):
    def test_recursive(self):
        self.assertEqual(fib.fib_recursive(8), 21)


if __name__ == "__main__":
    unittest.main()
