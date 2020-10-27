import time
import unittest

import numpy as np

from wavelet.fast_transform import FastWaveletTransform
from wavelet.wavelets import getAllWavelets


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for wavelet in getAllWavelets():
            start = time.time()
            t = FastWaveletTransform(wavelet)
            data = np.random.uniform(0, 1, 1000000)
            t.waveDec(data)
            end = time.time()

            print(f"Time taken {wavelet} :: {end - start} s")
        print()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
