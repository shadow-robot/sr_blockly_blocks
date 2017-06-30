# from __future__ import print_function

import actionlib

# goal message and the result message.
import sr_recognizer.msg

import rospy
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

try:
    # Run recognizer
    result = recognizer_client()

    # Publish tf frames if confident about object
    tf_br = tf2_ros.TransformBroadcaster()
    t_msg = geometry_msgs.msg.TransformStamped()
    tfBuffer = tf2_ros.Buffer()

    parent_frame = "camera_depth_optical_frame"

    for i in xrange(0, len(result.ids)):
        if result.confidences[i] >= 0.5:
            name = str(result.ids[i].data)
            transform = result.transforms[i]

            t_msg.header.stamp = rospy.Time.now()
            t_msg.header.frame_id = parent_frame
            t_msg.child_frame_id = name

            t_msg.transform.translation = transform.translation
            t_msg.transform.rotation = transform.rotation

            tf_br.sendTransform(t_msg)

except rospy.ROSInterruptException:
    print("program interrupted before completion")
