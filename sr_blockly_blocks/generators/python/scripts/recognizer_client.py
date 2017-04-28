# from __future__ import print_function
# import rospy

import actionlib


# goal message and the result message.
import sr_recognizer.msg


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

        result_names = list()

        for i in xrange(0, len(result.ids)):
            result_names.append(result.ids[i].data)

    except rospy.ROSInterruptException:
        print("program interrupted before completion")
