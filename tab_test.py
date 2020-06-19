from fury import ui, window

tab_ui = ui.TabUI(position=(300, 300), size=(200, 200), nb_tabs=3)

showm = window.ShowManager(title="Tab Test")
showm.scene.add(tab_ui)
showm.start()
