import unittest

from wavelet.util import decomposeArbitraryLength


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(decomposeArbitraryLength(13), [3, 2, 0])
        self.assertEqual(decomposeArbitraryLength(42), [5, 3, 1])
        self.assertEqual(decomposeArbitraryLength(43), [5, 3, 1, 0])
        self.assertEqual(decomposeArbitraryLength(1000000), [19, 18, 17, 16, 14, 9, 6])


if __name__ == '__main__':
    unittest.main()
