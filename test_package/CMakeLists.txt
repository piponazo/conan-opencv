cmake_minimum_required(VERSION 3.3)
project(OpenCVTest CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if (UNIX)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra")
endif ()

find_package(OpenCV REQUIRED)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_executable(example main.cpp)
target_link_libraries(example PRIVATE opencv_core)

if (opencv_opencl IN_LIST CONAN_LIBS_OPENCV)
    message("Test opencv OpenCL stuff")
    target_compile_definitions(example PRIVATE CV_WITH_OPENCL)
endif()

if (opencv_features2d IN_LIST CONAN_LIBS_OPENCV)
    message("Test features2d OpenCL stuff")
    target_compile_definitions(example PRIVATE CV_WITH_FEATURES2D)
target_link_libraries(example PRIVATE opencv_features2d)
endif()
