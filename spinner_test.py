from fury import ui, window
from fury.data import read_viz_icons, fetch_viz_icons

textbox = ui.TextBox2D(50, 20, position=(300, 400), text=" "*8 + "23")
button_up = ui.Button2D(icon_fnames=[('square', read_viz_icons(fname='circle-up.png'))], position=(365,408), size=(15,15))
button_down = ui.Button2D(icon_fnames=[('square', read_viz_icons(fname='circle-down.png'))], position=(365,394), size=(15,15))

current_size = (800, 800)
show_manager = window.ShowManager(size=current_size, title="Spinner UI Example")
show_manager.scene.add(textbox)
show_manager.scene.add(button_up)
show_manager.scene.add(button_down)
show_manager.start()
