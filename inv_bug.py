from fury.data import read_viz_icons
from fury import ui, window
button_example = ui.Button2D(icon_fnames=[('Up', read_viz_icons(fname='circle-up.png'))], position=(50,50), size=(30,30))
current_size = (100, 100)
show_manager = window.ShowManager(size=current_size, title="Inverted Image BUG")
show_manager.scene.add(button_example)
show_manager.start()
