Blockly.Python['v_object_finder_v1'] = function(block) {
  var text_transforms = block.getFieldValue('transforms');
  var text_name = block.getFieldValue('names');
 
  var code = "";

  code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/recognizer_client.py");
  code += "\n";
  code += "        " + text_transforms + "= list()" + "\n";
  code += "        " + text_transforms + "= result.transforms" + "\n";
  code += "        " + text_name      + "= list()" + "\n";
  code += "        " + text_name      + "= result_names" + "\n";

  code += "    except rospy.ROSInterruptException:" + "\n";
  code += "        print(\"program interrupted before completion\")  # , file=sys.stderr)" + "\n";
  

  return code;
};
