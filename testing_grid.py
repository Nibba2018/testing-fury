from fury.utils import vtk
from fury import ui, window

linesPolyData = vtk.vtkPolyData()

pts = vtk.vtkPoints()
count = 0

for i in range(0, 1800, 30):
	pts.InsertNextPoint([0, i, 0])
	pts.InsertNextPoint([800, i, 0])
	pts.InsertNextPoint([i, 0, 0])
	pts.InsertNextPoint([i, 800, 0])
	count += 1

linesPolyData.SetPoints(pts)

lines = vtk.vtkCellArray()

for i in range(0, count+1, 4):
	h_line = vtk.vtkLine()
	v_line = vtk.vtkLine()
	
	h_line.GetPointIds().SetId(0,i)
	h_line.GetPointIds().SetId(1, i+1)
	
	v_line.GetPointIds().SetId(0, i+2)
	v_line.GetPointIds().SetId(1, i+3)
	
	lines.InsertNextCell(h_line)
	lines.InsertNextCell(v_line)

linesPolyData.SetLines(lines)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(linesPolyData)

grid = vtk.vtkActor()
grid.SetMapper(mapper)
grid.GetProperty().SetLineWidth(1)

current_size = (800, 800)
show_manager = window.ShowManager(size=current_size, title="DIPY UI Example")

show_manager.scene.add(grid)
show_manager.start()
