Blockly.Blocks['arm_named_pose'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move arm to named pose:")
        .appendField(new Blockly.FieldDropdown([["Home", "ra_home"], ["Up", "ra_up"]]), "arm_pose_name");
    this.appendDummyInput()
        .appendField("Interpolation time: ")
        .appendField(new Blockly.FieldTextInput("3"), "time")
        .appendField("s")
        .appendField("Pause: ")
        .appendField(new Blockly.FieldTextInput("0"), "pause")
        .appendField("s");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};