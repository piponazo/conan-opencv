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
