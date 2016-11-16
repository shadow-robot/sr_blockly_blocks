from sr_manipulation_grasp_conductor.state_machines import GetGraspSM, GraspApproachSM, GraspSM, RetreatSM

selected_object = text_object_id

grasp_selector = GetGraspSM('coke_can_0', hand_commander)
select_outcome = grasp_selector.execute()

if "failed" == outcome:
    rospy.logerr("Grasp selection failed")
    exit(-1)

selected_grasp = grasp_selector.get_grasp()

approach_grasp = GraspApproachSM(selected_grasp, hand_commander, arm_commander, tf_listener)
approach_outcome = approach_grasp.execute()

if "failed" == outcome:
    rospy.logerr("Grasp approach failed")
    exit(-1)

do_grasp = GraspSM(selected_grasp, hand_commander, arm_commander, tf_listener)
grasp_outcome = do_grasp.execute()

if "failed" == outcome:
    rospy.logerr("Grasp failed")
    exit(-1)

retreat = RetreatSM(selected_grasp, hand_commander, arm_commander, tf_listener)
retreat_outcome = retreat.execute()
