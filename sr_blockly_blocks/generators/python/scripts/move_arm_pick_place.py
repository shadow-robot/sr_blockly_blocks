rospy.sleep(2.0)

GRASP_OFFSET = 0.15

ORIENTATION_X = 0.204
ORIENTATION_Y = 0.979
ORIENTATION_Z = -0.007
ORIENTATION_W = 0.004


class MoveArmToGoal:
    def __init__(self):
        self.arm_commander = SrArmCommander(name="right_arm_and_manipulator", set_ground=False)
        self.arm_commander.set_max_velocity_scaling_factor(0.2)

        self.current_pose = arm_commander.get_current_pose()
        self.__mapping = rospy.get_param("objects_to_grasp")
        self.grasp_init()

    def grasp_init(self):
        self.grasp_position = None
        self.grasp_id = None
        self.grasp_orientation = None

    def get_object_transform(self, object_trans):
        self.object_transform = object_trans

    def get_grasp(self, object_id):
        for n, grasp_map in enumerate(self.__mapping):
            object_id_from_yaml = grasp_map["object_id"]
            if object_id_from_yaml == object_id:
                self.grasp_id = grasp_map["grasp_id"]
                self.grasp_position = grasp_map["grasp_position"]
                self.grasp_orientation = grasp_map["grasp_orientation"]
        return self.grasp_id, self.grasp_position, self.grasp_orientation

    def set_object_transform(self, offset=0.0):
        self.object_transform.translation.z = 1.0
        self.x = self.object_transform.translation.x + self.grasp_position[0]
        self.y = self.object_transform.translation.y + self.grasp_position[1]
        self.z = self.object_transform.translation.z + self.grasp_position[2] + offset

    def set_current_pose_orientation(self, orientation=None):
        if orientation is None:
            orientation = self.grasp_orientation
        self.current_pose.orientation.x = float(orientation[0])
        self.current_pose.orientation.y = float(orientation[1])
        self.current_pose.orientation.z = float(orientation[2])
        self.current_pose.orientation.w = float(orientation[3])

    def set_current_pose_position(self, x=None, y=None):
        if x is None and y is None:
            x = self.x
            y = self.y
        self.current_pose.position.x = float(x)
        self.current_pose.position.y = float(y)
        self.current_pose.position.z = float(self.z)

    def move_arm(self):
        self.arm_commander.move_to_pose_target(self.current_pose)

try:
    if isinstance(move_arm_obj, MoveArmToGoal):
        move_arm_obj.grasp_init()
except:
    move_arm_obj = MoveArmToGoal()

object_transform = result_transforms[object_id]
move_arm_obj.get_object_transform(object_transform)

grasp_id, grasp_position, grasp_orientation = move_arm_obj.get_grasp(object_id)
if grasp_id is not None and grasp_position is not None and grasp_orientation is not None:

    move_arm_obj.set_current_pose_orientation()
    if dropdown_move is "pre_grasp":
        move_arm_obj.set_object_transform(GRASP_OFFSET)
        move_arm_obj.set_current_pose_position()
    elif dropdown_move is "grasp":
        move_arm_obj.set_object_transform()
        move_arm_obj.set_current_pose_position()
    elif dropdown_move is "goal":
        X = goal[0]
        Y = goal[1]
        move_arm_obj.set_object_transform(GRASP_OFFSET)
        move_arm_obj.set_current_pose_position(X, Y)
        move_arm_obj.set_current_pose_orientation([ORIENTATION_X, ORIENTATION_Y, ORIENTATION_Z, ORIENTATION_W])

    move_arm_obj.move_arm()
else:
    rospy.logerr("Object %s was not found" % object_id)
