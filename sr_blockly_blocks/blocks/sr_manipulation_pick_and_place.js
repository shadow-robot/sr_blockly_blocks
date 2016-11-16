Blockly.Blocks['sr_manipulation_pick'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Pick Object");
    this.appendDummyInput()
        .appendField("Object ID")
        .appendField(new Blockly.FieldTextInput("object id"), "object_id");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
  }
};

Blockly.Blocks['sr_manipulation_place'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Place Object");
    this.appendDummyInput()
        .appendField("Place Location");
        .appendField(new Blockly.FieldTextInput("location name"), "location_name");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
  }
};
