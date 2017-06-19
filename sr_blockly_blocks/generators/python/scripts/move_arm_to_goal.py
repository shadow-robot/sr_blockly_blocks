
rospy.sleep(2.0)

current_pose = arm_commander.get_current_pose()
object_transform = result_transforms[object_id]
x = object_transform.translation.x
y = object_transform.translation.y
z = object_transform.translation.z

if dropdown_move is "pre-grasp position":
    z += height + pre_grasp_offset
elif dropdown_move is "grasp position":
    z += height + grasp_offset
elif dropdown_move is "goal":
    x = goal[0]
    y = goal[1]
    z += height + grasp_offset

current_pose.position.x = float(x)
current_pose.position.y = float(y)
current_pose.position.z = float(z)

arm_commander.move_to_pose_target(current_pose)
