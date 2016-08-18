Blockly.Python['trajectory_named_waypoint'] = function(block) {
  var text_name = block.getFieldValue('name');
  var number_interpolation_time = block.getFieldValue('interpolation_time');
  var code = "{'name':'" + text_name + "','interpolate_time':" + number_interpolation_time + "}";
  return [code, Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['trajectory_execute_named_waypoint'] = function(block) {

  var list = '[';
  var firstElement = true;
  for (var i = 0; i < block.itemCount_; i++) {
    elementCode = Blockly.Python.valueToCode(block, 'ADD' + i, Blockly.Python.ORDER_NONE);
    if (elementCode) {
      if (firstElement) {
        firstElement = false;
      }
      else {
        list += ',';
      }
      list += elementCode;
    }
  }
  list += ']';

  var code = 'robot_commander.run_named_trajectory(' + list + ')\n';
  return code;
};