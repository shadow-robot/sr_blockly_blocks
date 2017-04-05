Blockly.Python['v_object_finder'] = function(block) {
 
  var code = '';


  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/recognizer_client.py");
  code += "\n";

  return code;
};
