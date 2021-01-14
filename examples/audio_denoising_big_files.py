from time import time

import numpy as np
import soundfile

from wavelet import FastWaveletTransform
from wavelet.compression import VisuShrinkCompressor
from wavelet.util import snr

INPUT_FILE = "/home/atul/Music/fish.wav"
OUTPUT_FILE = "/home/atul/Music/fish_denoised.wav"
WAVELET_NAME = "coif3"  # coif1 works very well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()
before = list()
after = list()

start = time()
with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=info.channels) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.1)):  # reading 10 % of duration
        coefficients = t.waveDec(block)
        coefficients = c.compress(coefficients)
        clean = t.waveRec(coefficients)
        before.append(snr(block))
        after.append(snr(clean))
        clean = np.asarray(clean)
        of.write(clean)

end = time()
print(f"Time taken :: {end - start}")

print(before)
print(after)
