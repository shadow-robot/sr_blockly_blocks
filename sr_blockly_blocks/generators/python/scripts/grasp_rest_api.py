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
import urllib2
import json

PORT = "8080"
HOST = "0.0.0.0"
ADDRESS = "http://" + HOST + ":" + PORT
API_METHOD = "/select_grasp"

grasp_cmd = [{"grasp_id": grasp_id, "grasp_state": grasp_state, "max_torque": max_torque}]

req = urllib2.Request(ADDRESS + API_METHOD)
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(grasp_cmd))
