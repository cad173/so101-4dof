import mujoco

model = mujoco.MjModel.from_xml_path(
    "models/scene_4dof.xml"
)

joint_names = [
    "base",
    "shoulder",
    "elbow",
    "wrist",
    "gripper",
]

for name in joint_names:
    joint = model.joint(name)

    print(f"\nJoint: {name}")
    print(f"Axis: {joint.axis}")
    print(f"Position: {joint.pos}")
    print(f"Range: {joint.range}")
