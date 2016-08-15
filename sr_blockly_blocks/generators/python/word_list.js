Blockly.Python['word_list'] = function(block) {
  var text_word_1 = block.getFieldValue('word_1');
  var text_word_2 = block.getFieldValue('word_2');
  var text_word_3 = block.getFieldValue('word_3');
  var text_word_4 = block.getFieldValue('word_4');
  var text_word_5 = block.getFieldValue('word_5');

  var code = "words_to_recognize = [" +
      "'" +  text_word_1 + "'," +
      "'" +  text_word_2 + "'," +
      "'" +  text_word_3 + "'," +
      "'" +  text_word_4 + "'," +
      "'" +  text_word_5 + "'" +
      "]\n";

  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/word_list.py");

  return code;
};
