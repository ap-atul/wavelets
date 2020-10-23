from wavelet.exceptions.custom import WaveletImplementationMissing
from wavelet.wavelets import db4, haar

# all wavelets go here
wavelet = {
    "db4": db4.Daubechies4,
    "haar": haar.Haar
}


def getWaveletDefinition(name):
    if name not in wavelet:
        raise WaveletImplementationMissing(WaveletImplementationMissing.__cause__)
    return wavelet[name]
