# from __future__ import print_function

import actionlib

# goal message and the result message.
import sr_recognizer.msg

import numpy as np

import rospy
import tf2_ros
import tf
import geometry_msgs.msg

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


if __name__ == '__main__':
    try:
        #     Initializes a rospy node so that the SimpleActionClient can
        #     publish and subscribe over ROS.
        #     rospy.init_node('recognizer_client_py') : not needed, because done by blockly
        result = recognizer_client()

        # tf_br = tf2_ros.TransformBroadcaster()
        tf_br = tf2_ros.TransformBroadcaster()
        t_msg = geometry_msgs.msg.TransformStamped()

        tfBuffer = tf2_ros.Buffer()
        listener = tf2_ros.TransformListener(tfBuffer)

        for i in xrange(0, len(result.ids)):

            parent_frame = "camera_depth_optical_frame"

            name = str(result.ids[i].data)
            print "************ object:", name
            transform = result.transforms[i]

            t_msg.header.stamp = rospy.Time.now()
            t_msg.header.frame_id = parent_frame
            t_msg.child_frame_id = name

            t_msg.transform.translation = transform.translation

            t_msg.transform.rotation = transform.rotation

            tf_br.sendTransform(t_msg)

            world2camera = tfBuffer.lookup_transform("world", "camera_depth_optical_frame", rospy.Time(0), rospy.Duration(3.0))
            print "world2camera", world2camera

            world2camera_trans = [world2camera.transform.translation.x, world2camera.transform.translation.y, world2camera.transform.translation.z]
            world2camera_rota = [world2camera.transform.rotation.x, world2camera.transform.rotation.y, world2camera.transform.rotation.z, world2camera.transform.rotation.w]

            world2camera_trans_matrix = tf.transformations.translation_matrix(world2camera_trans)
            world2camera_rota_matrix = tf.transformations.quaternion_matrix(world2camera_rota)
            world2camera_transform = np.dot(world2camera_trans_matrix, world2camera_rota_matrix)

            camera2object_trans = [transform.translation.x, transform.translation.y,
                                   transform.translation.z]
            camera2object_rota = [transform.rotation.x, transform.rotation.y,
                                  transform.rotation.z, transform.rotation.w]

            camera2object_trans_matrix = tf.transformations.translation_matrix(camera2object_trans)
            camera2object_rota_matrix = tf.transformations.quaternion_matrix(camera2object_rota)
            camera2object_transform = np.dot(camera2object_trans_matrix, camera2object_rota_matrix)

            world2object = np.dot(world2camera_transform, camera2object_transform)


            print "world2object", world2object
            # world2object = np.dot(world2camera, transform)
            # print world2object

            # for index in range(100):
            #     tf_br.sendTransform(t_msg)
            #     rospy.sleep(0.05)
            #     try:
            #         trans = tfBuffer.lookup_transform('world', name, rospy.Time(0)) # , rospy.Duration(3.0)
            #     except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            #         print "excepted "
            #         continue
            #     print trans

            # rospy.sleep(4.0)


            # trans = tfBuffer.lookup_transform('ra_base_link', name, rospy.Time(0))  # , rospy.Duration(3.0)
            # # result.tranform_from_world[i] = trans
            # print trans
            # # print result.tranform_from_world[i]


        print result

    except rospy.ROSInterruptException:
        print("program interrupted before completion")
