Blockly.Python['trajectory_named_waypoint'] = function(block) {
  var text_name = block.getFieldValue('name');
  var number_interpolation_time = block.getFieldValue('interpolation_time');
  var code = "{'name':'" + text_name + "','interpolate_time':" + number_interpolation_time + "}";
  return [code, Blockly.Python.ORDER_NONE];
};