from fury import ui, window

textbox = ui.TextBox2D(100, 100)

current_size = (800, 800)
show_manager = window.ShowManager(size=current_size, title="DIPY UI Example")
show_manager.scene.add(textbox)
show_manager.start()
