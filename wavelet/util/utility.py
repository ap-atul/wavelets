"""Utility functions"""

from math import log


def getExponent(value):
    """
    Returns the exponent for the data length

    Examples
    --------
    >>> getExponent(8)
    3
    >>> getExponent(32)
    5

    Parameters
    ----------
    value : float
        any number

    Returns
    -------
    int
        power of 2
    """
    return int(log(value) / log(2.))
