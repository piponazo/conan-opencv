## Package Status

| Bintray | Linux & Mac | Windows | 
|:--------:|:---------:|:-------------:|
|[ ![Download](https://api.bintray.com/packages/piponazo/piponazo/OpenCV%3Apiponazo/images/download.svg) ](https://bintray.com/piponazo/piponazo/OpenCV%3Apiponazo/_latestVersion)|[![Build Status](https://travis-ci.org/piponazo/conan-opencv.svg?branch=3.4-testing)](https://travis-ci.org/piponazo/conan-opencv)|[![Build status](https://ci.appveyor.com/api/projects/status/1jqerfo5583d44wq?svg=true)](https://ci.appveyor.com/project/piponazo/conan-opencv)|


# conan-opencv
Conan recipe for the opencv library (Open Source Computer Vision)

# Known issues

The compilation of opencv with clang-3.9 fails. There is an issue opened in OpenCV about it:
https://github.com/opencv/opencv/issues/8010

It's not clear if it's a defect in OpenCV or a compiler bug. For the moment we disable the compilation of OpenCV with
clang-3.9 from the travis matrix.

# TODO

Investigate the following options:

* OpenCL
* CUDA
* GUI mode: GTK, Win, Mac, GTK, QT
*   - GTK. The dev package brings 120MB of dependencies ...
* Add Examples in `test_package` to check that we can use each of the modules enabled
* Intel IPP

# Personal notes

## OpenCL

My personal laptop has a Iris Pro Graphics 5200 and according to this [link](https://software.intel.com/en-us/node/540387)
it should be compatible with OpenCL 1.2.

## CPU Baseline/Dispatch

Read more info about this topic [here](https://github.com/opencv/opencv/wiki/CPU-optimizations-build-options).

We have decided to use the default options.

## Parallel frameworks

Defaults used in each platform:

In this [link](https://docs.opencv.org/3.4.1/d7/dff/tutorial_how_to_use_OpenCV_parallel_for_.html) you can find more information about how to write parallel algorithms in OpenCV and the different parallel frameworks. For the moment we do not specify anything about the parallel framework to be used. Therefore, OpenCV automatically find a default framework for each platform:

* Linux: pthreads
* Mac OSX: GCD
* Windows: Concurrency