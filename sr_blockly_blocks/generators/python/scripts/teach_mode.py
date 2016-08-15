
if checkbox_on_off == 'true':
    teach_mode_on = True
else:
    teach_mode_on = False

if hand_arm_select == 'arm_teach':
    arm_commander.set_teach_mode(teach_mode_on)
else:
    hand_commander.set_teach_mode(teach_mode_on)

