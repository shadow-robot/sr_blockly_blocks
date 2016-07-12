Blockly.Blocks['warehouse_save'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Save to warehouse:")
        .appendField(new Blockly.FieldDropdown([["Arm", "arm_save"], ["Hand", "hand_save"], ["Arm and Hand", "arm_and_hand_save"]]), "select_robot_save");
    this.appendDummyInput()
        .appendField("Save as:")
        .appendField(new Blockly.FieldTextInput("default"), "pose_name");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(330);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};