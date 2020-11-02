from wavelet import FastWaveletTransform
from wavelet.compression import CompressorMagnitude

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)
c = CompressorMagnitude()

# original data
data = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

# decomposition --> reconstruction
coefficients = t.waveDec2(data)
coefficients = c.compress(coefficients)
print(f"Compression rate :: {c.getCompressionRate(coefficients)}")
data = t.waveRec2(coefficients)
print("Result :: ")
print(data)
