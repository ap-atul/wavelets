"""Utility functions"""

from math import log, pow

import numpy as np

from wavelet.exceptions import WaveletException


def getExponent(value):
    """Returns the exponent for the data Ex: 8 -> 3 [2 ^ 3]"""
    return int(log(value) / log(2.))


def scalb(f, scaleFactor):
    """Return the scale for the factor"""
    return f * pow(2., scaleFactor)


def isPowerOf2(number):
    """Checks if the length is equal to the power of 2"""
    power = getExponent(number)
    result = scalb(1., power)

    return result == number


def decomposeArbitraryLength(number):
    """
    Returns decomposition for the numbers

    Examples
    --------
    number 42 : 32 + 8 + 2
    powers : 5, 3, 1
    """
    if number < 1:
        raise WaveletException("Number should be greater than 1")

    tempArray = list()
    current = number
    position = 0

    while current >= 1.:
        power = getExponent(current)
        tempArray.append(power)
        current = current - scalb(1., power)
        position += 1

    return tempArray[:position]


def threshold(data, value, substitute=0):
    """Soft thresholding"""

    data = np.asarray(data)
    magnitude = np.absolute(data)

    with np.errstate(divide='ignore'):
        # divide by zero okay as np.inf values get clipped, so ignore warning.
        thresholded = (1 - value / magnitude)
        thresholded.clip(min=0, max=None, out=thresholded)
        thresholded = data * thresholded

    if substitute == 0:
        return thresholded
    else:
        cond = np.less(magnitude, value)
        return np.where(cond, substitute, thresholded)


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variability of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
    """
    arr = np.ma.array(arr).compressed()
    med = np.median(arr)
    return np.median(np.abs(arr - med))
