Blockly.Blocks['initialise_arm'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Load Arm Commander")
        .appendField(new Blockly.FieldDropdown([["right_arm", "right_arm"],
        ["right_arm_and_manipulator", "right_arm_and_manipulator"]]), "arm_group")
    this.appendDummyInput()
        .appendField("Velocity scaling factor: ")
        .appendField(new Blockly.FieldTextInput("1.0"), "vel_scale")
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(260);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};
