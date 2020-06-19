from fury import ui, window

range_slider_hor = ui.RangeSlider(
    line_width=8, handle_side=25, range_slider_center=(200, 500),
    value_slider_center=(200, 400), length=250, min_value=0,
    max_value=10, font_size=18, range_precision=2, value_precision=4,
    shape="square")
    
range_slider_ver = ui.RangeSlider(
    line_width=8, handle_side=25, range_slider_center=(475, 450),
    value_slider_center=(375, 450), length=250, min_value=0,
    max_value=10, font_size=18, range_precision=2, value_precision=4,
    orientation="vertical", shape="square")
    
current_size = (800, 800)
show_manager = window.ShowManager(size=current_size, title="Range Sliders Example")
show_manager.scene.add(range_slider_hor)
show_manager.scene.add(range_slider_ver)
show_manager.start()
