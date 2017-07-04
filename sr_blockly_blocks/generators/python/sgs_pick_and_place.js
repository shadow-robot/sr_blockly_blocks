Blockly.Python['init_pick_place'] = function(block) {
  var object_id = block.getFieldValue('object_id');
  var pre_grasp_offset_z = block.getFieldValue('pre_grasp_offset_z');

  var home_position_x = block.getFieldValue('home_x');
  var home_position_y = block.getFieldValue('home_y');
  var home_position_z = block.getFieldValue('home_z');
  var home_orientation_x = block.getFieldValue('home_orientation_x');
  var home_orientation_y = block.getFieldValue('home_orientation_y');
  var home_orientation_z = block.getFieldValue('home_orientation_z');
  var home_orientation_w = block.getFieldValue('home_orientation_w');

  var release_position_x = block.getFieldValue('release_x');
  var release_position_y = block.getFieldValue('release_y');
  var release_orientation_x = block.getFieldValue('release_orientation_x');
  var release_orientation_y = block.getFieldValue('release_orientation_y');
  var release_orientation_z = block.getFieldValue('release_orientation_z');
  var release_orientation_w = block.getFieldValue('release_orientation_w');

  var code = "";
  code += "object_id = \"" + object_id.toString() + "\"\n";
  code += "pre_grasp_offset_z = " + pre_grasp_offset_z.toString() + "\n";
  code += "home_position = [" + home_position_x.toString() + "," + home_position_y.toString() + "," +
  home_position_z.toString() +  "]\n";
  code += "home_orientation = [" + home_orientation_x.toString() + "," + home_orientation_y.toString() + "," +
  home_orientation_z.toString() + "," + home_orientation_w.toString()+ "]\n";
  code += "release_position = [" + release_position_x.toString() + "," + release_position_y.toString() +  "]\n";
  code += "release_orientation = [" + release_orientation_x.toString() + "," + release_orientation_y.toString() + "," +
  release_orientation_z.toString() + "," + release_orientation_w.toString()+ "]\n";
  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/init_pick_place.py");
  return code;
};

Blockly.Python['move_arm_pick_place'] = function(block) {
  var dropdown_move = block.getFieldValue('Move');
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  var code = "";
  code += "dropdown_move = '" + dropdown_move.toString() + "'" + "\n";
  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/move_arm_pick_and_place.py");
  code += "\n";

  return code;
};

Blockly.Python['grasp_rest_api'] = function(block) {
  var value_grasp_id = Blockly.Python.valueToCode(block, 'grasp_id', Blockly.Python.ORDER_ATOMIC);
  var value_max_torque = Blockly.Python.valueToCode(block, 'max torque', Blockly.Python.ORDER_ATOMIC);
  var dropdown_grasp_menu = block.getFieldValue('grasp_menu');

  var code = "";
  code += "grasp_state = '" + dropdown_grasp_menu.toString() + "'" + "\n";
  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/grasp_rest_api.py");
  code += "\n";

  return code;
};
