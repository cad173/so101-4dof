import mujoco


model = mujoco.MjModel.from_xml_path("models/scene_4dof.xml")

print("Number of joints:", model.njnt)
print("Degrees of freedom:", model.nv)
print("Number of actuators:", model.nu)

print("\nJoints:")
for i in range(model.njnt):
    print(model.joint(i).name)

print("\nActuators:")
for i in range(model.nu):
    print(model.actuator(i).name)
