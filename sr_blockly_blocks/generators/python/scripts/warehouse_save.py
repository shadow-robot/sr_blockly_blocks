# Copyright 2019 Shadow Robot Company Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

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
