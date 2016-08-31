Blockly.Blocks['trajectory_named_waypoint'] = {};

function createTrajectoryNamedWaypoint(data) {
  Blockly.Blocks['trajectory_named_waypoint'] = {
    init: function() {
      if ((null != data) && (data.length > 0)) {
        this.appendDummyInput()
          .appendField("Name:")
          .appendField(new Blockly.FieldDropdown(data), "name");
      }
      else {
        this.appendDummyInput()
          .appendField("Name:")
          .appendField(new Blockly.FieldTextInput("waypoint_name"), "name");
      }

      this.appendDummyInput()
        .appendField("Interpolation time:")
        .appendField(new Blockly.FieldNumber(1, 0, Infinity, 0.01), "interpolation_time")
        .appendField("s");
      this.setOutput(true, null);
      this.setColour(65);
      this.setTooltip('');
      this.setHelpUrl('http://www.shadowrobot.com/');
    }
  };
}

Blockly.waitForComponentToLoad('sr_blockly_blocks', 'get_named_poses', ['right_hand', 'left_hand'],
  function (response) {
    createTrajectoryNamedWaypoint(response);
  },
  function(jqXHR, textStatus, errorThrown) {
    createTrajectoryNamedWaypoint(null);
  });
