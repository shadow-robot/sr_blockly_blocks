Blockly.Blocks['v_object_finder_v2'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Finde me the object:")
        .appendField(new Blockly.FieldTextInput("name"), "input_name");
    this.appendDummyInput()
        .appendField("Output:")
        .appendField(new Blockly.FieldTextInput("transform"), "transform");
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
