Blockly.Blocks['recognizer'] = {
  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("Which objects do you see?");
    this.setNextStatement(true, "Array");
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
