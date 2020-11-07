import os
from time import time

import numpy as np
import soundfile

from wavelet import FastWaveletTransform
from wavelet.compression import VisuShrinkCompressor

INPUT_FILE = "/home/atul/Music/fish.wav"
OUTPUT_DIR = "/home/atul/Music/"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

WAVELET_NAME = "coif1"
t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()

outputFileName = os.path.join(OUTPUT_DIR, "gretel_" + WAVELET_NAME + ".wav")
with soundfile.SoundFile(outputFileName, "w", samplerate=rate, channels=1) as of:
    start = time()
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.30)):  # reading 10 % of duration

        # processing only single channel
        if block.ndim > 1:
            block = block.T
            block = block[0]
        else:
            block = block.flatten()

        # coefficients = np.fft.fft(block)
        coefficients = t.waveDec(block)
        coefficients = c.compress(coefficients)
        clean = t.waveRec(coefficients)
        # clean = np.fft.ifft(coefficients)

        clean = np.asarray(clean, dtype=np.float_)
        of.write(clean)
    end = time()

    print(f"Finished processing with {WAVELET_NAME}")
    print(f"Time taken :: {end - start} s")
