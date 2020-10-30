import cv2
import numpy as np
from matplotlib import pyplot as plt

from wavelet import FastWaveletTransform

inputFile = "/home/atul/Pictures/My/1.jpg"

data = cv2.imread(inputFile)
data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
data = np.array(data)
originalShape = data.shape
data = data.flatten()

transform = FastWaveletTransform("haar")

coefficients = transform.waveDec(data)
coefficients = transform.waveRec(coefficients)

coefficients = np.array(coefficients)
coefficients = coefficients.reshape(originalShape)
plt.imshow(coefficients)
plt.show()
