Blockly.Blocks['v_object_finder_v1'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Which Objects do you see?");
    this.appendDummyInput()
        .appendField("Output:")
        .appendField(new Blockly.FieldTextInput("names"), "names")
        .appendField(",")
        .appendField(new Blockly.FieldTextInput("transforms"), "transforms");
    this.setNextStatement(true, null);
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
