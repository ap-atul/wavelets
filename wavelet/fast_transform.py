"""Fast Wavelet Transform calls the Base Transform based on the dimensions"""

import os
from multiprocessing import Pool

import numpy as np

from wavelet.transforms.base_transform import BaseTransform
from wavelet.util.utility import getExponent, isPowerOf2, decomposeArbitraryLength, scalb


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
        arrHilbert = np.array(arrHilbert, dtype=np.float_)
        dimensions = np.ndim(arrHilbert)

        # checking if the data is not of arbitrary length
        # special cases only for 1D arrays
        if dimensions == 1 and not isPowerOf2(len(arrHilbert)):
            # perform ancient egyptian decomposition
            return self.__waveRecAncientEgyptian(arrHilbert)

        if dimensions == 1:
            level = getExponent(len(arrHilbert))
            return self.waveRec1(list(arrHilbert), level)
        elif dimensions == 2:
            return self.waveRec2(arrHilbert)

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
        arrTime = np.array(arrTime, dtype=np.float_)
        dimensions = np.ndim(arrTime)

        # checking if the data is not of arbitrary length
        # special cases only for 1D arrays
        if dimensions == 1 and not isPowerOf2(len(arrTime)):
            # perform ancient egyptian decomposition
            return self.__waveDecAncientEgyptian(arrTime)

        # data of length power of 2
        if dimensions == 1:
            level = getExponent(len(arrTime))
            return self.waveDec1(list(arrTime), level)

        elif dimensions == 2:
            return self.waveDec2(arrTime)

    def __waveDecAncientEgyptian(self, arrTime):
        """
        Wavelet decomposition for data of arbitrary length

        References
        ----------
        The array is distributed by the length of the power of 2
        and then wavelet decomposition is performed
        Look into the utility.decomposeArbitraryLength function

        for a data with length 42
        Ex: 42 = 2^5, 2^3, 2^1   i.e. 32, 8, 2 lengths partitions are made

        Parameters
        ----------
        arrTime: array_like
            input array in the time domain

        Returns
        -------
        array_like
            hilbert domain array
        """
        arrHilbert = list()
        powers = decomposeArbitraryLength(len(arrTime))
        offset = 0

        # running for each decomposed array by power
        for power in powers:
            sliceIndex = int(scalb(1., power))
            arrTimeSliced = arrTime[offset: (offset + sliceIndex)]

            # run the wavelet decomposition for the slice
            arrHilbert.extend(self.waveDec(arrTimeSliced))

            # incrementing the offset
            offset += sliceIndex

        return arrHilbert

    def __waveDecAncientEgyptian2(self, arrTime):
        """
        Wavelet decomposition for data of arbitrary length

        References
        ----------
        The array is distributed by the length of the power of 2
        and then wavelet decomposition is performed
        Look into the utility.decomposeArbitraryLength function

        for a data with length 42
        Ex: 42 = 2^5, 2^3, 2^1   i.e. 32, 8, 2 lengths partitions are made

        Parameters
        ----------
        arrTime: array_like
            input array in the time domain

        Returns
        -------
        array_like
            hilbert domain array
        """
        pool = Pool(os.cpu_count())
        powers = decomposeArbitraryLength(len(arrTime))
        offset = 0
        arrHilbert = list()
        arrTimeSliced = list()

        # running for each decomposed array by power
        for power in powers:
            sliceIndex = int(scalb(1., power))
            arrTimeSliced.append(arrTime[offset: (offset + sliceIndex)])

        result = pool.map(self.waveDec, arrTimeSliced)

        [arrHilbert.extend(res) for res in result]

        return arrHilbert

    def __waveRecAncientEgyptian(self, arrHilbert):
        """
        Wavelet reconstruction for data of arbitrary length

        References
        ----------
        The array is distributed by the length of the power of 2
        and then wavelet decomposition is performed
        Look into the utility.decomposeArbitraryLength function

        for a data with length 42
        Ex: 42 = 2^5, 2^3, 2^1   i.e. 32, 8, 2 lengths partitions are made

        Parameters
        ----------
        arrHilbert: array_like
            input array in the hilbert domain

        Returns
        -------
        array_like
            hilbert time array
        """
        arrTime = list()
        powers = decomposeArbitraryLength(len(arrHilbert))
        offset = 0

        # running for each decomposed array by power
        for power in powers:
            sliceIndex = int(scalb(1., power))
            arrHilbertSliced = arrHilbert[offset: (offset + sliceIndex)]

            # run the wavelet decomposition for the slice
            arrTimeSliced = self.waveRec(arrHilbertSliced)
            arrTime.extend(arrTimeSliced)

            # incrementing the offset
            offset += sliceIndex

        return arrTime
