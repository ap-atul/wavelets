import numpy as np

from wavelet.util.utility import getExponent


class BaseTransform:
    def waveDec(self, arrTime):
        level = getExponent(len(arrTime))
        return self.waveDec1(arrTime, level)

    def waveDec1(self, arrTime, level):
        pass

    def waveRec(self, arrHilbert):
        level = getExponent(len(arrHilbert))
        return self.waveRec1(arrHilbert, level)

    def waveRec1(self, arrHilbert, level):
        pass

    def waveDec2(self, matTime):
        noOfRows = len(matTime)
        noOfCols = len(matTime[0])
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matHilbert = [[0.] * noOfRows] * noOfCols
        matHilbert = np.array(matHilbert)

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
        noOfRows = len(matHilbert)
        noOfCols = len(matHilbert[0])
        levelM = getExponent(noOfRows)
        levelN = getExponent(noOfCols)

        matTime = [[0.] * noOfRows] * noOfCols
        matTime = np.array(matTime)

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
