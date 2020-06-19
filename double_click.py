from fury import actor, window, interactor
import numpy as np

dir1 = np.random.rand(1,3)
dir2 = np.random.rand(1,3)
cube1 = actor.cube([(0, 0, 0)], [(0.16526678, 0.0186237, 0.01906076)], (1,1,1), heights=3)
cube2 = actor.cube([(0, 0, 0)], [(0.16526678, 0.0186237, 0.01906076)], (1,0,0), heights=3)

print(dir1)
print(dir2)

cube2.SetVisibility(False)

def left_single_click(iren, obj):
    print("> Left Single Click <")
    print(iren.event.name)
    iren.force_render()

def left_double_click(iren, obj):
    print("> Left Double Click <")
    print(iren.event.name)
    cube1.SetVisibility(not bool(cube1.GetVisibility()))
    cube2.SetVisibility(not bool(cube2.GetVisibility()))
    iren.force_render()

def right_single_click(iren, obj):
    print("> Right Single Click <")
    iren.force_render()

def right_double_click(iren, obj):
    print("> Right Double Click <")
    cube1.SetVisibility(not bool(cube1.GetVisibility()))
    cube2.SetVisibility(not bool(cube2.GetVisibility()))
    iren.force_render()

def middle_single_click(iren, obj):
    print("> Middle Single Click <")
    iren.force_render()

def middle_double_click(iren, obj):
    print("> Middle Double Click <")
    cube1.SetVisibility(not bool(cube1.GetVisibility()))
    cube2.SetVisibility(not bool(cube2.GetVisibility()))
    iren.force_render()

test_events = {"LeftButtonPressEvent":left_single_click,
                "LeftButtonDoubleClickEvent":left_double_click,
                "RightButtonPressEvent":right_single_click,
                "RightButtonDoubleClickEvent":right_double_click,
                "MiddleButtonPressEvent":middle_single_click,
                "MiddleButtonDoubleClickEvent":middle_double_click}

current_size = (800, 800)
showm = window.ShowManager(size=current_size, title="Double Click Test")
showm.scene.add(cube1, cube2)

for test_event, callback in test_events.items():
    showm.style.add_callback(cube1, test_event, callback)
    showm.style.add_callback(cube2, test_event, callback)

showm.start()
