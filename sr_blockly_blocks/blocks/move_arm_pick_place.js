Blockly.Blocks['move_arm_pick_place'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move arm to")
        .appendField(new Blockly.FieldDropdown([["pre-grasp position","pre_grasp"], ["grasp position","grasp"], ["goal","goal"]]), "Move");
    this.appendValueInput("NAME")
        .setCheck("String")
        .appendField("Which object to grasp");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
