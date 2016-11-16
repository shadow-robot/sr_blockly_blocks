Blockly.Blocks['tf_listener'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Load TF Listener");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
  }
};
