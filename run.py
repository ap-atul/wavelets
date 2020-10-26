import numpy as np

from wavelet.fast_transform import FastWaveletTransform

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)

# original data
data = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

data = np.asarray(data).flatten()

# decomposition --> reconstruction
coefficients = t.waveDec(np.asarray(data).flatten())
data = t.waveRec(coefficients)
print(data)
