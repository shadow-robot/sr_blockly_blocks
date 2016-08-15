Blockly.Blocks['execute'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Execute Trajectory");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};