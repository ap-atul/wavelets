import numpy as np
import soundfile

from wavelet import threshold, mad
from wavelet.fourier_transform import DiscreteFourierTransform

INPUT_FILE = "/home/atul/Music/fish.wav"
OUTPUT_FILE = "/home/atul/Music/fish_fft.wav"
WAVELET_NAME = "db4"  # coif1 works vey well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate
t = DiscreteFourierTransform()

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

        coefficients = t.decompose(block)

        # VISU Shrink
        sigma = mad(coefficients)
        thresh = sigma * np.sqrt(2 * np.log(len(block)))

        # thresholding using the noise threshold generated
        coefficients = threshold(coefficients, thresh)

        # getting the clean signal as in original form and writing to the file
        clean = t.reconstruct(coefficients)
        clean = np.asarray(clean, dtype=np.float_)
        of.write(clean)
