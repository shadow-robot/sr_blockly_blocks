Blockly.Python['recognizer'] = function(block) {
  // TODO: Assemble Python into code variable.
  var code = '...\n';
  return code;
};

Blockly.Python['move_to_object_goal'] = function(block) {
  var dropdown_move_drop_down = block.getFieldValue('move_drop_down');
  var value_object = Blockly.Python.valueToCode(block, 'object', Blockly.Python.ORDER_ATOMIC);
  // TODO: Assemble Python into code variable.
  var code = '...\n';
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
