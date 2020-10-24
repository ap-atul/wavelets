import math

import soundfile

from wavelet.fast_transform import FastWaveletTransform
from wavelet.util.utility import getExponent

inputFile = "../example/input.wav"
outputFile = "../example/input_denoised.wav"

# reading the input file
data, rate = soundfile.read(inputFile)

# the implementation limit data to the power of 2
expo = getExponent(len(data))
s = math.pow(2, expo)

t = FastWaveletTransform(waveletName='haar')
coefficients = t.waveDec(data[: int(s)])
coefficients = t.waveRec(coefficients)

# writing the reconstructed file
soundfile.write(outputFile, coefficients, rate)
