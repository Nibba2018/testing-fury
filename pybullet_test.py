import numpy as np
from fury import window, actor
import itertools
import pybullet as p


client = p.connect(p.DIRECT)
p.setGravity(0, 0, -10, physicsClientId=client)


boxHalfLength = 0.1
boxHalfWidth = 5
boxHalfHeight = 5
wall_vertical_collision = p.createCollisionShape(
    p.GEOM_BOX,
    halfExtents=[
        boxHalfLength,
        boxHalfWidth,
        boxHalfHeight])
wall_vertical = p.createMultiBody(baseCollisionShapeIndex=wall_vertical_collision,
                         basePosition=[-4, 0, 4])

boxHalfLength_1 = 5
boxHalfWidth_1 = 5
boxHalfHeight_1 = 0.1
wall_horizontal_collision= p.createCollisionShape(
    p.GEOM_BOX,
    halfExtents=[
        boxHalfLength_1,
        boxHalfWidth_1,
        boxHalfHeight_1])
wall_horizontal = p.createMultiBody(baseCollisionShapeIndex=wall_horizontal_collision,
                           basePosition=[0, 0, 0])

boxHalfLength_ = 0.1
boxHalfWidth_ = 0.1
boxHalfHeight_ = 0.5
cuboid_collision = p.createCollisionShape(
    p.GEOM_BOX,
    halfExtents=[
        boxHalfLength_,
        boxHalfWidth_,
        boxHalfHeight_])

cuboid = p.createMultiBody(baseMass=1,
                        baseCollisionShapeIndex=cuboid_collision,
                        basePosition=[0, 0, 4],
                        baseOrientation=[-0.4044981, -0.8089962,
                                         -0.4044981, 0.1352322])

boxHalfLength_ = 0.1
boxHalfWidth_ = 0.1
boxHalfHeight_ = 0.5
sphere_collision = p.createCollisionShape(
    p.GEOM_SPHERE,
    radius=0.5)

sphere = p.createMultiBody(baseMass=0.5,
                        baseCollisionShapeIndex=sphere_collision,
                        basePosition=[0, 0, 4],
                        baseOrientation=[-0.4044981, -0.8089962,
                                         -0.4044981, 0.1352322])

p.changeDynamics(cuboid, -1, lateralFriction=0.5)
p.changeDynamics(cuboid, -1, restitution=0.6)

p.changeDynamics(sphere, -1, lateralFriction=0.5)
p.changeDynamics(sphere, -1, restitution=0.6)

p.changeDynamics(wall_vertical, -1, lateralFriction=0.3)
p.changeDynamics(wall_vertical, -1, restitution=0.5)

p.changeDynamics(wall_horizontal, -1, lateralFriction=0.4)

enableCol = 1
p.setCollisionFilterPair(cuboid, wall_vertical, -1, -1, enableCol)
p.setCollisionFilterPair(cuboid, wall_horizontal, -1, -1, enableCol)

p.setCollisionFilterPair(sphere, wall_vertical, -1, -1, enableCol)
p.setCollisionFilterPair(sphere, wall_horizontal, -1, -1, enableCol)

p.setCollisionFilterPair(sphere, cuboid, -1, -1, enableCol)

xyz = np.array([[0, 0, 0]])
colors = np.array([[1, 0, 0, 1]])
radii = 0.5

scene = window.Scene()


# fetch_viz_textures()
# filename = read_viz_textures("1_earth_8k.jpg")
# image = io.load_image(filename)

# sphere_actor = actor.texture_on_sphere(image)

sphere_actor = actor.sphere(centers=xyz,
                            colors=colors,
                            radii=radii)

cuboid_actor = actor.box(centers=xyz,
                         directions=np.array(p.getEulerFromQuaternion(
                             [-0.4044981, -0.8089962, -0.4044981, 0.1352322])),
                         size=(0.2, 0.2, 1),
                         colors=(0, 1, 1))

wall_vertical_actor = actor.box(centers=np.array([[-4, 0, 4]]),
                         directions=np.array([[1.57, 0, 0]]),
                         size=(0.2, 10, 10),
                         colors=(1, 1, 1))

wall_horizontal_actor = actor.box(centers=np.array([[0, 0, 0]]),
                         directions=np.array([[-1.57, 0, 0]]),
                         size=(10, 10, 0.2),
                         colors=(1, 1, 1))

scene.add(actor.axes())
scene.add(wall_vertical_actor)
scene.add(wall_horizontal_actor)
scene.add(cuboid_actor)
scene.add(sphere_actor)

showm = window.ShowManager(scene,
                           size=(900, 768), reset_camera=False,
                           order_transparent=True)

showm.initialize()
counter = itertools.count()

f = 1


def timer_callback(_obj, _event):
    global f
    cnt = next(counter)
    showm.render()
    cuboid_pos, cuboid_orn = p.getBasePositionAndOrientation(cuboid)
    sphere_pos, sphere_orn = p.getBasePositionAndOrientation(sphere)

    if f:
        print("entered")
        for j in range(5):
            p.applyExternalForce(cuboid, -1,
                                 forceObj=[-1000, 0, -100],
                                 posObj=cuboid_pos,
                                 flags=p.WORLD_FRAME)

            p.applyExternalForce(sphere, -1,
                                 forceObj=[-1000, 0, -100],
                                 posObj=sphere_pos,
                                 flags=p.WORLD_FRAME)
            f = 0

    cuboid_actor.SetPosition(*cuboid_pos)
    cuboid_orn_deg = np.degrees(p.getEulerFromQuaternion(cuboid_orn))
    cuboid_actor.SetOrientation(*cuboid_orn_deg)
    cuboid_actor.RotateWXYZ(*cuboid_orn)

    sphere_actor.SetPosition(*sphere_pos)
    sphere_orn_deg = np.degrees(p.getEulerFromQuaternion(sphere_orn))
    sphere_actor.SetOrientation(*sphere_orn_deg)
    sphere_actor.RotateWXYZ(*sphere_orn)

    p.stepSimulation()

    print(cnt)
    if cnt == 1200:
        showm.exit()


showm.add_timer_callback(True, 10, timer_callback)
showm.start()
# window.record(showm.scene, size=(900, 768), out_path="viz_timer.png")
