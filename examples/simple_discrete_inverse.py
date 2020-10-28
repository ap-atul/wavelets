from wavelet import WaveletTransform, getExponent

transform = WaveletTransform(waveletName="db2")
data = [1, 2, 3, 4, 5, 6, 7, 9]

# dwt with max level
coefficients = transform.dwt(data, level=getExponent(len(data)))

# inverse dwt with max level
data = transform.idwt(coefficients, level=len(coefficients))
