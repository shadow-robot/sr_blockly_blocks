Blockly.Python['move_arm_pick_place'] = function(block) {
  var dropdown_move = block.getFieldValue('Move');
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  var code = "";
  code += "dropdown_move = '" + dropdown_move.toString() + "'" + "\n";
  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/move_arm_pick_place.py");
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
