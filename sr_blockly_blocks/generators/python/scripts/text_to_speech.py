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

try:
    if text_to_speech_initialization is not None:
        pass
except NameError:
    text_to_speech_initialization = True


if text_to_speech_initialization:

    text_to_speech_initialization = False

    from sound_play.libsoundplay import SoundClient

    sound_handle = SoundClient()

rospy.sleep(1)
sound_handle.say(text_command, "voice_kal_diphone")
