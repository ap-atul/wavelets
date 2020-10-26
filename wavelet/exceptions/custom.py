"""All custom exceptions"""


class WaveletImplementationMissing(Exception):
    """
    This exception will be raised when unknown wavelet name is provided for
    transform object. When the wavelet implementation is missing
    """
    __cause__ = "The implementation for the requested wavelet is missing!"


class WaveletException(Exception):
    """
    This exception will be raised when something goes wrong with calculations
    or validations with message added at the runtime
    """
    pass
