Blockly.Python['v_object_finder_v2'] = function(block) {
  var text_input_name = block.getFieldValue('input_name');
  var text_transform = block.getFieldValue('transform');
 
  var code = "";

  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/recognizer_client_v1.py");
  code += "\n";
  code += "        input_name_ = \"" + text_input_name + "\"\n";
  
  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/recognizer_client_v1_part2.py");
  code += "\n";

  code += "        " + text_transform + " = transform_" + "\n";

  code += "    except rospy.ROSInterruptException:" + "\n";
  code += "        print(\"program interrupted before completion\")  # , file=sys.stderr)" + "\n";
  
  return code;
};
