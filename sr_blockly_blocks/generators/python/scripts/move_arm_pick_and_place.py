import geometry_msgs.msg
import copy

rospy.sleep(1.0)

if grasp_pose is not None and release_pose is not None and home_pose is not None and pre_grasp_offset_z is not None:
    arm_goal_pose = geometry_msgs.msg.Pose()
    if dropdown_move is "home":
        rospy.loginfo("Moving arm to home position")
        arm_goal_pose = copy.deepcopy(home_pose)
    elif dropdown_move is "pre_grasp":
        rospy.loginfo("Moving arm to pre-grasp position")
        arm_goal_pose = copy.deepcopy(grasp_pose)
        arm_goal_pose.position.z += pre_grasp_offset_z
    elif dropdown_move is "grasp":
        rospy.loginfo("Moving arm to grasp position")
        arm_goal_pose = copy.deepcopy(grasp_pose)
    elif dropdown_move is "pre_release":
        rospy.loginfo("Moving arm to pre-release position")
        arm_goal_pose = copy.deepcopy(release_pose)
        arm_goal_pose.position.z += pre_grasp_offset_z
    elif dropdown_move is "release":
        rospy.loginfo("Moving arm to release position")
        arm_goal_pose = copy.deepcopy(release_pose)

    arm_commander.plan_to_pose_target(arm_goal_pose)
    if arm_commander.check_plan_is_valid():
        arm_commander.execute()
    else:
        rospy.logerr("Not valid plan found for specified arm pose")
        quit()
else:
    rospy.logerr("Grasp information for object %s was not found" % object_id)
