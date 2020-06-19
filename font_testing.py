from fury.ui import TextBlock2D, Disk2D
from fury import window

text = TextBlock2D(text="FURY\nFURY\nFURY\nHello", position=(100, 100), bg_color=(1, 0, 0), color=(0,1,0), font_size=18)
# disk = Disk2D(5, center=(100, 150), color=(1, 0, 0))

# print("Lower-left corner:\n", text.actor.GetPositionCoordinate())
# # text.actor.GetPosition2Coordinate().SetCoordinateSystemToViewport()
# print("Upper-right corner:\n", text.actor.GetPosition2Coordinate())

# text.font_size = 10
# text.justification = "center"
# # text.resize((200, 200))
# print(text.size)
# print(text.font_size)
# print(text.actor.GetTextScaleMode())

# print(dir(text.actor))
texture = text.actor.GetTexture()
data = texture.GetInput()
print(data)
# text.background_color = None
text.position = (0, 100)
# print(text.background_color)
# print(text.background.actor.GetVisibility())
sm = window.ShowManager(size=(400, 400), title="Testing font sizes")
sm.scene.add(text)
sm.start()