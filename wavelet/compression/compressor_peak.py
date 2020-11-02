""" Compression using the difference of the max & min data in the signal """

import numpy as np

from wavelet.compression.compressor import Compressor


class CompressorPeak:
    """
    The magnitude calculated will be used to threshold the data signal, the
    output generated would be the compressed signal with zeros that was threhold
    by the algorithm

    Attributes
    ------------
    __max: float
        the maximum value in the data
    __min: float
        the minimum value in the data
    __magnitude: float
        the calculated threshold value
    __compressor: Compressor
        object that performs the compression with the calculated magnitude value
    """

    def __init__(self):
        self.__max = None
        self.__min = None
        self.__magnitude = 0.
        self.__compressor = Compressor()

    def compress(self, data):
        """
        Perform calculation of the magnitude that is the difference of the highest and lowest
        peaks on the input data, this magnitude is then use to the threshold the signal

        Look at the Compressor to see the implementation

        Parameters
        ----------
        data: array_like
            input signal, mostly output of the decomposition process

        Returns
        -------
        array_like
            thresholded signal
        """
        data = np.asanyarray(data)

        self.__max = np.max(data)
        self.__min = np.min(data)
        self.__magnitude = 0.5 * (self.__max - self.__min)

        return self.__compressor.compress(data, self.__magnitude)

    def getCompressionRate(self, data):
        """
        Returns the compression rate of the final data that was thresholded

        Parameters
        ----------
        data: array_like
            data to check the compression rate for

        Returns
        -------
        float
            compression rate in percentage
        """
        return self.__compressor.calculateCompressionRate(data)

    def getMagnitude(self):
        return self.__magnitude
