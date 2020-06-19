import fury.ui as ui
import fury.window as window
dSliderH = ui.LineDoubleSlider2D()
dSliderV = ui.LineDoubleSlider2D(orientation="vertical")

def print_values(slider):
	print(f'New Left:{slider.handles[0].position}, Right:{slider.handles[1].position}')

dSliderH.on_change = print_values

sm=window.ShowManager(size=(600,600))
sm.scene.add(dSliderH)
sm.scene.add(dSliderV)
print(f"Initial position of handles:\nLeft:{dSliderH.handles[0].position}, Right:{dSliderH.handles[1].position}")
sm.start()
