import fury.ui as ui
import fury.window as window
values = ['abcdefghijklmnopqrstuvwxyz', 'ahdfjkhkashdfjkhdskfhiweuroqweqr', 'akdiuhdaiufhasdfusdffsdfusdyf', 'Soham', '012345678901234567', 'dfhfsjkljfhsakljfhsjkaljhfajklhgsfajkljhgajkljhkakjljhaklhgfakljhgfajh']
listbox = ui.ListBox2D(values=values, size=(300, 300))
sm=window.ShowManager(size=(600,600))
sm.scene.add(listbox)
sm.start()
