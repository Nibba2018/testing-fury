import numpy as np
from fury import actor, window
scene = window.Scene()
lines = [np.array([0.50, 0.50, 0.50]), np.array([0.20, 0.3, 0.6])]
colors = np.random.rand(2, 3)
c = actor.line(lines, colors)
scene.add(c)
window.show(scene)
