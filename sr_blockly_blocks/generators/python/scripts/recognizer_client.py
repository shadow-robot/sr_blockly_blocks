# from __future__ import print_function

import actionlib

# goal message and the result message.
import sr_recognizer.msg



import rospy
import tf
import tf2_ros
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
        # rate = rospy.Rate(10.0)
        # while not rospy.is_shutdown():

        #     Initializes a rospy node so that the SimpleActionClient can
        #     publish and subscribe over ROS.
        #     rospy.init_node('recognizer_client_py') : not needed, because done by blockly
        result = recognizer_client()
        # print result

        result_names = list()

        for i in xrange(0, len(result.ids)):
            result_names.append(result.ids[i].data)
            # print result.ids[i]

        # rospy.init_node('recognizer_client_py')
        tf_br = tf2_ros.TransformBroadcaster()
        t_msg = geometry_msgs.msg.TransformStamped()

        # trans_pub = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.TransformStamped,
        #                              queue_size=1)

        for i in xrange(0, len(result.ids)):

            parent_frame = "camera_depth_optical_frame"
            # parent_frame = "camera_rgb_optical_frame"

            name = result.ids[i]
            transform = result.transforms[i]

            t_msg.header.stamp = rospy.Time.now()
            t_msg.header.frame_id = parent_frame
            t_msg.child_frame_id = str(name)

            t_msg.transform.translation = transform.translation

            t_msg.transform.rotation = transform.rotation

            tf_br.sendTransform(t_msg)

            # rate.sleep()

    except rospy.ROSInterruptException:
        print("program interrupted before completion")
