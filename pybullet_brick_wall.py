import numpy as np
from fury import window, actor
import itertools
import pybullet as p
import time

# Pybullet client
client = p.connect(p.DIRECT)
p.setGravity(0, 0, -10, physicsClientId=client)

class storage:
    f = 1 # F determines if the force has been applied or not.
    orn_prev = 0 # to keep track of the previous orientation.(No use for now)

# BALL
ball_actor = actor.sphere(centers = np.array([[0, 0, 0]]),
                    colors=np.array([1,0,0]),
                    radii=0.3)
ball_coll = p.createCollisionShape(p.GEOM_SPHERE,
                                    radius=0.3)
ball = p.createMultiBody(baseMass=3,
                          baseCollisionShapeIndex=ball_coll,
                          basePosition=[2, 0, 1.5],
                          baseOrientation=[ 0, 0, 0, 1 ])
p.changeDynamics(ball, -1, lateralFriction=0.3, restitution=0.5)

# BASE Plane
base_actor = actor.box(centers=np.array([[0, 0, 0]]),
                         directions=[0,0,0],
                         size=(5, 5, 0.2) ,
                         colors=(1, 1, 1))
base_coll = p.createCollisionShape(p.GEOM_BOX,
                                   halfExtents=[2.5, 2.5, 0.1]) # half of the actual size.
base = p.createMultiBody(
                          baseCollisionShapeIndex=base_coll,
                          basePosition=[0, 0, -0.1],
                          baseOrientation=[ 0, 0, 0, 1 ])
p.changeDynamics(base, -1, lateralFriction=0.3, restitution=0.5)

height = 10
base_length = 10


brick_Ids = []
brick_actors = []

scene = window.Scene()
scene.add(actor.axes())
scene.add(ball_actor)
scene.add(base_actor)

# print("working....")
for i in range(height):
    temp = []
    temp_actors=[]
    for j in range(base_length):
        pos = np.array([[-1, (0.2+j*0.4), (0.1 + 0.2*i)]])
        brick_actor = actor.box(centers=np.array([[0, 0, 0]]),
                         directions=np.array([1.57, 0,0]),
                         size=(0.2, 0.4, 0.2) ,
                         colors=np.random.rand(1,3))
        #physics of the brick

        brick_coll = p.createCollisionShape(p.GEOM_BOX,
                                            halfExtents=[0.1, 0.2, 0.1])
        brick = p.createMultiBody(baseMass=0.5,
                                   baseCollisionShapeIndex=brick_coll,
                                   basePosition=[-1, (j*0.4) - 1.5, (0.2*i)],
                                   baseOrientation=[ 0, 0, 0, 1 ])
        p.changeDynamics(brick, -1, lateralFriction=0.1, restitution=0.1)

        pos, _ = p.getBasePositionAndOrientation(brick)
        brick_actor.SetPosition(pos[0], pos[1], pos[2])
        # Add collision of bricks with the ball
        enableCol = 1
        p.setCollisionFilterPair(ball, brick, -1, -1, enableCol)

        scene.add(brick_actor)
        temp_actors.append(brick_actor)

        temp.append(brick)
    brick_Ids.append(temp)
    brick_actors.append(temp_actors)

scene.add(base_actor, ball_actor)

showm = window.ShowManager(scene,
                           size=(900, 768), reset_camera=False,
                           order_transparent=True)

showm.initialize()
counter = itertools.count()

for i, brick_row in enumerate(brick_actors):
        for j, brick_actor in enumerate(brick_row):
            enableCol = 1
            p.setCollisionFilterPair(base, brick, -1, -1, enableCol)

def timer_callback(_obj, _event):
    cnt = next(counter)
    showm.render()

    pos, orn = p.getBasePositionAndOrientation(ball)
    base_pos, base_orn = p.getBasePositionAndOrientation(base)
    base_actor.SetPosition(base_pos[0], base_pos[1], base_pos[2])
    if storage.f:
        print("entered")
        for j in range(5):
            p.applyExternalForce(ball, -1,
                                  forceObj=[-2000, 0, 0],
                                  posObj=pos,
                                  flags=p.WORLD_FRAME)
            storage.f = 0

    # Updating brick position
    for i, brick_row in enumerate(brick_actors):
        for j, brick_actor in enumerate(brick_row):
            ball_actor.SetPosition(pos[0], pos[1], pos[2])
            brick_pos, brick_orn = p.getBasePositionAndOrientation(brick_Ids[i][j])
            brick_actor.SetPosition(brick_pos[0], brick_pos[1], brick_pos[2])
            orn_deg = np.degrees(p.getEulerFromQuaternion(brick_orn))
            brick_actor.SetOrientation(orn_deg[0], orn_deg[1], orn_deg[2])
            brick_actor.RotateWXYZ(orn[1], orn[2], orn[3], orn[0])
    p.stepSimulation()
    # print(orn)
    # storage.orn_prev = orn

    if cnt == 2000:
        showm.exit()

showm.add_timer_callback(True, 10, timer_callback)
showm.start()
# window.record(showm.scene, size=(900, 768), out_path="viz_timer.png")