"""Maps the wavelet name to the Wavelet Class object"""

from wavelet.exceptions.custom import WaveletImplementationMissing
from wavelet.wavelets import db4, haar

# all wavelets go here
wavelet = {
    "db4": db4.Daubechies4,
    "haar": haar.Haar
}


def getWaveletDefinition(name):
    """
    Returns the wavelet class

    Parameters
    ----------
    name: str
        name of the wavelet

    Raises
    ------
    WaveletImplementationMissing
        missing wavelet implementation

    Returns
    -------
    object
        object of the wavelet
    """
    if name not in wavelet:
        raise WaveletImplementationMissing(WaveletImplementationMissing.__cause__)
    return wavelet[name]


def getAllWavelets():
    """
    Returns a list of all the implemented/stored wavelets

    Returns
    -------
    list
        list of all the wavelets
    """
    return wavelet.keys()
