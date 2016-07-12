Blockly.Blocks['arm'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move arm:")
        .appendField(new Blockly.FieldDropdown([["X", "x_axis"], ["Y", "y_axis"], ["Z", "z_axis"]]), "axis")
        .appendField("axis");
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("0.1"), "displacement")
        .appendField("m");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(197);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};