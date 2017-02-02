import os
from conans import ConanFile, tools, CMake

class OpenCVConan(ConanFile):
    name = 'OpenCV'
    lib_version = '3.1.0'
    version = '%s-0' % lib_version
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'OpenCV recipe for the opencv repository'
    url = 'https://github.com/piponazo/conan-opencv'
    license = 'MIT'

    def source(self):
        self.run('git clone --depth 1 --branch %s https://github.com/opencv/opencv.git' % self.lib_version)

    def build(self):
        build_path = 'build'
        os.makedirs(build_path)

        cmake = CMake(self.settings)
        cmake_options = ['CMAKE_INSTALL_PREFIX=%s' % self.package_folder,
                         'CMAKE_INSTALL_RPATH="\$ORIGIN/../lib"',
                         'CMAKE_BUILD_TYPE=%s' % self.settings.build_type,
                         'CMAKE_CONFIGURATION_TYPES=%s' % self.settings.build_type,
                         'BUILD_SHARED_LIBS=ON',
                         'BUILD_PACKAGE=OFF',
                         'BUILD_PERF_TESTS=OFF',
                         'BUILD_TESTS=OFF',
                         'BUILD_DOCS=OFF',
                         'WITH_IPP=OFF',
                         'BUILD_WITH_DEBUG_INFO=OFF',
                         'BUILD_EXAMPLES=OFF',
                         'BUILD_opencv_calib3d=ON',
                         'BUILD_opencv_core=ON',
                         'BUILD_opencv_features2d=ON',
                         'BUILD_opencv_flann=ON',
                         'BUILD_opencv_video=ON',
                         'BUILD_opencv_imgcodecs=ON',
                         'BUILD_opencv_imgproc=ON',
                         'BUILD_opencv_ml=ON',
                         'BUILD_opencv_apps=OFF',
                         'BUILD_opencv_shape=OFF',
                         'BUILD_opencv_highgui=OFF',
                         'BUILD_opencv_videoio=OFF',
                         'BUILD_opencv_objdetect=OFF',
                         'BUILD_opencv_photo=OFF',
                         'BUILD_opencv_stitching=OFF',
                         'BUILD_opencv_superres=OFF',
                         'BUILD_opencv_videostab=OFF',
                         'BUILD_opencv_world=OFF',
                         'BUILD_opencv_java=OFF',
                         'BUILD_opencv_python2=OFF',
                         'BUILD_opencv_python3=OFF',
                         'CMAKE_VERBOSE_MAKEFILE=OFF',
                         'WITH_OPENMP=OFF',
                         'WITH_QT=OFF',
                         'WITH_PNG=OFF',
                         'WITH_TIFF=OFF',
                         'WITH_JPEG=OFF',
                         'WITH_WEBP=OFF',
                         'WITH_OPENEXR=OFF',
                         'WITH_TBB=OFF',
                         'WITH_1394=OFF',
                         'WITH_GTK=OFF',
                         'WITH_CUDA=OFF',
                         'WITH_CUFFT=OFF',
                         'WITH_OPENCL=OFF',
                         'WITH_OPENCLAMDBLAS=OFF',
                         'WITH_OPENCLAMDFFT=OFF',
                         'WITH_OPENCL_SVM=OFF',
                         'WITH_FFMPEG=OFF',
                         'WITH_PVAPI=OFF',
                         'WITH_GSTREAMER=OFF',
                         'WITH_JASPER=OFF',
                         'WITH_V4L=OFF',
                         'WITH_OPENCL=OFF',
                         'WITH_OPENCLAMDBLAS=OFF',
                         'WITH_OPENCLAMDFFT=OFF',
                         'WITH_OPENCL_SVM=OFF',
                         'ENABLE_SSE3=ON',
                         'ENABLE_SSE41=ON',
                         'ENABLE_SSE42=ON',
                         'ENABLE_SSSE3=ON',
                         'ENABLE_PRECOMPILED_HEADERS=ON',
                         'WITH_GIGEAPI=OFF',
                         'WITH_GPHOTO2=OFF',
                         'WITH_LIBV4L=OFF',
                         'WITH_MATLAB=OFF',
                         'WITH_VTK=OFF']

        options = '-D' + ' -D'.join(cmake_options)

        config_command = 'cd %s && cmake ../opencv %s %s' % (build_path, cmake.command_line, options)
        self.output.warn(config_command)
        self.run(config_command)

        compile_command = 'cd %s && cmake --build . %s' % (build_path, cmake.build_config)
        if self.settings.os != 'Windows':
            n_cores = tools.cpu_count()
            compile_command = compile_command + ' -- -j%s' % n_cores
        self.output.warn(compile_command)
        self.run(compile_command)

        install_command = 'cd %s && cmake --build . --target install' % build_path
        install_command = install_command + ' --config %s' % (self.settings.build_type)
        self.output.warn(install_command)
        self.run(install_command)

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['opencv_aruco', 'opencv_calib3d', 'opencv_core', 'opencv_features2d', 'opencv_flann'
                              'opencv_imgcodecs', 'opencv_imgproc', 'opencv_ml',
                              'opencv_video'] # The libs to link against

        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
