cmake_minimum_required(VERSION 2.8.3)
project(sr_blockly_blocks)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs message_generation)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ${PROJECT_NAME}
#  CATKIN_DEPENDS moveit_core moveit_msgs moveit_ros_planning roscpp
#  DEPENDS system_lib
)

function(cat IN_FILE OUT_FILE)
  file(READ ${IN_FILE} CONTENTS)
  file(APPEND ${OUT_FILE} "${CONTENTS}")
endfunction()

SET(BLOCKS_UNCOMPRESSED_JS_FILE "blocks_uncompressed.js")
SET(TEMP_BLOCKS_UNCOMPRESSED_JS_FILE "blocks_uncompressed.js.in")

FILE(GLOB_RECURSE PACKAGE_JS_FILES *.js)

FILE(WRITE ${TEMP_BLOCKS_UNCOMPRESSED_JS_FILE}  "")

foreach(PACKAGE_JS_FILE ${PACKAGE_JS_FILES})
  cat(${PACKAGE_JS_FILE} ${TEMP_BLOCKS_UNCOMPRESSED_JS_FILE})
endforeach()

configure_file(${TEMP_BLOCKS_UNCOMPRESSED_JS_FILE} ${CMAKE_CURRENT_SOURCE_DIR}/${BLOCKS_UNCOMPRESSED_JS_FILE} COPYONLY)

install(FILES
  ${BLOCKS_UNCOMPRESSED_JS_FILE}
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
