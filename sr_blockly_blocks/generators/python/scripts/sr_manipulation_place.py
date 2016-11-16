from sr_manipulation_msgs.srv import GetPoseByName

rospy.logwarn("Waiting for pose service...")
rospy.wait_for_service("/get_place_location_by_name")

pose_server = rospy.ServiceProxy("/get_place_location_by_name", GetPoseByName)

release_pose = pose_server(text_location_name).pose

place = PlaceSM(selected_grasp, hand_commander, arm_commander, tf_listener, release_pose)
place_outcome = place.execute()
