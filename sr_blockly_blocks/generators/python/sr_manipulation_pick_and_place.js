Blockly.Python['sr_manipulation_pick'] = function(block) {
    var text_object_id = block.getFieldValue('object_id');
    var code = 'text_object_id = "' + text_object_id.toString() + '"\n';
    code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/sr_manipulation_pick.py");
    return code;
};

Blockly.Python['sr_manipulation_place'] = function(block) {
    var text_location_name = block.getFieldValue('location_name');
    var code = 'text_location_name = "' + text_location_name.toString() + '"\n';
    code += Blockly.readFile("/sr_blockly_blocks/generators/python/scripts/sr_manipulation_place.py");
    return code;
};
