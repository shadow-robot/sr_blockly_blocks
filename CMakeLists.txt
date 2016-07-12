cmake_minimum_required(VERSION 2.8.3)
project(sr_blockly_blocks)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs message_generation)

# add_message_files(DIRECTORY msg FILES Floats.msg HeaderString.msg)

# generate_messages(DEPENDENCIES std_msgs)

# catkin_package(CATKIN_DEPENDS std_msgs message_runtime)

# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
# catkin_install_python(PROGRAMS
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/scripts
# )

