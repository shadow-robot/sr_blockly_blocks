Blockly.Python['arm'] = function(block) {
  var dropdown_axis = block.getFieldValue('axis');
  var value_axis = Blockly.Python.valueToCode(block, 'Axis', Blockly.Python.ORDER_ATOMIC);
  var text_displacement = block.getFieldValue('displacement');
  var value_displacement = Blockly.Python.valueToCode(block, 'displacement', Blockly.Python.ORDER_ATOMIC);

  var code = "";
  code += "dropdown_axis = \"" + dropdown_axis.toString() + "\"\n";
  code += "text_displacement = " + text_displacement.toString() + "\n";

  code += Blockly.readPythonFile("scripts/arm.py");

  return code;
};

Blockly.Python['arm_named_pose'] = function(block) {
  var dropdown_named_pose = block.getFieldValue('arm_pose_name');
  var text_time = block.getFieldValue('time');
  var text_pause = block.getFieldValue('pause');

  var code = "";
  code += "dropdown_named_pose = '" + dropdown_named_pose.toString() + "'" + "\n";
  code += "time = " + text_time.toString() + "\n";
  code += "pause = " + text_pause.toString() + "\n";

  code += Blockly.readPythonFile("scripts/arm_named_pose.py");

  return code;
};

Blockly.Python['pose'] = function(block) {
  var dropdown_wait = block.getFieldValue('wait');
  var text_x = block.getFieldValue('x');
  var text_y = block.getFieldValue('y');
  var text_z = block.getFieldValue('z');

  var code = "";
  code += "wait = \"" + dropdown_wait.toString() + "\"\n";
  code += "x_displacement = " + text_x.toString() + "\n";
  code += "y_displacement = " + text_y.toString() + "\n";
  code += "z_displacement = " + text_z.toString() + "\n";

  code += Blockly.readPythonFile("scripts/pose.py");

  return code;
};

Blockly.Python['arm_joint_target'] = function(block) {
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

  code += Blockly.readPythonFile("scripts/arm_joint_target.py");

  return code;
};
