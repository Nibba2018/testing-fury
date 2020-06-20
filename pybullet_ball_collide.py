import numpy as np
from fury import window, actor
import itertools
import pybullet as p

client = p.connect(p.DIRECT)
p.setGravity(0, 0, -10, physicsClientId=client)

red_ball_coll = p.createCollisionShape(
    p.GEOM_SPHERE,
    radius=0.5)

red_ball = p.createMultiBody(baseMass=0.5,
                        baseCollisionShapeIndex=red_ball_coll,
                        basePosition=[10, 0.5, 0],
                        baseOrientation=[-0.4044981, -0.8089962,
                                         -0.4044981, 0.1352322])

blue_ball_coll = p.createCollisionShape(
    p.GEOM_SPHERE,
    radius=0.5)

blue_ball = p.createMultiBody(baseMass=0.5,
                        baseCollisionShapeIndex=red_ball_coll,
                        basePosition=[-10, 0, 0],
                        baseOrientation=[-0.4044981, -0.8089962,
                                         -0.4044981, 0.1352322])

p.changeDynamics(red_ball, -1, restitution=0.6)
p.changeDynamics(blue_ball, -1, restitution=0.6)

# print(p.getDynamicsInfo(red_ball, -1))

enableCol = 1
p.setCollisionFilterPair(red_ball, blue_ball, -1, -1, enableCol)

scene = window.Scene()

red_ball_actor = actor.sphere(centers=np.array([[0, 0, 0]]),
                            colors=np.array([[1, 0, 0]]),
                            radii=0.5)

blue_ball_actor = actor.sphere(centers=np.array([[0, 0, 0]]),
                            colors=np.array([[0, 0, 1]]),
                            radii=0.5)

scene.add(actor.axes())
scene.add(red_ball_actor)
scene.add(blue_ball_actor)

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
    red_pos, red_orn = p.getBasePositionAndOrientation(red_ball)
    blue_pos, blue_orn = p.getBasePositionAndOrientation(blue_ball)

    if f:
        print("entered")
        for j in range(5):
            p.applyExternalForce(red_ball, -1,
                                 forceObj=[-8000, 0, 0],
                                 posObj=red_pos,
                                 flags=p.WORLD_FRAME)

            p.applyExternalForce(blue_ball, -1,
                                 forceObj=[8000, 0, 0],
                                 posObj=blue_pos,
                                 flags=p.WORLD_FRAME)

            f = 0

    red_pos, red_orn = p.getBasePositionAndOrientation(red_ball)
    blue_pos, blue_orn = p.getBasePositionAndOrientation(blue_ball)

    red_ball_actor.SetPosition(*red_pos)
    red_orn_deg = np.degrees(p.getEulerFromQuaternion(red_orn))
    red_ball_actor.SetOrientation(*red_orn_deg)
    red_ball_actor.RotateWXYZ(*red_orn)

    blue_ball_actor.SetPosition(*blue_pos)
    blue_orn_deg = np.degrees(p.getEulerFromQuaternion(blue_orn))
    blue_ball_actor.SetOrientation(*blue_orn_deg)
    blue_ball_actor.RotateWXYZ(*blue_orn)

    p.stepSimulation()

    print(cnt)
    if cnt == 1200:
        showm.exit()


showm.add_timer_callback(True, 50, timer_callback)
showm.start()
# window.record(showm.scene, size=(900, 768), out_path="viz_timer.png")


