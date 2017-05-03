import ast

if joint_goal == 'joint_angles':
    arm_commander.move_to_joint_value_target_unsafe(ast.literal_eval(joint_pose_target), time_to_target, wait=wait,
                                                    angle_degrees=angle)
else:
    joints = arm_commander.get_named_target_joint_values(joint_pose_target)
    arm_commander.move_to_joint_value_target_unsafe(joints, time_to_target, wait=wait, angle_degrees=angle)
