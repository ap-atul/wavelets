from time import time

import numpy as np
import soundfile

from wavelet import FastWaveletTransform
from wavelet.compression import VisuShrinkCompressor

INPUT_FILE = "/example/input"
OUTPUT_FILE = "/example/output"
WAVELET_NAME = "coif1"  # coif1 works vey well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate
t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()

start = time()
with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=1) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.1)):  # reading 10 % of duration
        # processing only single channel
        if block.ndim > 1:
            print("Multi-Channel Audio")
            block = block.T
            block = block[0]
        else:
            print("Single Channel Audio")
            block = block.flatten()

        # level 1 = 516
        # level 2 = 698
        level = 2
        print(f"Level for transform :: {level}")
        print()
        coefficients = t.waveDec(block, level=level)

        coefficients = c.compress(coefficients)

        clean = t.waveRec(coefficients, level=level)
        clean = np.asarray(clean)
        of.write(clean)
end = time()
print(f"Time taken :: {end - start}")
