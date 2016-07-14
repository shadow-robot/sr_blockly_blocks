Blockly.Python['initialise'] = function(block) {
  var dropdown_commander = block.getFieldValue('commander');
  var dropdown_side = block.getFieldValue('side');
  var code = "";

  code += "dropdown_commander = '" + dropdown_commander.toString() + "'" + "\n";
  code += "side = '" + dropdown_side.toString() + "'" + "\n";

  code += Blockly.readPythonFile("/sr_blockly_blocks/generators/python/scripts/initialise.py");

  return code;
};

Blockly.Python['teach_mode'] = function(block) {
  var dropdown_hand_arm_select = block.getFieldValue('hand_arm_select');
  var checkbox_on_off = block.getFieldValue('on_off') == 'TRUE';
  var code = "";

  code += "hand_arm_select = '" + dropdown_hand_arm_select.toString() + "'" + "\n";
  code += "checkbox_on_off = '" + checkbox_on_off.toString() + "'" + "\n";

  code += Blockly.readPythonFile("/sr_blockly_blocks/generators/python/scripts/teach_mode.py");
  code += "\n";

  return code;
};
