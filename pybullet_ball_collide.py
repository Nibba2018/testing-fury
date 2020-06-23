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

    contact = p.getContactPoints(red_ball, blue_ball, -1, -1)
    if len(contact) != 0:print(contact)
    # Output:
    # ((0, 0, 1, -1, -1,
    # (-0.023686780875139403, 0.23521219823707942, -0.062410514348040964),
    # (0.023686780875139535, 0.26478780176291894, -0.06241051434804092),
    # (0.8482627424036934, 0.5295756035258475, 7.569817989544679e-16),
    # -0.05584774549455995, 9423.979289768244, -1227.5817656949062,
    # (-0.5295756035258475, 0.8482627424036934, 0.0), -1.4854460576409489e-12,
    # (-6.42119456730798e-16, -4.0087909303939393e-16, 1.0)),)

    print(p.getAABB(red_ball))

    p.stepSimulation()

    # print(cnt)
    if cnt == 1200:
        showm.exit()


showm.add_timer_callback(True, 50, timer_callback)
showm.start()
# window.record(showm.scene, size=(900, 768), out_path="viz_timer.png")


