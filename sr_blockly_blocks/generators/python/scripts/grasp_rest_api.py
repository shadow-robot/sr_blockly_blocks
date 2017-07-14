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
