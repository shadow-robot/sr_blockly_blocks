Blockly.Blocks['v_object_finder'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Which Objects do you see?");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
