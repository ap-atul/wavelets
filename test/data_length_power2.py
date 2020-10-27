import unittest

from wavelet.fast_transform import FastWaveletTransform


class MyTestCase(unittest.TestCase):
    def test_something(self):
        WAVELET_NAME = "db4"
        t = FastWaveletTransform(WAVELET_NAME)

        # original data
        data = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]]

        # decomposition --> reconstruction
        coefficients = t.waveDec(data)
        clean = t.waveRec(coefficients)

        self.assertListEqual(data, list(clean))


if __name__ == '__main__':
    unittest.main()
