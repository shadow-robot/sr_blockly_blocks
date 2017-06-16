Blockly.Blocks['move_to_object'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move above object");
    this.setPreviousStatement(true, "Array");
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};
