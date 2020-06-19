import numpy as np
from fury import window, utils, actor, primitive
import itertools

vertices, triangles = primitive.prim_star()

colors = 255 * np.random.rand(*vertices.shape)

point_actor = actor.point(vertices, point_radius=0.01, colors=colors/255.)
# this does not work
#colors = np.array([255, 0. , 0.])
# this does work
colors = np.array([[255, 0. , 0.],
                    [255, 0. , 0.],
                    [255, 0. , 0.],
                    [255, 0. , 0.],
                    [255, 0. , 0.],
                    [255, 0. , 0.],
                    [255, 0. , 0.],
                    [255, 0. , 0.]])
frustum_actor = utils.get_actor_from_primitive(vertices=vertices, triangles=triangles, colors=colors, backface_culling=False)

scene = window.Scene()
scene.add(point_actor)
scene.add(actor.axes())
scene.add(frustum_actor)
# frustum_actor.GetProperty().SetOpacity(0.3)
scene.set_camera(position=(10, 5, 7), focal_point=(0, 0, 0))

window.show(scene,size=(600,600), reset_camera=False)
