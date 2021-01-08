from setuptools import setup

setup(
    name='wavelet',
    version='0.0.1',
    author='AP-Atul',
    author_email='atulpatare99@gmail.com',
    packages=['wavelet/',
              'wavelet/exceptions',
              'wavelet/transforms',
              'wavelet/util',
              'wavelet/wavelets/',
              'wavelet/compression'],
    url='https://github.com/AP-Atul/Wavelets',
    license='LICENSE',
    description='Simple and easy to understand implementation of Wavelet Transform',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy"
    ],
)
