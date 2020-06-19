# def contour_from_label(data, affine=None,
#                        color=None, opacity=1):
#     """Generate surface actor from a binary labeled Array.

#     The color and opacity of the surface can be customized.

#     Parameters
#     ----------
#     data : array, shape (X, Y, Z)
#         A labeled array file that will be binarized and displayed.
#     affine : array, shape (4, 4)
#         Grid to space (usually RAS 1mm) transformation matrix. Default is None.
#         If None then the identity matrix is used.
#     color : (N, 3) ndarray
#         RGB values in [0,1]. Default is None.
#         If None then random colors are used.
#     opacity : float
#         Opacity of surface between 0 and 1.

#     Returns
#     -------
#     contour_assembly : vtkAssembly
#         Tuple of Array surface object displayed in space
#         coordinates as calculated by the affine parameter
#         in the order of their roi ids.
#     """
#     if data.ndim != 3:
#         raise ValueError('Only 3D arrays are currently supported.')
#     else:
#         nb_components = 1

#     unique_roi_id = np.unique(data)

#     if color is None:
#         color = np.random.rand(len(unique_roi_id), 3)
#     elif color.shape != (len(unique_roi_id), 3):
#         raise ValueError("Incorrect color array shape")

#     if affine is None:
#         affine = np.eye(4)

#     # Set the transform (identity if none given)
#     transform = vtk.vtkTransform()
#     transform_matrix = vtk.vtkMatrix4x4()
#     transform_matrix.DeepCopy((
#         affine[0][0], affine[0][1], affine[0][2], affine[0][3],
#         affine[1][0], affine[1][1], affine[1][2], affine[1][3],
#         affine[2][0], affine[2][1], affine[2][2], affine[2][3],
#         affine[3][0], affine[3][1], affine[3][2], affine[3][3]))
#     transform.SetMatrix(transform_matrix)
#     transform.Inverse()

#     skin_extractor = vtk.vtkContourFilter()

#     for i, roi_id in enumerate(unique_roi_id):
#         if roi_id == 0:
#             continue
#         roi_data = np.isin(data, roi_id).astype(np.int)

#         vol = np.interp(roi_data,
#                         xp=[roi_data.min(), roi_data.max()], fp=[0, 255])
#         vol = vol.astype('uint8')

#         im = vtk.vtkImageData()
#         di, dj, dk = vol.shape[:3]
#         im.SetDimensions(di, dj, dk)
#         voxsz = (1., 1., 1.)
#         # im.SetOrigin(0,0,0)
#         im.SetSpacing(voxsz[2], voxsz[0], voxsz[1])
#         im.AllocateScalars(vtk.VTK_UNSIGNED_CHAR, nb_components)

#         vol = np.swapaxes(vol, 0, 2)
#         vol = np.ascontiguousarray(vol)

#         vol = vol.ravel()

#         uchar_array = numpy_support.numpy_to_vtk(vol, deep=0)
#         im.GetPointData().SetScalars(uchar_array)

#         image_resliced = vtk.vtkImageReslice()
#         set_input(image_resliced, im)
#         image_resliced.SetResliceTransform(transform)
#         image_resliced.AutoCropOutputOn()

#         rzs = affine[:3, :3]
#         zooms = np.sqrt(np.sum(rzs * rzs, axis=0))
#         image_resliced.SetOutputSpacing(*zooms)

#         image_resliced.SetInterpolationModeToLinear()
#         image_resliced.Update()

#         skin_extractor.SetInputData(image_resliced.GetOutput())
#         skin_extractor.SetValue(i, roi_id)

#     skin_normals = vtk.vtkPolyDataNormals()
#     skin_normals.SetInputConnection(skin_extractor.GetOutputPort())
#     skin_normals.SetFeatureAngle(60.0)

#     skin_mapper = vtk.vtkPolyDataMapper()
#     skin_mapper.SetInputConnection(skin_normals.GetOutputPort())
#     skin_mapper.ScalarVisibilityOff()

#     skin_actor = vtk.vtkActor()

#     skin_actor.SetMapper(skin_mapper)
#     skin_actor.GetProperty().SetOpacity(opacity)

#     skin_actor.GetProperty().SetColor(color[0], color[1], color[2])

#     return skin_actor

def contour_from_label(data, affine=None,
                       color=np.array([1, 0, 0]), opacity=1):
    """Generate surface actor from a binary labeled Array.
    The color and opacity of the surface can be customized.
    Parameters
    ----------
    data : array, shape (X, Y, Z)
        A labeled array file that will be binarized and displayed.
    affine : array, shape (4, 4)
        Grid to space (usually RAS 1mm) transformation matrix. Default is None.
        If None then the identity matrix is used.
    color : (1, 3) ndarray
        RGB values in [0,1].
    opacity : float
        Opacity of surface between 0 and 1.
    Returns
    -------
    tuple of contour_assembly : vtkAssembly
        Tuple of Array surface object displayed in space
        coordinates as calculated by the affine parameter
        in the order of their roi ids.
    """
    unique_roi_surfaces = vtk.vtkAssembly()

    unique_roi_id = np.unique(data)

    color = np.random.rand(len(unique_roi_id), 3)

    for i, roi_id in enumerate(unique_roi_id):
        if roi_id != 0:
            roi_surface = np.isin(data, roi_id).astype(np.int)
            roi_surface = contour_from_roi(roi_surface, affine, color=color[i], opacity=opacity)
            unique_roi_surfaces.AddPart(roi_surface)

    return unique_roi_surfaces
