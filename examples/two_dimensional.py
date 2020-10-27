from wavelet.fast_transform import FastWaveletTransform

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)

# original data
data = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

# decomposition --> reconstruction
coefficients = t.waveDec2(data)
data = t.waveRec2(coefficients)
print(data)
