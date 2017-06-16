Blockly.Blocks['move_to_object_goal'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move ")
        .appendField(new Blockly.FieldDropdown([["above object","object"], ["to goal","goal"]]), "move_drop_down");
    this.appendValueInput("object")
        .setCheck("String")
        .appendField("which object to grasp");
    this.setPreviousStatement(true, "Array");
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
