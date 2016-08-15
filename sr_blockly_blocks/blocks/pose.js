Blockly.Blocks['pose'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move arm to pose:");
    this.appendDummyInput()
        .appendField("Position: ")
        .appendField("X")
        .appendField(new Blockly.FieldTextInput("0.1"), "x")
        .appendField("m")
        .appendField("Y")
        .appendField(new Blockly.FieldTextInput("0.1"), "y")
        .appendField("m")
        .appendField("Z")
        .appendField(new Blockly.FieldTextInput("0.1"), "z")
        .appendField("m");
    this.appendDummyInput()
        .appendField("Wait for movement to complete: ")
        .appendField(new Blockly.FieldDropdown([["True", "true"], ["False", "false"]]), "wait");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(260);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};