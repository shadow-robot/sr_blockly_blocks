cmake_minimum_required(VERSION 2.8.3)
project(sr_blockly_blocks)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs message_generation sr_blocks_common)

catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ${PROJECT_NAME}
#  CATKIN_DEPENDS moveit_core moveit_msgs moveit_ros_planning roscpp
#  DEPENDS system_lib
)

generate_blockly_js()

install(FILES ${BLOCKS_UNCOMPRESSED_JS_FILE} DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(PROGRAMS src/${PROJECT_NAME}/web_service_module.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
