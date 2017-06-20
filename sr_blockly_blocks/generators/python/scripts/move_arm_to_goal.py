
rospy.sleep(2.0)

grasp_position = None
grasp_id = None
grasp_orienation = None

arm_commander = SrArmCommander(name="right_arm_and_manipulator", set_ground=False)

current_pose = arm_commander.get_current_pose()
object_transform = result_transforms[object_id]

__mapping = rospy.get_param("objects_to_grasp")

for n, grasp_map in enumerate(__mapping):
    object_id_from_yaml = grasp_map["object_id"]
    if object_id_from_yaml == object_id:
        grasp_id = grasp_map["grasp_id"]
        grasp_position = grasp_map["grasp_position"]
        grasp_orientation = grasp_map["grasp_orientation"]
print grasp_position
if grasp_id is not None and grasp_position is not None and grasp_orientation is not None:
    object_transform.translation.x = 0.42
    object_transform.translation.y = 0.88
    object_transform.translation.z = 0.687

    x = object_transform.translation.x + grasp_position[0]
    y = object_transform.translation.y + grasp_position[1]
    z = object_transform.translation.z + grasp_position[2]

    pre_grasp_offset = 0.4

    print dropdown_move

    if dropdown_move is "pre_grasp":
        z += pre_grasp_offset
    elif dropdown_move is "goal":
        x = goal[0]
        y = goal[1]
    print 'z = ', z
    current_pose.position.x = float(x)
    current_pose.position.y = float(y)
    current_pose.position.z = float(z)

    current_pose.orientation.x = float(grasp_orientation[0])
    current_pose.orientation.y = float(grasp_orientation[1])
    current_pose.orientation.z = float(grasp_orientation[2])
    current_pose.orientation.w = float(grasp_orientation[3])
    print current_pose
    arm_commander.move_to_pose_target(current_pose)
else:
    rospy.logerr("Object %s was not found" % object_id)