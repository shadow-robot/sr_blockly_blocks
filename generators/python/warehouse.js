Blockly.Python['warehouse_save'] = function(block) {
  var dropdown_select_save = block.getFieldValue('select_robot_save');
  var text_pose_name = block.getFieldValue('pose_name');
  var code = "";

  code += "select_to_save = '" + dropdown_select_save.toString() + "'" + "\n";
  code += "pose_name = '" + text_pose_name.toString() + "'" + "\n";

  code += Blockly.readPythonFile("/sr_blockly_blocks/generators/python/scripts/warehouse_save.py");
  code += "\n";
  return code;
};

Blockly.Python['launch_warehouse'] = function(block) {
  var code = "";

  code += "import os\n";
  code += "os.system('roslaunch sr_moveit_hand_config default_warehouse_db.launch')";

  return code;
};
