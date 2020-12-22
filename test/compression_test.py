import os
from time import time

import numpy as np
import soundfile

from wavelet.compression import VisuShrinkCompressor
from wavelet.fast_transform import FastWaveletTransform
from wavelet.wavelets import getAllWavelets

INPUT_FILE = "/home/atul/Music/fish.wav"
OUTPUT_DIR = "/home/atul/Music/test/"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate
compressor = VisuShrinkCompressor()

for wavelet in getAllWavelets():
    try:

        WAVELET_NAME = wavelet
        t = FastWaveletTransform(WAVELET_NAME)
        outputFileName = os.path.join(OUTPUT_DIR, "test_" + WAVELET_NAME + ".wav")

        with soundfile.SoundFile(outputFileName, "w", samplerate=rate, channels=info.channels) as of:
            start = time()
            for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.10)):  # reading 10 % of duration

                coefficients = t.waveDec(block)

                coefficients = compressor.compress(coefficients)
                print(f"Compression rate :: {compressor.getCompressionRate(coefficients)}")

                # getting the clean signal as in original form and writing to the file
                clean = t.waveRec(coefficients)
                clean = np.asarray(clean)
                of.write(clean)

            end = time()

            print(f"Finished processing with {WAVELET_NAME}")
            print(f"Time taken :: {end - start} s")
            print()

    except:
        print(f"Wavelet {wavelet} died")
        print()
