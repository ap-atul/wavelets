"""Discrete Wavelet and Inverse Transform implementation"""

from wavelet.wavelets import getWaveletDefinition


class WaveletTransform:
    """
    Class to run the selected wavelet and to perform the dwt & idwt
    based on the wavelet filters

    Attributes
    ----------
    __wavelet__: object
        object of the selected wavelet class
    """

    def __init__(self, waveletName):
        self.__wavelet__ = getWaveletDefinition(waveletName)

    def dwt(self, arrTime, level):
        """
        Discrete Wavelet Transform

        Parameters
        ----------
        arrTime : array_like
            input array in Time domain
        level : int
            level to decompose

        Returns
        -------
        array_like
            output array in Frequency or the Hilbert domain
        """
        arrHilbert = [0.] * level
        # shrinking value 8 -> 4 -> 2
        a = level >> 1

        for i in range(a):
            for j in range(self.__wavelet__.__motherWaveletLength__):
                k = (i << 1) + j

                # circulate the array if scale is higher
                while k >= level:
                    k -= level

                # approx & detail coefficient
                arrHilbert[i] += arrTime[k] * self.__wavelet__.decompositionLowFilter[j]
                arrHilbert[i + a] += arrTime[k] * self.__wavelet__.decompositionHighFilter[j]

        return arrHilbert

    def idwt(self, arrHilbert, level):
        """
        Inverse Discrete Wavelet Transform

        Parameters
        ----------
        arrHilbert : array_like
            input array in Frequency or the Hilbert domain
        level : int
            level to decompose

        Returns
        -------
        array_like
            output array in Time domain
        """
        arrTime = [0.] * level
        # shrinking value 8 -> 4 -> 2
        a = level >> 1

        for i in range(a):
            for j in range(self.__wavelet__.__motherWaveletLength__):
                k = (i << 1) + j

                # circulating the array if scale is higher
                while k >= level:
                    k -= level

                # summing the approx & detail coefficient
                arrTime[k] += (arrHilbert[i] * self.__wavelet__.reconstructionLowFilter[j] +
                               arrHilbert[i + a] * self.__wavelet__.reconstructionHighFilter[j])

        return arrTime
