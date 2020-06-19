from fury import ui
from fury import window

text1 = ui.TextBlock2D("Hello", font_size = 18, position=(300,300))
text2 = ui.TextBlock2D("Hello", font_size = 19, position=(300,300))
text3 = ui.TextBlock2D("Hello", font_size = 20, position=(300,300))
text4 = ui.TextBlock2D("Hello", font_size = 21, position=(300,300))

sm = window.ShowManager(size=(600, 600))
sm.scene.add(text1)
sm.scene.add(text2)
sm.scene.add(text3)
sm.scene.add(text4)
print(text1.actor.GetBoundingBox(sm, sm))
sm.start()
