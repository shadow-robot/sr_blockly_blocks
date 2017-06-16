Blockly.Blocks['grasp_new'] = {
  init: function() {
    this.appendValueInput("grasp_id")
        .setCheck("String")
        .appendField("grasp id");
    this.appendValueInput("max torque")
        .setCheck("Number")
        .appendField("max torque");
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["pregrasp","pre_grasp"], ["grasp","grasp"]]), "grasp_menu");
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
