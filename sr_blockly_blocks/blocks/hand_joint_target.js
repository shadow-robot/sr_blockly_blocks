Blockly.Blocks['hand_joint_target'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move hand to joint target:");
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["Pose name", "enter_pose"], ["Enter angles", "joint_angles"]]), "joint_goal")
        .appendField(new Blockly.FieldTextInput("default"), "joint_pose_target");
    this.appendDummyInput()
        .appendField("Time:")
        .appendField(new Blockly.FieldTextInput("2"), "time_to_target")
        .appendField("Wait:")
        .appendField(new Blockly.FieldDropdown([["True", "True"], ["False", "False"]]), "wait")
        .appendField("Angle unit:")
        .appendField(new Blockly.FieldDropdown([["Radians", "False"], ["Degrees", "True"]]), "angle");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(240);
    this.setTooltip('Enter pose as either named pose or a list of joint angles in curly braces.');
    this.setHelpUrl('http://www.shadowrobot.com/');
  }
};
