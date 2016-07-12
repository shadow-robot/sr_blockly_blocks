
rospy.sleep(2.0)

current_pose = arm_commander.get_current_pose()

if "x_axis" is dropdown_axis:
    current_pose.position.x += float(text_displacement)
elif "y_axis" is dropdown_axis:
    current_pose.position.y += float(text_displacement)
if "z_axis" is dropdown_axis:
    current_pose.position.z += float(text_displacement)

arm_commander.move_to_pose_target(current_pose)
