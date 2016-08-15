Blockly.Blocks['teach_mode'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Teach mode: ")
        .appendField(new Blockly.FieldDropdown([["Arm", "arm_teach"], ["Hand", "hand_teach"]]), "hand_arm_select")
        .appendField(new Blockly.FieldCheckbox("TRUE"), "on_off");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(180);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};