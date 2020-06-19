from fury import actor, window
import numpy as np

scene = window.Scene()
data = np.zeros((50, 50, 50))
data[15:20, 25, 25] = 1.
data[25, 20:30, 25] = 2.
data[25, 40:50, 30:50] = 3.

surface = actor.contour_from_label(data, color=np.random.rand(3, 3), opacity=0.6)

scene.add(surface)
scene.reset_camera()
scene.reset_clipping_range()
window.show(scene)
