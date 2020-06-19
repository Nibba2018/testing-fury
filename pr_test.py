from fury import window, actor
import numpy as np
scene = window.Scene()
centers = np.random.rand(1, 3)
dirs = np.random.rand(1, 3)
colors = np.random.rand(1, 3)*255
scales = np.random.rand(1, 1)
actor = actor.frustum(centers, dirs, colors, scales)
scene.add(actor)
window.show(scene)