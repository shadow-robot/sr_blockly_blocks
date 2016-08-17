if (null == toolboxXmlText) {
    var toolboxXmlText = "";
}
toolboxXmlText += `
    <category id="shadow" name="Shadow Robot" colour="306">
        <category name="Commander">
          <block type="initialise"></block>
          <block type="teach_mode"></block>
        </category>
        <category name="Hand">
          <block type="grasp"></block>
          <block type="hand_joint_target"></block>
        </category>
        <category name="Arm">
          <block type="arm"></block>
          <block type="pose"></block>
          <block type="arm_named_pose"></block>
          <block type="arm_joint_target"></block>
        </category>
        <category name="Trajectory">
          <block type="trajectory_named_waypoint"></block>
          <block type="execute"></block>
        </category>
        <category name="Voice Recognition">
          <block type="text_to_speech"></block>
          <block type="word_list"></block>
        </category>
        <category name="ROS">
          <block type="sleep"></block>
        </category>
        <category name="Warehouse Database">
          <block type="warehouse_save"></block>
          <block type="launch_warehouse"></block>
        </category>
    </category>
`;
