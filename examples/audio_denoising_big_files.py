from time import time

import numpy as np
import soundfile

from wavelet import FastWaveletTransform
from wavelet.compression import VisuShrinkCompressor

INPUT_FILE = "/home/atul/Videos/gretel_small.wav"
OUTPUT_FILE = "/home/atul/Videos/gretel_small_denoised.wav"
WAVELET_NAME = "coif1"  # coif1 works vey well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()

start = time()
with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=info.channels) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.1)):  # reading 10 % of duration

        coefficients = t.waveDec(block)
        coefficients = c.compress(coefficients)
        clean = t.waveRec(coefficients)

        clean = np.asarray(clean)
        of.write(clean)

end = time()
print(f"Time taken :: {end - start}")
