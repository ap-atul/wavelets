import unittest

import numpy as np

from wavelet.fast_transform import FastWaveletTransform
from wavelet.wavelets import getAllWavelets


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for wavelet in getAllWavelets():
            t = FastWaveletTransform(wavelet)

            data = np.random.uniform(0, 5, 100000)

            coefficients = t.waveDec(data)

            clean = t.waveRec(coefficients)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
