from fury import ui, window
from fury.data import read_viz_icons, fetch_viz_icons

textbox1 = ui.TextBox2D(50, 20, position=(330, 300), text="Element 1" + " "*8)
button_right = ui.Button2D(icon_fnames=[('square', read_viz_icons(fname='circle-right.png'))], position=(295,295), size=(30,30))

textbox2 = ui.TextBox2D(50, 20, position=(330, 270), text="Element 2" + " "*8)
button_down = ui.Button2D(icon_fnames=[('square', read_viz_icons(fname='circle-down.png'))], position=(295,265), size=(30,30))

content = ui.Panel2D(size=(170, 100), color=(1, 1, 1), align="left")
content.center = (330, 330)

textbox = ui.TextBox2D(50, 10, text="Hello World!!")
content.add_element(textbox, (20, 50))

elements = [textbox1, button_right, button_down, content, textbox2, textbox]

current_size = (800, 800)
show_manager = window.ShowManager(size=current_size, title="Accordion UI Example")
for element in elements:
	show_manager.scene.add(element)
show_manager.start()
