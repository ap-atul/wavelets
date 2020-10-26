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


## Limitations
The performance is not that good. Help to make it even better by contributing

## Usage
1. Clone the repo
```console
$ git clone https://github.com/AP-Atul/Wavelets.git
```
2. Run the run.py file
```console
$ python run.py
```

