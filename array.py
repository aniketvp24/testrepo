import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array: \n", arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array: \n", arr_2d)

arr_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print("3D Array: \n", arr_3d)

arr1 = np.array([[[10, 22, 43], [64, 5, 16], [17, 8, 29]]])
arr2 = np.array([[[50, 21, 3], [42, 1, 6], [67, 28, 9]]])

print("Dimension of arr1 = ", arr1.ndim)

print("\narr1 = \n", arr1)
print("arr2 = \n", arr2)

#Matrix Add
print("arr1 + arr2 = \n", arr1 + arr2)

#Matrix Subtract
print("arr1 - arr2 = \n", arr1 - arr2)

#Matrix Multiply
print("arr1 * arr2 = \n", arr1 * arr2)








