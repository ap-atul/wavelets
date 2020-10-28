"""Maps the wavelet name to the Wavelet Class object"""

from wavelet.exceptions import WaveletImplementationMissing
from wavelet.wavelets import (db2, db3, db4, db5, db6, db7, db8, db9, db10,
                              db11, db12, db13, db14, db15, db16, db17, db18, db19, db20,
                              sym2, sym3, sym4, sym5, sym6, sym7, sym8, sym9, sym10,
                              sym11, sym12, sym13, sym14, sym15, sym16, sym17, sym18, sym19, sym20,
                              haar)

# all wavelets go here
wavelet = {
    "db2": db2.Daubechies2,
    "db3": db3.Daubechies3,
    "db4": db4.Daubechies4,
    "db5": db5.Daubechies5,
    "db6": db6.Daubechies6,
    "db7": db7.Daubechies7,
    "db8": db8.Daubechies8,
    "db9": db9.Daubechies9,
    "db10": db10.Daubechies10,
    "db11": db11.Daubechies11,
    "db12": db12.Daubechies12,
    "db13": db13.Daubechies13,
    "db14": db14.Daubechies14,
    "db15": db15.Daubechies15,
    "db16": db16.Daubechies16,
    "db17": db17.Daubechies17,
    "db18": db18.Daubechies18,
    "db19": db19.Daubechies19,
    "db20": db20.Daubechies20,
    "sym2": sym2.Symlet2,
    "sym3": sym3.Symlet3,
    "sym4": sym4.Symlet4,
    "sym5": sym5.Symlet5,
    "sym6": sym6.Symlet6,
    "sym7": sym7.Symlet7,
    "sym8": sym8.Symlet8,
    "sym9": sym9.Symlet9,
    "sym10": sym10.Symlet10,
    "sym11": sym11.Symlet11,
    "sym12": sym12.Symlet12,
    "sym13": sym13.Symlet13,
    "sym14": sym14.Symlet14,
    "sym15": sym15.Symlet15,
    "sym16": sym16.Symlet16,
    "sym17": sym17.Symlet17,
    "sym18": sym18.Symlet18,
    "sym19": sym19.Symlet19,
    "sym20": sym20.Symlet20,
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
    return list(wavelet.keys())
