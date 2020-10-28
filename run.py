import numpy as np

from wavelet import FastWaveletTransform

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)

# original data
data = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

# for performing the ancient egyptian decomposition
data = np.asarray(data).flatten()

# decomposition --> reconstruction
coefficients = t.waveDec(np.asarray(data).flatten())
data = t.waveRec(coefficients)
print(data)
