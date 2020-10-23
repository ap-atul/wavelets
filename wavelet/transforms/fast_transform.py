import numpy as np

from wavelet.transforms.base_transform import BaseTransform
from wavelet.util.utility import getExponent


class FastWaveletTransform(BaseTransform):
    def __init__(self, waveletName):
        super().__init__(waveletName)
        self.__wavelet = self.getWaveletDefinition()

    def waveRec(self, arrHilbert):
        arrHilbert = np.array(arrHilbert)
        dimensions = np.ndim(arrHilbert)

        if dimensions == 1:
            level = getExponent(len(arrHilbert))
            return self.waveRec1(arrHilbert, level)
        elif dimensions == 2:
            return self.waveRec2(arrHilbert)

    def waveDec(self, arrTime):
        arrTime = np.array(arrTime)
        dimensions = np.ndim(arrTime)

        if dimensions == 1:
            level = getExponent(len(arrTime))
            return self.waveDec1(arrTime, level)
        elif dimensions == 2:
            return self.waveDec2(arrTime)
