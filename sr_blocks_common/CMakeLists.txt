cmake_minimum_required(VERSION 2.8.3)

set(sr_blocks_common_EXTRAS_DIR ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

project(sr_blocks_common)

find_package(catkin REQUIRED)

catkin_package()

include(${sr_blocks_common_EXTRAS_DIR}/cat.cmake)
include(${sr_blocks_common_EXTRAS_DIR}/blockly.cmake)

install(DIRECTORY cmake DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/cmake)