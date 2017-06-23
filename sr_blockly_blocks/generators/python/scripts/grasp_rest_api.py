import urllib2
import json

port = "8080"
host = "0.0.0.0"
# host = "hand-H"
address = "http://" + host + ":" + port

print "grasp_rest_api"

grasp_cmd = [{"grasp_id": grasp_id, "grasp_state": grasp_state, "max_torque": max_torque}]
print grasp_cmd

api_method_to_test = "/select_grasp"
req = urllib2.Request(address + api_method_to_test)
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(grasp_cmd))
