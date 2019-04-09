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

current_pose = arm_commander.get_current_pose()

current_pose.position.x = float(x_displacement)
current_pose.position.y = float(y_displacement)
current_pose.position.z = float(z_displacement)

arm_commander.move_to_pose_target(current_pose, wait=wait)
