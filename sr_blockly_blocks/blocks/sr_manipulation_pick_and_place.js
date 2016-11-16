Blockly.Blocks['sr_manipulation_pick'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Pick Object");
    this.appendDummyInput()
        .appendField("Object ID")
        .appendField(new Blockly.FieldTextInput("elipta_device_1"), "object_id");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
  }
};
