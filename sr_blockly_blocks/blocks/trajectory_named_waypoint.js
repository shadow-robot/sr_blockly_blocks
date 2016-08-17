Blockly.Blocks['trajectory_named_waypoint'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Name:")
        .appendField(new Blockly.FieldTextInput("waypoint_name"), "name");
    this.appendDummyInput()
        .appendField("Interpolation time:")
        .appendField(new Blockly.FieldNumber(1, 0, Infinity, 0.01), "interpolation_time")
        .appendField("s");
    this.setOutput(true, null);
    this.setColour(65);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};