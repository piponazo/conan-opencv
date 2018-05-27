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
* Check the CPU features BASELINE/DISTPATCH
* Parallel framework
* Eigen integration
* World
* Add Examples in `test_package` to check that we can use each of the modules enabled
* Intel IPP

# Personal notes

## OpenCL

My personal laptop has a Iris Pro Graphics 5200 and according to this [link](https://software.intel.com/en-us/node/540387)
it should be compatible with OpenCL 1.2.

## CPU Baseline/Dispatch

Read more info about this topic [here](https://github.com/opencv/opencv/wiki/CPU-optimizations-build-options).

We have decided to use the default options.
