
from moveit_msgs.srv import SaveRobotStateToWarehouse as SaveState
from sensor_msgs.msg import JointState
from moveit_msgs.msg import RobotState
from sr_utilities.hand_finder import HandFinder
from sr_robot_commander.sr_robot_state_saver import SrStateSaverUnsafe

if "__main__" == __name__:

    if select_to_save == 'arm_and_hand_save':
        which = 'both'
    elif select_to_save == 'arm_save':
        which = 'arm'
    else:
        which = 'hand'

    gs = SrStateSaverUnsafe(pose_name, which)
    gs.spin()
