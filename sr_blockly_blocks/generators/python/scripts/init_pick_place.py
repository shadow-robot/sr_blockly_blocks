import geometry_msgs.msg

TABLE_HEIGHT = 1.0


class InitPickAndPlace(object):
    def __init__(self):
        self.grasp_id = None
        self.grasp_position = None
        self.grasp_orientation = None
        self.max_torque = None

    def get_object_transform(self, object_trans):
        self.object_transform = object_trans

        # Ensure that the object pose in z is same as table height
        self.object_transform.translation.z = TABLE_HEIGHT
        return self.object_transform

    def set_grasp_info(self, object_id):
        objects_to_grasp = rospy.get_param("objects_to_grasp")
        for n, grasp_map in enumerate(objects_to_grasp):
            object_id_from_yaml = grasp_map["object_id"]
            if object_id_from_yaml == object_id:
                self.grasp_id = grasp_map["grasp_id"]
                self.grasp_position = grasp_map["grasp_position"]
                self.grasp_orientation = grasp_map["grasp_orientation"]
                self.max_torque = grasp_map["max_torque"]
                return True
        return False

    def get_grasp_info(self):
        return self.grasp_id, self.max_torque

    def get_grasp_pose(self):
        self.grasp_pose = geometry_msgs.msg.Pose()
        self.grasp_pose.position.x = self.object_transform.translation.x + self.grasp_position[0]
        self.grasp_pose.position.y = self.object_transform.translation.y + self.grasp_position[1]
        self.grasp_pose.position.z = self.object_transform.translation.z + self.grasp_position[2]

        self.grasp_pose.orientation.x = self.grasp_orientation[0]
        self.grasp_pose.orientation.y = self.grasp_orientation[1]
        self.grasp_pose.orientation.z = self.grasp_orientation[2]
        self.grasp_pose.orientation.w = self.grasp_orientation[3]
        return self.grasp_pose

    def get_home_pose(self, home_position, home_orientation):
        self.home_pose = geometry_msgs.msg.Pose()
        self.home_pose.position.x = home_position[0]
        self.home_pose.position.y = home_position[1]
        self.home_pose.position.z = home_position[2]

        self.home_pose.orientation.x = home_orientation[0]
        self.home_pose.orientation.y = home_orientation[1]
        self.home_pose.orientation.z = home_orientation[2]
        self.home_pose.orientation.w = home_orientation[3]
        return self.home_pose

    def get_release_pose(self, release_position, release_orientation):
        self.release_pose = geometry_msgs.msg.Pose()
        self.release_pose.position.x = release_position[0]
        self.release_pose.position.y = release_position[1]
        self.release_pose.position.z = self.grasp_pose.position.z

        self.release_pose.orientation.x = release_orientation[0]
        self.release_pose.orientation.y = release_orientation[1]
        self.release_pose.orientation.z = release_orientation[2]
        self.release_pose.orientation.w = release_orientation[3]
        return self.release_pose


# Fake result_transforms
# obj_tf = geometry_msgs.msg.Transform()
# obj_tf.translation.x = 0.42
# obj_tf.translation.y = 0.88
# result_transforms = {'pringles_red': obj_tf}

# Block starts
init_pick_and_place = False

try:
    object_tf = result_transforms[object_id]

    pick_and_place = InitPickAndPlace()
    object_transform = pick_and_place.get_object_transform(object_tf)

    if pick_and_place.set_grasp_info(object_id):
        grasp_id, max_torque = pick_and_place.get_grasp_info()
        grasp_pose = pick_and_place.get_grasp_pose()
        home_pose = pick_and_place.get_home_pose(home_position, home_orientation)
        release_pose = pick_and_place.get_release_pose(release_position, release_orientation)
        init_pick_and_place = True
    else:
        rospy.logerr("Grasp information for object %s was not found" % object_id)
except:
    init_pick_and_place = False
