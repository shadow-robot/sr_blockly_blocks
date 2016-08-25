
class WebServiceModule(object):

    def get_named_poses(self, parameters):
        # Debug code
        result = []
        for robot_name in parameters:
            result.append(['One pose - ' + robot_name, 'one_pose_' + robot_name])
        return result
