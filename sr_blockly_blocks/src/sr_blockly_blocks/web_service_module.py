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
import rospy
from moveit_msgs.srv import ListRobotStatesInWarehouse as ListState


class WebServiceModule(object):

    def get_named_poses(self, parameters):
        result = []
        try:
            rospy.wait_for_service('list_robot_states', 0.3)
            list_states = rospy.ServiceProxy('list_robot_states', ListState)
            for robot_name in parameters:
                response = list_states('', robot_name)
                for state in response.states:
                    result.append([state])
        except (rospy.ServiceException, rospy.ROSException):
            pass
        return result
