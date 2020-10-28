# Wavelets
Python implementation of the Fast Wavelet Transform (FWT) on 1D, 2D, and 3D(soon) input signals/data.
The common wavelets like Haar, and Daubechies is available. 

The code is according to the software development process, so hopefully its user-friendly or
dev-friendly

## Introduction
The simple Wavelet Transform is given by the formula

![formula](https://github.com/AP-Atul/Wavelets/blob/master/img/wt.png)

The fundamental idea of wavelet transforms is that the transformation should allow only changes in time extension, but not shape.
This is affected by choosing suitable basis functions that allow for this.
Changes in the time extension are expected to conform to the corresponding analysis frequency of the basis function.

## API
Dimension implemented (1D, 2D)
Just call  ```waveDec``` for wavelet decomposition for any dim, length array
And ```waveRec``` for wavelet reconstruction for any dim, length array

Note: For n dimension with length not power of 2, you will need to flatten() the array
```np.asarray(data).flatten```

Check the ```examples/``` for some examples on the usage. Refer the html ```docs/```

## Example
1. Wavelet decomposition and reconstruction

```python
from wavelet import FastWaveletTransform

WAVELET_NAME = "db4"
t = FastWaveletTransform(WAVELET_NAME)

# original data
data = [1, 1, 1, 1, 1, 1, 1, 1]

# decomposition --> reconstruction
coefficients = t.waveDec(data)
data = t.waveRec(coefficients)

```

2. Simple discrete transforms

```python
from wavelet import WaveletTransform, getExponent

transform = WaveletTransform(waveletName="db2")
data = [1, 2, 3, 4, 5, 6, 7, 9]

# dwt with max level
coefficients = transform.dwt(data, level=getExponent(len(data)))

# inverse dwt with max level
data = transform.idwt(coefficients, level=len(coefficients))
```
## Applications
(I'll try to provide some examples for this)
1. Audio de-noising by cleaning the noise signal from the coefficients
2. Data cleaning in the sense of Data Mining
3. Data compression
4. Digital Communications
5. Image Processing
6. etc.

## Limitations
The performance can be improved. Help to make it even better by contributing

## Usage
1. Clone the repo
```console
$ git clone https://github.com/AP-Atul/Wavelets.git
```
2. Install the package
```console
python setup.py install
```

