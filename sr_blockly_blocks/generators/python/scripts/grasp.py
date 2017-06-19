trajectory = [
    {
        'name': dropdown_grasp,
        'interpolate_time': time,
        'pause_time': pause
    }
]

# Run trajectory via moveit
hand_commander.run_named_trajectory(trajectory)
