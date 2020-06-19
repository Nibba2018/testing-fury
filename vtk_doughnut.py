import pybullet as p
from time import sleep
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.resetSimulation(p.RESET_USE_DEFORMABLE_WORLD)

p.setGravity(0, 0, -10)

planeId = p.loadURDF("plane.urdf", [0,0,-2])

bunnyId = p.loadSoftBody("torus.vtk", useNeoHookean = 1, NeoHookeanMu = 60, NeoHookeanLambda = 200, NeoHookeanDamping = 0.01, useSelfCollision = 1, frictionCoeff = 0.5)
p.setPhysicsEngineParameter(sparseSdfVoxelSize=0.25)
p.setRealTimeSimulation(1)

while p.isConnected():
  p.setGravity(0,0,-10)
  sleep(1./240.)