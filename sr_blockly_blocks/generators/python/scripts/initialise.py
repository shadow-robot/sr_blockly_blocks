
from sr_robot_commander.sr_arm_commander import SrArmCommander
from sr_robot_commander.sr_hand_commander import SrHandCommander
from sr_robot_commander.sr_robot_commander import SrRobotCommander

if dropdown_commander == 'arm_commander':
    arm_commander = SrArmCommander(set_ground=False)
elif dropdown_commander == 'hand_commander':
    hand_commander = SrHandCommander(name=side + "_hand")
elif dropdown_commander == 'robot_commander':
    robot_commander = SrRobotCommander(name=side + "_arm_and_hand")
elif dropdown_commander == 'hand_h_and_arm':
    robot_commander = SrRobotCommander ("right_arm_and_hand", prefix="H1_")
else:
    arm_commander = SrArmCommander(set_ground=False)
    hand_commander = SrHandCommander(name=side + "_hand")
