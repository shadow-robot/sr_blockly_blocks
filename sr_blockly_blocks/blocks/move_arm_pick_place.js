Blockly.Blocks['move_arm_pick_place'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move arm to")
        .appendField(new Blockly.FieldDropdown([["home position","home"], ["pre-grasp position","pre_grasp"], ["grasp position","grasp"],
        ["pre-release position","pre_release"], ["release position","release"]]), "Move");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};
