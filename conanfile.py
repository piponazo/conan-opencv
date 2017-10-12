import os
from conans import ConanFile, tools, CMake

class OpenCVConan(ConanFile):
    """
    This recipe generates OpenCV with a classical setup that is useful for most of the cases.
    If you want to experiment with additional features use the provided options.

    This recipe requires conan 0.25.1 (At least)
    """
    name = 'OpenCV'
    version = '3.3.0'
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'OpenCV recipe for the opencv repository'
    url = 'https://github.com/piponazo/conan-opencv'
    source_url = 'https://github.com/opencv/opencv.git'
    license = 'MIT'
    generators = 'cmake'

    options = {
        'opencv_core': [True, False],
        'opencv_features2d': [True, False], # features2d depends on ml and flann
        'opencv_flann': [True, False],
        'opencv_ml': [True, False],
        'opencv_video': [True, False],
        'opencv_imgproc': [True, False],
        'opencv_calib3d': [True, False],    # calib3d needs features2d and imgproc
        'opencv_highgui': [True, False],    # high_gui depends on imgcodecs & videoio
        'opencv_imgcodecs': [True, False],
        'opencv_videoio': [True, False],
        'opencv_shape': [True, False],
        'opencv_objdetect': [True, False],
        'opencv_photo': [True, False],
        'opencv_stitching': [True, False],
        'precompiled_headers': [True, False],
        'shared': [True, False],
    }

    default_options = 'opencv_core=True', \
        'opencv_features2d=True', \
        'opencv_flann=True', \
        'opencv_ml=True', \
        'opencv_video=False', \
        'opencv_imgproc=True', \
        'opencv_calib3d=True', \
        'opencv_highgui=True', \
        'opencv_imgcodecs=True', \
        'opencv_videoio=True', \
        'opencv_shape=False', \
        'opencv_objdetect=False', \
        'opencv_photo=False', \
        'opencv_stitching=False', \
        'precompiled_headers=True', \
        'shared=False'

    def source(self):
        self.run('git clone --depth 1 --branch %s %s' % (self.version, self.source_url))

    def build(self):
        build_path = 'build'
        os.makedirs(build_path)

        tools.replace_in_file("opencv/CMakeLists.txt",
            "project(OpenCV CXX C)",
            """project(OpenCV CXX C)
               include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
               conan_basic_setup()""")

        cmake = CMake(self, parallel=True)
        cmake_args = {
            'CMAKE_CONFIGURATION_TYPES' : self.settings.build_type,
            'CMAKE_BUILD_TYPE' : self.settings.build_type,
            'BUILD_SHARED_LIBS' : 'ON',
            'BUILD_PACKAGE' : 'OFF',
            'BUILD_PERF_TESTS' : 'OFF',
            'BUILD_TESTS' : 'OFF',
            'BUILD_DOCS' : 'OFF',
            'BUILD_WITH_DEBUG_INFO' : 'OFF',
            'BUILD_EXAMPLES' : 'OFF',
            'BUILD_SHARED_LIBS' : self.options.shared,

            'BUILD_opencv_apps' : 'OFF',
            'BUILD_opencv_calib3d': self.options.opencv_calib3d,
            'BUILD_opencv_core': self.options.opencv_core,
            'BUILD_opencv_dnn': 'OFF',
            'BUILD_opencv_features2d': self.options.opencv_features2d,
            'BUILD_opencv_flann': self.options.opencv_flann,
            'BUILD_opencv_highgui': self.options.opencv_highgui,
            'BUILD_opencv_imgcodecs': self.options.opencv_imgcodecs,
            'BUILD_opencv_imgproc': self.options.opencv_imgproc,
            'BUILD_opencv_ml': self.options.opencv_ml,
            'BUILD_opencv_objdetect': self.options.opencv_objdetect,
            'BUILD_opencv_photo': self.options.opencv_photo,
            'BUILD_opencv_shape': self.options.opencv_shape,
            'BUILD_opencv_stitching': self.options.opencv_stitching,
            'BUILD_opencv_superres' : 'OFF',
            'BUILD_opencv_ts' : 'OFF',
            'BUILD_opencv_video': self.options.opencv_video,
            'BUILD_opencv_videoio': self.options.opencv_videoio,
            'BUILD_opencv_videostab' : 'OFF',
            'BUILD_opencv_world' : 'OFF',

            'BUILD_opencv_java' : 'OFF',
            'BUILD_opencv_python2' : 'OFF',
            'BUILD_opencv_python3' : 'OFF',
            'CMAKE_VERBOSE_MAKEFILE' : 'OFF',

            'BUILD_ZLIB' : 'ON',
            'BUILD_PNG' : 'ON',
            'WITH_PNG' : 'ON',
            'WITH_TIFF' : 'ON',
            'WITH_JPEG' : 'ON',
            'WITH_GTK' : 'ON',

            'BUILD_PROTOBUF' : 'OFF',

            'WITH_IPP' : 'OFF',
            'WITH_QT' : 'OFF',
            'WITH_OPENMP' : 'OFF',
            'WITH_WEBP' : 'OFF',
            'WITH_OPENEXR' : 'OFF',
            'WITH_TBB' : 'OFF',
            'WITH_1394' : 'OFF',
            'WITH_CUDA' : 'OFF',
            'WITH_CUFFT' : 'OFF',
            'WITH_OPENCL' : 'OFF',
            'WITH_OPENCLAMDBLAS' : 'OFF',
            'WITH_OPENCLAMDFFT' : 'OFF',
            'WITH_OPENCL_SVM' : 'OFF',
            'WITH_FFMPEG' : 'OFF',
            'WITH_PVAPI' : 'OFF',
            'WITH_GSTREAMER' : 'OFF',
            'WITH_JASPER' : 'OFF',
            'WITH_V4L' : 'OFF',
            'WITH_GIGEAPI' : 'OFF',
            'WITH_GPHOTO2' : 'OFF',
            'WITH_LIBV4L' : 'OFF',
            'WITH_MATLAB' : 'OFF',
            'WITH_VTK' : 'OFF',

            'ENABLE_SSE3' : 'ON',
            'ENABLE_SSE41' : 'ON',
            'ENABLE_SSE42' : 'OFF',
            'ENABLE_SSSE3' : 'ON',
            'ENABLE_PRECOMPILED_HEADERS' : 'ON',

        }

        cmake.configure(source_dir='../opencv', build_dir='build', defs=cmake_args)
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        for option, activated in self.options.items():
            if activated == 'True':
                self.cpp_info.libs.append(option)
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
