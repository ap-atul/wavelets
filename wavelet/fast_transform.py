"""Fast Wavelet Transform calls the Base Transform based on the dimensions"""

import numpy as np

from wavelet.transforms.base_transform import BaseTransform
from wavelet.util.utility import getExponent


class FastWaveletTransform(BaseTransform):
    """
    Reads the dimensions of the input signal and calls
    the respective functions of the Base Transform class
    """

    def __init__(self, waveletName):
        super().__init__(waveletName)

    def waveRec(self, arrHilbert):
        """
        Wavelet Reconstruction

        Parameters
        ----------
        arrHilbert: array_like
            input array in the Hilbert domain

        Returns
        -------
        array_like
            Time domain
        """
        arrHilbert = np.array(arrHilbert)
        dimensions = np.ndim(arrHilbert)

        if dimensions == 1:
            level = getExponent(len(arrHilbert))
            return self.waveRec1(list(arrHilbert), level)
        elif dimensions == 2:
            return self.waveRec2(list(arrHilbert))

    def waveDec(self, arrTime):
        """
        Wavelet Decomposition

        Parameters
        ----------
        arrTime: array_like
            input array in the Time domain

        Returns
        -------
        array_like
            Hilbert domain
        """
        arrTime = np.array(arrTime)
        dimensions = np.ndim(arrTime)

        if dimensions == 1:
            level = getExponent(len(arrTime))
            return self.waveDec1(list(arrTime), level)
        elif dimensions == 2:
            return self.waveDec2(list(arrTime))
