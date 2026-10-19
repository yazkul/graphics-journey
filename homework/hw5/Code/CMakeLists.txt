cmake_minimum_required(VERSION 3.10)
project(hw5)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(APPLE)
    execute_process(COMMAND brew --prefix OUTPUT_VARIABLE BREW_PREFIX
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
    include_directories(${BREW_PREFIX}/include)
    include_directories(${BREW_PREFIX}/include/eigen3)
    link_directories(${BREW_PREFIX}/lib)

    execute_process(COMMAND brew --prefix opencv OUTPUT_VARIABLE OPENCV_PREFIX
                    OUTPUT_STRIP_TRAILING_WHITESPACE)
    if(OPENCV_PREFIX)
        list(APPEND CMAKE_PREFIX_PATH ${OPENCV_PREFIX})
        include_directories(${OPENCV_PREFIX}/include/opencv5)
        include_directories(${OPENCV_PREFIX}/include/opencv4)
        link_directories(${OPENCV_PREFIX}/lib)
    endif()
endif()
# 不需要 OpenCV
file(GLOB SRC "*.cpp")
add_executable(hw5 ${SRC})
