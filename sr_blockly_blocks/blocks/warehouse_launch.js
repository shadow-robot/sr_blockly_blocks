Blockly.Blocks['launch_warehouse'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Launch warehouse");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(225);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};