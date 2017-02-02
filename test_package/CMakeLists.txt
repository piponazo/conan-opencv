project(OpenCVTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_set_find_paths()

find_package(OpenCV REQUIRED)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

message("OPENCV_LIBRARY: ${OpenCV_LIBS}")
message("OPENCV_INCLUDE_DIRS: ${OpenCV_INCLUDE_DIRS}")
message("EIGEN_INCLUDE_DIR: ${EIGEN_INCLUDE_DIR}")

add_executable(test main.cpp)
target_link_libraries(test ${OpenCV_LIBS})
target_include_directories(test PRIVATE ${OpenCV_INCLUDE_DIRS})
target_include_directories(test PRIVATE ${EIGEN_INCLUDE_DIR})

set_property(TARGET test PROPERTY CXX_STANDARD 11)

