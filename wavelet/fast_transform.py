"""Fast Wavelet Transform calls the Base Transform based on the dimensions"""

import numpy as np

from wavelet.transforms import BaseTransform
from wavelet.util import isPowerOf2, decomposeArbitraryLength, scalb, getExponent


class FastWaveletTransform(BaseTransform):
    """
    Reads the dimensions of the input signal and calls
    the respective functions of the Base Transform class
    """

    def __init__(self, waveletName):
        super().__init__(waveletName)

    def waveRec(self, arrHilbert, level=None):
        """
        Wavelet Reconstruction

        Parameters
        ----------
        level: int
            level for reconstruction
        arrHilbert: array_like
            input array in the Hilbert domain

        Returns
        -------
        array_like
            Time domain
        """
        arrHilbert = np.array(arrHilbert, dtype=np.float_)
        dimensions = np.ndim(arrHilbert)

        # setting the max level
        if level is None:
            level = getExponent(len(arrHilbert))

        # checking if the data is not of arbitrary length
        # special cases only for 1D arrays
        if dimensions == 1 and not isPowerOf2(len(arrHilbert)):
            # perform ancient egyptian decomposition
            return self.__waveRecAncientEgyptian(arrHilbert, level)

        # check for arbitrary length of data for 2D arrays
        if dimensions == 2 and not (isPowerOf2(len(arrHilbert[0])) or isPowerOf2(len(arrHilbert))):
            return self.__waveRecAncientEgyptian2(arrHilbert)

        if dimensions == 1:
            return self.waveRec1(arrHilbert, level)

        elif dimensions == 2:
            return self.waveRec2(arrHilbert)

    def waveDec(self, arrTime, level=None):
        """
        Wavelet Decomposition

        Parameters
        ----------
        level: int
            level for decomposition
        arrTime: array_like
            input array in the Time domain

        Returns
        -------
        array_like
            Hilbert domain
        """
        arrTime = np.array(arrTime, dtype=np.float_)
        dimensions = np.ndim(arrTime)

        # setting the max level
        if level is None:
            level = getExponent(len(arrTime))

        # checking if the data is not of arbitrary length
        # special cases only for 1D arrays
        if dimensions == 1 and not isPowerOf2(len(arrTime)):
            # perform ancient egyptian decomposition
            return self.__waveDecAncientEgyptian(arrTime, level)

        # check for arbitrary length of data for 2D arrays
        if dimensions == 2 and not (isPowerOf2(len(arrTime[0])) or isPowerOf2(len(arrTime))):
            return self.__waveDecAncientEgyptian2(arrTime)

        # data of length power of 2
        if dimensions == 1:
            return self.waveDec1(arrTime, level)

        elif dimensions == 2:
            return self.waveDec2(arrTime)

    def __waveDecAncientEgyptian(self, arrTime, level):
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
            arrHilbert.extend(self.waveDec1(arrTimeSliced, level))

            # incrementing the offset
            offset += sliceIndex

        return arrHilbert

    def __waveRecAncientEgyptian(self, arrHilbert, level):
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
            arrTimeSliced = self.waveRec1(arrHilbertSliced, level)
            arrTime.extend(arrTimeSliced)

            # incrementing the offset
            offset += sliceIndex

        return arrTime

    def __waveDecAncientEgyptian2(self, matTime):
        # shape
        noOfRows = len(matTime)
        noOfCols = len(matTime[0])

        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matHilbert = np.zeros(shape=(noOfRows, noOfCols))

        # rows
        for i in range(noOfRows):
            # run the decomposition
            matHilbert[i] = self.__waveDecAncientEgyptian(matTime[i], levelN)

        # cols
        for j in range(noOfCols):
            # run the decomposition
            matHilbert[:, j] = self.__waveDecAncientEgyptian(matHilbert[:, j], levelM)

        return matHilbert

    def __waveRecAncientEgyptian2(self, matHilbert):
        noOfRows = len(matHilbert)
        noOfCols = len(matHilbert[0])

        # getting the levels
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matTime = np.zeros(shape=(noOfRows, noOfCols))

        # rows
        for j in range(noOfCols):
            # run the reconstruction on the row
            matTime[:, j] = self.__waveRecAncientEgyptian(matHilbert[:, j], levelM)

        # cols
        for i in range(noOfRows):
            # run the reconstruction on the column
            matTime[i] = self.__waveRecAncientEgyptian(matTime[i], levelN)

        return matTime
