"""Base Transform for doing basic calls for dwt & idwt based on the dimensions called"""

import numpy as np

from wavelet.transforms.wavelet import Wavelet
from wavelet.util.utility import getExponent
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
        return list(getAllWavelets())

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
        arrHilbert = arrTime
        length = 0
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
        Two Dimension wavelet decomposition based on the levels

        Parameters
        ----------
        matTime : array_like
            input matrix signal in Time domain

        Returns
        -------
        array_like
            coefficients Time domain
        """
        noOfRows = len(matTime)
        noOfCols = len(matTime[0])
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matHilbert = [[0.] * noOfRows] * noOfCols
        matHilbert = np.array(matHilbert).T

        # rows
        for i in range(noOfRows):
            arrTime = [0.] * noOfCols
            for j in range(noOfCols):
                arrTime[j] = matTime[i][j]

            arrHilbert = self.waveDec1(arrTime, levelN)

            for j in range(noOfCols):
                matHilbert[i][j] = arrHilbert[j]

        # cols
        for j in range(noOfCols):
            arrTime = [0.] * noOfRows
            for i in range(noOfRows):
                arrTime[i] = matHilbert[i][j]

            arrHilbert = self.waveDec1(arrTime, levelM)

            for i in range(noOfRows):
                matHilbert[i][j] = arrHilbert[i]

        return matHilbert

    def waveRec2(self, matHilbert):
        """
        Two Dimension wavelet reconstruction based on the levels

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
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matTime = [[0.] * noOfRows] * noOfCols
        matTime = np.array(matTime).T

        # rows
        for j in range(noOfCols):
            arrHilbert = [0.] * noOfRows
            for i in range(noOfRows):
                arrHilbert[i] = matHilbert[i][j]

            arrTime = self.waveRec1(arrHilbert, levelM)

            for i in range(noOfRows):
                matTime[i][j] = arrTime[i]

        # cols
        for i in range(noOfRows):
            arrHilbert = [0.] * noOfCols
            for j in range(noOfCols):
                arrHilbert[j] = matTime[i][j]

            arrTime = self.waveRec1(arrHilbert, levelN)

            for j in range(noOfCols):
                matTime[i][j] = arrTime[j]

        return matTime
