Blockly.Blocks['text_to_speech'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Text to speech");
    this.appendDummyInput()
        .appendField("Command:")
        .appendField(new Blockly.FieldTextInput("start"), "command");
    this.setColour(210);
    this.setTooltip('');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};

Blockly.Blocks['word_list'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Accepted words:");
    this.appendDummyInput()
        .appendField("Word 1:")
        .appendField(new Blockly.FieldTextInput("start"), "word_1");
    this.appendDummyInput()
        .appendField("Word 2:")
        .appendField(new Blockly.FieldTextInput("stop"), "word_2");
    this.appendDummyInput()
        .appendField("Word 3:")
        .appendField(new Blockly.FieldTextInput(""), "word_3");
    this.appendDummyInput()
        .appendField("Word 4:")
        .appendField(new Blockly.FieldTextInput(""), "word_4");
    this.appendDummyInput()
        .appendField("Word 5:")
        .appendField(new Blockly.FieldTextInput(""), "word_5");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};