import math

from wavelet.util import decomposeArbitraryLength, scalb


class DiscreteFourierTransform:
    def __init__(self):
        pass

    def dft(self, arrTime):
        m = len(arrTime)
        arrFreq = [0.] * m
        n = m >> 1

        for i in range(n):
            iR = i * 2
            iC = i * 2 + 1

            arg = -2. * math.pi * i / n

            for k in range(n):
                kR = k * 2
                kC = k * 2 + 1

                cos = math.cos(k * arg)
                sin = math.sin(k * arg)

                arrFreq[iR] += arrTime[kR] * cos - arrTime[kC] * sin
                arrFreq[iC] += arrTime[kR] * sin + arrTime[kC] * cos

            arrFreq[iR] /= n
            arrFreq[iC] /= n

        return arrFreq

    def idft(self, arrFreq):
        m = len(arrFreq)
        arrTime = [0.] * m
        n = m >> 1

        for i in range(n):
            iR = i * 2
            iC = 2 * i + 1

            arg = 2. * math.pi * i / n

            for k in range(n):
                kR = k * 2
                kC = k * 2 + 1

                cos = math.cos(k * arg)
                sin = math.sin(k * arg)

                arrTime[iR] += arrFreq[kR] * cos - arrFreq[kC] * sin
                arrTime[iC] += arrFreq[kR] * sin - arrFreq[kC] * cos

        return arrTime

    def decompose(self, arrTime):
        length = len(arrTime)
        powers = decomposeArbitraryLength(length)
        offset = 0
        arrHilbert = list()

        for power in powers:
            index = scalb(1, power)
            arrSliced = arrTime[offset: int(index)]

            arrHilbert.extend(self.dft(arrSliced))

            offset += int(index)

        return arrHilbert

    def reconstruct(self, arrFreq):
        length = len(arrFreq)
        powers = decomposeArbitraryLength(length)
        offset = 0
        arrTime = list()

        for power in powers:
            index = scalb(1, power)
            arrSliced = arrFreq[offset: int(index)]

            arrTime.extend(self.idft(arrSliced))

            offset += int(index)

        return arrTime
