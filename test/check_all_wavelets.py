from time import time

from wavelet.fast_transform import FastWaveletTransform
from wavelet.wavelets import getAllWavelets


def run():
    for wavelet in getAllWavelets():
        if wavelet == "haar":
            continue

        WAVELET_NAME = wavelet
        start = time()
        t = FastWaveletTransform(WAVELET_NAME)

        # original data
        data = [1] * 100000

        # decomposition --> reconstruction
        coefficients = t.waveDec(data)
        clean = t.waveRec(coefficients)

        end = time() - start
        print(f"Wavelet {wavelet}")
        print(f"Time taken :: {end} s")
        print()


if __name__:
    run()
