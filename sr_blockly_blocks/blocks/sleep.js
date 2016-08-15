Blockly.Blocks['sleep'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Sleep:")
        .appendField(new Blockly.FieldTextInput("1"), "sleep")
        .appendField("s");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};