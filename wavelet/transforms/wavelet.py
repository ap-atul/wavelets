from wavelet.wavelets import getWaveletDefinition


class Wavelet:
    def __init__(self, waveletName):
        self.__wavelet__ = getWaveletDefinition(waveletName)

    def dwt(self, arrTime, level):
        arrHilbert = [0.] * level
        # shrinking value 8 -> 4 -> 2
        a = level >> 1

        for i in range(a):
            for j in range(self.__wavelet__.__motherWaveletLength__):
                k = (i << 1) + j

                # circulate the array if scale is higher
                while k >= len(arrHilbert):
                    k -= len(arrHilbert)

                arrHilbert[i] += arrTime[k] * self.__wavelet__.decompositionLowFilter[j]
                arrHilbert[i + a] += arrTime[k] * self.__wavelet__.decompositionHighFilter[j]

        return arrHilbert

    def idwt(self, arrHilbert, level):
        arrTime = [0.] * level
        # shrinking value 8 -> 4 -> 2
        a = level >> 1

        for i in range(a):
            for j in range(self.__wavelet__.__motherWaveletLength__):
                k = (i << 1) + j

                # circulating the array if scale is higher
                while k >= len(arrTime):
                    k -= len(arrTime)

                arrTime[k] += (arrHilbert[i] * self.__wavelet__.reconstructionLowFilter[j] +
                               arrHilbert[i + a] * self.__wavelet__.reconstructionHighFilter[j])

        return arrTime
