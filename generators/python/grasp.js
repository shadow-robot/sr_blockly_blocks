Blockly.Python['grasp'] = function(block) {
  var dropdown_grasp_name = block.getFieldValue('grasp_name');
  var text_time = block.getFieldValue('time');
  var text_pause = block.getFieldValue('pause');

  var code = "";
  code += "dropdown_grasp = '" + dropdown_grasp_name.toString() + "'" + "\n";
  code += "time = " + text_time.toString() + "\n";
  code += "pause = " + text_pause.toString() + "\n";

  code += Blockly.readPythonFile("/sr_blockly_blocks/generators/python/scripts/grasp.py");

  return code;
};

Blockly.Python['hand_joint_target'] = function(block) {
  var dropdown_joint_goal = block.getFieldValue('joint_goal');
  var text_joint_pose_target = block.getFieldValue('joint_pose_target');
  var text_time_to_target = block.getFieldValue('time_to_target');
  var dropdown_wait = block.getFieldValue('wait');
  var dropdown_angle = block.getFieldValue('angle');

  var code = "";
  code += "joint_goal = '" + dropdown_joint_goal.toString() + "'" + "\n";
  code += "joint_pose_target = \"" + text_joint_pose_target.toString() + "\"" + "\n";
  code += "time_to_target = " + text_time_to_target.toString() + "\n";
  code += "wait = " + dropdown_wait.toString() + "\n";
  code += "angle = " + dropdown_angle.toString() + "\n";

  code += Blockly.readPythonFile("/sr_blockly_blocks/generators/python/scripts/hand_joint_target.py");
  code += "\n";

  return code;
};
