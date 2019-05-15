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
import ast

if joint_goal == 'joint_angles':
    arm_commander.move_to_joint_value_target_unsafe(ast.literal_eval(joint_pose_target), time_to_target, wait=wait,
                                                    angle_degrees=angle)
else:
    joints = arm_commander.get_named_target_joint_values(joint_pose_target)
    arm_commander.move_to_joint_value_target_unsafe(joints, time_to_target, wait=wait, angle_degrees=angle)
