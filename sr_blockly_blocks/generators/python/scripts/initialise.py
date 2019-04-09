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
    robot_commander = SrRobotCommander(name="right_arm_and_hand", prefix="H1_")
else:
    arm_commander = SrArmCommander(set_ground=False)
    hand_commander = SrHandCommander(name=side + "_hand")
