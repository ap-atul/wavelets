""" Compression using the average of signal as a magnitude """

import numpy as np

from wavelet.compression.compressor import Compressor


class CompressorMagnitude:
    """
    The average of the signal is used to perform the compression on the input
    data signal. Check the Compressor class on how the thresholding is done
    with the magnitude

    Attributes
    ----------
    __magnitude: float
        magnitude calculated using the average of the signal
    __compressor: Compressor
        object to call the compress function using the magnitude calculated

    """

    def __init__(self):
        self.__magnitude = 0.
        self.__compressor = Compressor()

    def compress(self, data):
        """
        Apply thresholding techniques to remove the signal below the magnitude

        Parameters
        ----------
        data: array_like
            input data signal, mostly coefficients output of the decompose

        Returns
        -------
        array_like
            thresholded data/ coefficients
        """
        data = np.asanyarray(data)
        self.__magnitude = np.sum(data.flatten(), axis=0)
        return self.__compressor.compress(data, (self.__magnitude / len(data)))

    def getCompressionRate(self, data):
        """
        Run the compression calculation on the data to check how well the compressor
        performed

        Parameters
        ----------
        data: array_like
            input data from the final step of re-construction

        Returns
        -------
        float
            percentage of the compression
        """
        return self.__compressor.calculateCompressionRate(data)

    def getMagnitude(self):
        """
        Returns the calculated magnitude

        Returns
        -------
        float
            calculated magnitude
        """
        return self.__magnitude
