Blockly.Python['recognizer'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};

Blockly.Python['move_to_object_goal'] = function(block) {
  var dropdown_move = block.getFieldValue('Move');
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  var code = "";
  code += "dropdown_move = '" + dropdown_move.toString() + "'" + "\n";
  code += "object = '" + value_name.toString() + "'" + "\n";
  code += Blockly.readfile("/sr_blockly_blocks/generators/python/scripts/move_arm_to_goal.py")

  return code;
};

Blockly.Python['move_to_object'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};

Blockly.Python['grasp_new'] = function(block) {
  var value_grasp_id = Blockly.Python.valueToCode(block, 'grasp_id', Blockly.Python.ORDER_ATOMIC);
  var value_max_torque = Blockly.Python.valueToCode(block, 'max torque', Blockly.Python.ORDER_ATOMIC);
  var dropdown_grasp_menu = block.getFieldValue('grasp_menu');
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};
