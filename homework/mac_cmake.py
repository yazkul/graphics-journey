#!/usr/bin/env python3
"""给 GAMES101 作业目录生成 Mac 可用的 CMakeLists.txt
用法: python3 mac_cmake.py <目录1> <目录2> ...
"""
import os, sys, glob

TEMPLATE = """cmake_minimum_required(VERSION 3.10)
project(%(proj)s)

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
%(opencv)s
file(GLOB SRC "*.cpp")
add_executable(%(proj)s ${SRC})
%(link)s"""

def analyze(d):
    txt = ""
    for f in glob.glob(os.path.join(d, "*.cpp")) + glob.glob(os.path.join(d, "*.hpp")):
        txt += open(f, errors="ignore").read()
    need_cv = "opencv2" in txt
    return need_cv

def main(dirs):
    for d in dirs:
        need_cv = analyze(d)
        rel = os.path.relpath(os.path.abspath(d), os.getcwd()).split(os.sep)[0]
        proj = rel if rel.startswith("hw") else os.path.basename(os.path.abspath(d))
        proj = "".join(c if c.isalnum() or c == "_" else "_" for c in proj)
        if proj[0].isdigit():
            proj = "P" + proj
        open(os.path.join(d, "CMakeLists.txt"), "w").write(TEMPLATE % dict(
            proj=proj,
            opencv="find_package(OpenCV REQUIRED)\ninclude_directories(${OpenCV_INCLUDE_DIRS})" if need_cv else "# 不需要 OpenCV",
            link="target_link_libraries(%s ${OpenCV_LIBS})" % proj if need_cv else "",
        ))
        print("patched:", d, "(opencv=%s)" % need_cv)

if __name__ == "__main__":
    main(sys.argv[1:])
