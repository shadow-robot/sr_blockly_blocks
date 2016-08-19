Blockly.Blocks['grasp'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Grasp")
        .appendField(new Blockly.FieldDropdown([["Pack", "pack"], ["Open", "open"], ["Fingers packed, open thumb", "fingers_pack_thumb_open"]]), "grasp_name");
    this.appendDummyInput()
        .appendField("Interpolation time: ")
        .appendField(new Blockly.FieldTextInput("3"), "time")
        .appendField("s")
        .appendField("Pause: ")
        .appendField(new Blockly.FieldTextInput("0"), "pause")
        .appendField("s");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(306);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};
