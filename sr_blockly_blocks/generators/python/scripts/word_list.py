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
import threading
from std_msgs.msg import String

try:
    if world_list_initialization is not None:
        pass
except NameError:
    world_list_initialization = True


if world_list_initialization:

    world_list_initialization = False
    message_arrived_trigger_event = threading.Event()

    def speech_recognition_callback(message):
        global recognized_message, message_arrived_trigger_event
        rospy.loginfo("Recognized => %s", message.data)
        recognized_message = message.data
        message_arrived_trigger_event.set()

    speech_recognition_subscriber = rospy.Subscriber("recognizer/output", String, speech_recognition_callback)
    command_execution_timeout = 2


found = False

recognition_list = set(words_to_recognize)
if "" in recognition_list:
    recognition_list.remove("")

recognized_words_set = set()

while not found and not rospy.is_shutdown():
    recognized_message = ""
    message_arrived_trigger_event.clear()
    message_arrived_trigger_event.wait(command_execution_timeout)
    recognized_message_set = set(recognized_message.split(" "))
    recognized_words_set = recognized_message_set.intersection(recognition_list)
    if len(recognized_words_set) > 0:
        found = True

recognized_words = list(recognized_words_set)
