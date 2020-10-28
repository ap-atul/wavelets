from wavelet import FastWaveletTransform

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)

# original data
data = [1, 1, 1, 1, 1, 1, 1, 1]
print(data)

# decomposition --> reconstruction
coefficients = t.waveDec(data)
data = t.waveRec(coefficients)
print(data)
