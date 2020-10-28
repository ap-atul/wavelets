import numpy as np
import soundfile

from wavelet.fast_transform import FastWaveletTransform
from wavelet.util.utility import threshold, mad

INPUT_FILE = "/input.wav"
OUTPUT_FILE = "/output.wav"
WAVELET_NAME = "db4"

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate
t = FastWaveletTransform(WAVELET_NAME)

with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=1) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.10)):  # reading 10 % of duration
        # processing only single channel
        if block.ndim > 1:
            print()
            print("Multi-Channel Audio")
            block = block.T
            block = block[0]
        else:
            print("Single Channel Audio")
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
