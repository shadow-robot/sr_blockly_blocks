from sr_robot_commander.sr_arm_commander import SrArmCommander

arm_commander = SrArmCommander(name=dropdown_arm_group, set_ground=False)
arm_commander.set_max_velocity_scaling_factor(vel_scale)
