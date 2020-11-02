import os
from time import time

import numpy as np
import soundfile
from pywt import wavedec, waverec, threshold

from wavelet.util.utility import mad

INPUT_FILE = "/home/atul/Music/fish.wav"
OUTPUT_DIR = "/home/atul/Music/test/"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

WAVELET_NAME = "sym2"
outputFileName = os.path.join(OUTPUT_DIR, "_" + WAVELET_NAME + ".wav")
with soundfile.SoundFile(outputFileName, "w", samplerate=rate, channels=1) as of:
    start = time()
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.10)):  # reading 10 % of duration

        # processing only single channel
        if block.ndim > 1:
            block = block.T
            block = block[0]
        else:
            block = block.flatten()

        coefficients = wavedec(block, wavelet=WAVELET_NAME)

        # VISU Shrink
        sigma = mad(coefficients[- 1])
        thresh = sigma * np.sqrt(2 * np.log(len(block)))
        print(thresh)

        # thresholding using the noise threshold generated
        coefficients[1:] = (threshold(i, value=thresh, mode='soft') for i in coefficients[1:])

        # getting the clean signal as in original form and writing to the file
        clean = waverec(coefficients, wavelet=WAVELET_NAME)
        clean = np.asarray(clean)
        of.write(clean)
    end = time()

    print(f"Finished processing with {WAVELET_NAME}")
    print(f"Time taken :: {end - start} s")
