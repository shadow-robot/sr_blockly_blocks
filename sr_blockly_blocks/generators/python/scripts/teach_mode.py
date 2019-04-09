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
if checkbox_on_off == 'true':
    teach_mode_on = True
else:
    teach_mode_on = False

if hand_arm_select == 'arm_teach':
    arm_commander.set_teach_mode(teach_mode_on)
else:
    hand_commander.set_teach_mode(teach_mode_on)
