
current_pose = arm_commander.get_current_pose()

current_pose.position.x = float(x_displacement)
current_pose.position.y = float(y_displacement)
current_pose.position.z = float(z_displacement)

arm_commander.move_to_pose_target(current_pose, wait=wait)
