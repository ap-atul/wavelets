from wavelet import FastWaveletTransform

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)

# original data (ancient decomposition would be applied)
data = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]]

# decomposition --> reconstruction
coefficients = t.waveDec(data)
data = t.waveRec(coefficients)
print(data)
