import vtk
from fury import utils as vtk_utils
from fury import actor, window, interactor
scene = window.Scene()

# the show manager allows to break the rendering process
# in steps so that the widgets can be added properly
interactor_style = interactor.CustomInteractorStyle()
show_manager = window.ShowManager(scene, size=(800, 800),
                                  reset_camera=False,
                                  interactor_style=interactor_style)

# Create a cursor, a circle that will follow the mouse.
polygon_source = vtk.vtkRegularPolygonSource()
polygon_source.GeneratePolygonOff()  # Only the outline of the circle.
polygon_source.SetNumberOfSides(50)
polygon_source.SetRadius(10)
# polygon_source.SetRadius
polygon_source.SetCenter(0, 0, 0)

mapper = vtk.vtkPolyDataMapper2D()
vtk_utils.set_input(mapper, polygon_source.GetOutputPort())

cursor = vtk.vtkActor2D()
cursor.SetMapper(mapper)
cursor.GetProperty().SetColor(1, 0.5, 0)
scene.add(cursor)

def follow_mouse(iren, obj):
    obj.SetPosition(*iren.event.position)
    iren.force_render()

interactor_style.add_active_prop(cursor)
interactor_style.add_callback(cursor, "MouseMoveEvent", follow_mouse)
show_manager.start()
