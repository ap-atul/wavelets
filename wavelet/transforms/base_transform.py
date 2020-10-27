"""Base Transform for doing basic calls for dwt & idwt based on the dimensions called"""

import numpy as np

from wavelet.exceptions import WrongLengthsOfData
from wavelet.transforms.wavelet import Wavelet
from wavelet.util import getExponent, isPowerOf2
from wavelet.wavelets import getAllWavelets


class BaseTransform:
    """
    Transform class to call the Discrete Wavelet Transform on select wavelet based on
    the dimensions of the data

    Attributes
    ----------
    __wavelet: Wavelet
        object of the Wavelet class based on the wavelet name
    """

    def __init__(self, waveletName):
        self.__wavelet = Wavelet(waveletName)

    def getWaveletDefinition(self):
        """
        Returns the wavelet definition for the select wavelet

        Returns
        -------
        object
            object of the selected wavelet class
        """
        return self.__wavelet.__wavelet__

    @staticmethod
    def getAllWaveletDefinition():
        """
        Returns the list of all the wavelets implemented

        Returns
        -------
        list
            list of all wavelets
        """
        return getAllWavelets()

    def waveDec1(self, arrTime, level):
        """
        Single Dimension wavelet decomposition based on the levels

        Parameters
        ----------
        arrTime : array_like
            input array signal in Time domain
        level : int
            level for the decomposition power of 2

        Returns
        -------
        array_like
            coefficients Frequency or the Hilbert domain
        """
        length = 0
        arrHilbert = arrTime.copy()
        dataLength = len(arrHilbert)
        transformWaveletLength = self.__wavelet.__wavelet__.__transformWaveletLength__

        while dataLength >= transformWaveletLength and length < level:
            arrTemp = self.__wavelet.dwt(arrHilbert, dataLength)

            arrHilbert[: len(arrTemp)] = arrTemp
            dataLength >>= 1
            length += 1

        return arrHilbert

    def waveRec1(self, arrHilbert, level):
        """
        Single Dimension wavelet reconstruction based on the levels

        Parameters
        ----------
        arrHilbert : array_like
            input array signal in Frequency or the Hilbert domain
        level : int
            level for the decomposition power of 2

        Returns
        -------
        array_like
            coefficients Time domain
        """
        arrTime = arrHilbert.copy()
        dataLength = len(arrTime)
        transformWaveletLength = self.__wavelet.__wavelet__.__transformWaveletLength__
        h = transformWaveletLength

        steps = getExponent(dataLength)
        for _ in range(level, steps):
            h <<= 1

        while len(arrTime) >= h >= transformWaveletLength:
            arrTemp = self.__wavelet.idwt(arrTime, h)

            arrTime[: len(arrTemp)] = arrTemp
            h <<= 1

        return arrTime

    def waveDec2(self, matTime):
        """
        Two Dimension Multi-level wavelet decomposition based on the levels

        Parameters
        ----------
        matTime : array_like
            input matrix signal in Time domain

        Returns
        -------
        array_like
            coefficients Time domain
        """
        # shape
        noOfRows = len(matTime)
        noOfCols = len(matTime[0])

        if not isPowerOf2(noOfRows) or isPowerOf2(noOfCols):
            raise WrongLengthsOfData(WrongLengthsOfData.__cause__)

        # get the levels
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matHilbert = np.zeros(shape=(noOfRows, noOfCols))

        # rows
        for i in range(noOfRows):
            # run the decomposition on the row
            matHilbert[i] = self.waveDec1(matTime[i], levelN)

        # cols
        for j in range(noOfCols):
            # run the decomposition on the col
            matHilbert.T[j] = self.waveDec1(matHilbert.T[j], levelM)

        return matHilbert

    def waveRec2(self, matHilbert):
        """
        Two Dimension Multi-level wavelet reconstruction based on the levels

        Parameters
        ----------
        matHilbert : array_like
            input matrix signal in Frequency or the Hilbert domain

        Returns
        -------
        array_like
            coefficients Time domain
        """
        noOfRows = len(matHilbert)
        noOfCols = len(matHilbert[0])

        # getting the levels
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matHilbert = np.array(matHilbert).T
        matTime = np.zeros(shape=(noOfRows, noOfCols))

        # rows
        for j in range(noOfCols):
            # run the reconstruction on the row
            matTime.T[j] = self.waveRec1(matHilbert[j], levelM)

        # cols
        for i in range(noOfRows):
            # run the reconstruction on the column
            matTime[i] = self.waveRec1(matTime[i], levelN)

        return matTime
