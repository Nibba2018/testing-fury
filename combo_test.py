from fury import window, actor, ui

values = ["An Item" + str(i) for i in range(5)]
new_values = [str(i) for i in range(5)]

combobox = ui.ComboBox2D(
    items=values, position=(0, 100), size=(300, 200), draggable=True)
# disk = ui.Disk2D(10, center=(0, 100))

# count = 0
# def add_val(combobox):
#     global count
#     combobox.append_item("Test" + str(count))
#     count += 1

# def add_val_disk(i_ren, obj, element):
#     global count, combobox
#     combobox.append_item("Test" + str(count))
#     count += 1


# combobox.position = (0, 100)
# print(combobox.size)
# combobox.resize((150, 100))
# print(combobox.size)
# disk.on_left_mouse_button_clicked = add_val_disk
combobox.append_item(*new_values)
# combobox.on_change = add_val
showm = window.ShowManager(title="ComboBox UI Test")
showm.scene.add(combobox)
showm.start()