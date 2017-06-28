import actionlib
import sr_recognizer.msg
import numpy as np
import rospy
import tf2_ros
import tf
import geometry_msgs.msg

PARENT_FRAME = "camera_depth_optical_frame"


def recognizer_client():
    # Creates the SimpleActionClient, passing the type of the action
    # to the constructor.
    client = actionlib.SimpleActionClient('recognizer', sr_recognizer.msg.RecognizerAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = sr_recognizer.msg.RecognizerGoal(start=1)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()


class Transformations:
    def __init__(self):
        self.tf_br = tf2_ros.TransformBroadcaster()
        self.t_msg = geometry_msgs.msg.TransformStamped()

        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)

    def set_geometry_msgs(self):
        self.t_msg.header.stamp = rospy.Time.now()
        self.t_msg.header.frame_id = PARENT_FRAME
        self.t_msg.child_frame_id = name
        self.t_msg.transform.translation = transform.translation
        self.t_msg.transform.rotation = transform.rotation
        self.tf_br.sendTransform(self.t_msg)

    def set_world2camera(self):
        world2camera = self.tfBuffer.lookup_transform("world", PARENT_FRAME, rospy.Time(0), rospy.Duration(3.0))
        world2camera_trans = [world2camera.transform.translation.x, world2camera.transform.translation.y,
                              world2camera.transform.translation.z]
        world2camera_rota = [world2camera.transform.rotation.x, world2camera.transform.rotation.y,
                             world2camera.transform.rotation.z, world2camera.transform.rotation.w]
        world2camera_trans_matrix = tf.transformations.translation_matrix(world2camera_trans)
        world2camera_rota_matrix = tf.transformations.quaternion_matrix(world2camera_rota)
        self.world2camera_transform = np.dot(world2camera_trans_matrix, world2camera_rota_matrix)

    def set_camera2object(self):
        camera2object_trans = [transform.translation.x, transform.translation.y,
                               transform.translation.z]
        camera2object_rota = [transform.rotation.x, transform.rotation.y,
                              transform.rotation.z, transform.rotation.w]
        camera2object_trans_matrix = tf.transformations.translation_matrix(camera2object_trans)
        camera2object_rota_matrix = tf.transformations.quaternion_matrix(camera2object_rota)
        self.camera2object_transform = np.dot(camera2object_trans_matrix, camera2object_rota_matrix)

    def set_world2object(self):
        self.set_world2camera()
        self.set_camera2object()

        world2object = np.dot(self.world2camera_transform, self.camera2object_transform)

        world2object_t = transform
        world2object_t.translation.x = world2object[0, 3]
        world2object_t.translation.y = world2object[1, 3]
        world2object_t.translation.z = world2object[2, 3]
        return world2object_t

try:
    result = recognizer_client()
    result_names = list()
    result_transforms = dict()

    tt = Transformations()
    for i in xrange(0, len(result.ids)):
        result_names.append(result.ids[i].data)

        for j in xrange(0, len(result.ids)):
            name = str(result.ids[i].data)

            transform = result.transforms[i]
            tt.set_geometry_msgs()
            result_transforms[name] = tt.set_world2object()

except rospy.ROSInterruptException:
    print("program interrupted before completion")
