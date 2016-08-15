
from sr_robot_commander.sr_arm_commander import SrArmCommander
from sr_robot_commander.sr_hand_commander import SrHandCommander

if dropdown_commander == 'arm_commander':
    arm_commander = SrArmCommander(set_ground=False)
elif dropdown_commander == 'hand_commander':
    hand_commander = SrHandCommander(name=side + "_hand")
else:
    arm_commander = SrArmCommander(set_ground=False)
    hand_commander = SrHandCommander(name=side + "_hand")
