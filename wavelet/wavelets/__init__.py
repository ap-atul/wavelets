from wavelet.exceptions.custom import WaveletImplementationMissing
from wavelet.wavelets import db4

# all wavelets go here
wavelet = {
    "db4": db4.Daubechies4
}


def getWaveletDefinition(name):
    if name not in wavelet:
        raise WaveletImplementationMissing(WaveletImplementationMissing.__cause__)
    return wavelet[name]
