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
