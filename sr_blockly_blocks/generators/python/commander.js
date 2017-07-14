Blockly.Python['initialise'] = function(block) {
  var dropdown_commander = block.getFieldValue('commander');
  var dropdown_side = block.getFieldValue('side');
  var code = "";

  code += "dropdown_commander = '" + dropdown_commander.toString() + "'" + "\n";
  code += "side = '" + dropdown_side.toString() + "'" + "\n";

  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/initialise.py");

  return code;
};

Blockly.Python['initialise_arm'] = function(block) {
  var dropdown_arm_group = block.getFieldValue('arm_group');
  var vel_scale = block.getFieldValue('vel_scale');

  var code = "";

  code += "dropdown_arm_group = '" + dropdown_arm_group.toString() + "'" + "\n";
  code += "vel_scale = " + vel_scale.toString() + "\n";

  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/initialise_arm_commander.py");

  return code;
};

Blockly.Python['teach_mode'] = function(block) {
  var dropdown_hand_arm_select = block.getFieldValue('hand_arm_select');
  var checkbox_on_off = block.getFieldValue('on_off') == 'TRUE';
  var code = "";

  code += "hand_arm_select = '" + dropdown_hand_arm_select.toString() + "'" + "\n";
  code += "checkbox_on_off = '" + checkbox_on_off.toString() + "'" + "\n";

  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/teach_mode.py");
  code += "\n";

  return code;
};
