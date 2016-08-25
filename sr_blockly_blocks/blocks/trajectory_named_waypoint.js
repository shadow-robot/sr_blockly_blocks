Blockly.Blocks['trajectory_named_waypoint'] = {
    init: function() {
        var that = this;
        Blockly.callWebService('sr_blockly_blocks', 'get_named_poses', ['right_hand', 'left_hand'], false,
            function (response) {
                if ((null != response) && (response.length > 0)) {
                    that.appendDummyInput()
                        .appendField("Name:")
                        .appendField(new Blockly.FieldDropdown(response), "name");
                }
                else {
                    that.appendDummyInput()
                        .appendField("Name:")
                        .appendField(new Blockly.FieldTextInput("waypoint_name"), "name");
                }
            },
            function(jqXHR, textStatus, errorThrown) {
                that.appendDummyInput()
                    .appendField("Name:")
                    .appendField(new Blockly.FieldTextInput("waypoint_name"), "name");
            });

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