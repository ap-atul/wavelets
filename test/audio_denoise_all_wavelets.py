import os
from time import time

import numpy as np
import soundfile

from wavelet.fast_transform import FastWaveletTransform
from wavelet.util.utility import threshold, mad
from wavelet.wavelets import getAllWavelets

INPUT_FILE = "/home/atul/Music/fish.wav"
OUTPUT_DIR = "/home/atul/Music/test/"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

for wavelet in getAllWavelets():
    try:

        WAVELET_NAME = wavelet
        t = FastWaveletTransform(WAVELET_NAME)
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

                coefficients = t.waveDec(block)

                # VISU Shrink
                sigma = mad(coefficients)
                thresh = sigma * np.sqrt(2 * np.log(len(block)))

                # thresholding using the noise threshold generated
                coefficients[0:] = threshold(coefficients, thresh)

                # getting the clean signal as in original form and writing to the file
                clean = t.waveRec(coefficients)
                clean = np.asarray(clean)
                of.write(clean)
            end = time()

            print(f"Finished processing with {WAVELET_NAME}")
            print(f"Time taken :: {end - start} s")
            print()
            print()

    except:
        print(f"Wavelet {wavelet} died")
        print()
