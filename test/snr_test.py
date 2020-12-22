import os
from time import time

import numpy as np
import soundfile
from matplotlib import pyplot as plt

from wavelet.fast_transform import FastWaveletTransform
from wavelet.util.utility import threshold, mad, snr, amp_to_db

INPUT_FILE = "/example/input/file.wav"
OUTPUT_DIR = "/example/output/"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

WAVELET_NAME = "coif1"
t = FastWaveletTransform(WAVELET_NAME)
outputFileName = os.path.join(OUTPUT_DIR, "_" + WAVELET_NAME + ".wav")
noiseRatios = list()

with soundfile.SoundFile(outputFileName, "w", samplerate=rate, channels=info.channels) as of:
    start = time()
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.10)):  # reading 10 % of duration

        coefficients = t.waveDec(block)

        # VISU Shrink
        sigma = mad(coefficients)
        thresh = sigma * np.sqrt(2 * np.log(len(block)))

        # thresholding using the noise threshold generated
        coefficients = threshold(coefficients, thresh)

        # getting the clean signal as in original form and writing to the file
        clean = t.waveRec(coefficients)
        clean = np.asarray(clean)
        of.write(clean)

        noiseRatios.append(snr(amp_to_db(clean)))

    end = time()

    x = []
    for i in range(len(noiseRatios)):
        x.append(i)
    plt.plot(x, np.array(noiseRatios).astype(float))
    plt.show()

    print(f"Finished processing with {WAVELET_NAME}")
    print(f"Time taken :: {end - start} s")
