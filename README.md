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

## Limitations
Since the wavelet transform with the Discrete Wavelet Transform, only works with the power of 2 length data. i.e. 2, 4, 8, 16, 32.
For arbitrary length signal Ancient Egyptian Multiplication can be implemented. (will try it)

## Usage
1. Clone the repo
```console
$ git clone https://github.com/AP-Atul/Wavelets.git
```
2. Run the run.py file
```console
$ python run.py
```

Check the ```examples/``` for some examples on the usage. Refer the html ```docs/```
