import numpy as np

# a. Create the original array
original = np.array([1, 2, 3, 4, 5, 6])
print("Original:", original)


# b. Create a slice from index 1 to 4
subset = original[1:5]
print("Subset:", subset)


# c. Modify the first element of subset
subset[0] = 999

print("After modifying subset:")
print("Original:", original)
print("Subset:", subset)


# d. Create another slice using copy()
copied = original[1:5].copy()

copied[0] = 500

print("\nAfter modifying copied array:")
print("Original:", original)
print("Copied:", copied)


# e. Create numbers from 1 to 12 and reshape into 3 x 4
matrix = np.arange(1, 13).reshape(3, 4)

print("\n3 x 4 Matrix:")
print(matrix)


# f. Indexing and slicing

# First row
print("\nFirst row:")
print(matrix[0, :])

# Last row
print("\nLast row:")
print(matrix[-1, :])

# Second column
print("\nSecond column:")
print(matrix[:, 1])

# Rows 1-2 and columns 2-3
print("\nRows 1-2 and columns 2-3:")
print(matrix[1:3, 2:4])


# g. Flatten and ravel
flat_array = matrix.flatten()
ravel_array = matrix.ravel()

print("\nFlatten:")
print(flat_array)

print("\nRavel:")
print(ravel_array)


# h. Modify ravel array
ravel_array[0] = 1000

print("\nAfter modifying ravel:")
print("Ravel:", ravel_array)
print("Original matrix:")
print(matrix)


# i. Modify flatten array
flat_array[1] = 2000

print("\nAfter modifying flatten:")
print("Flatten:", flat_array)
print("Original matrix:")
print(matrix)


# j. Display shape, ndim, size, dtype
print("\nMatrix properties:")
print("Shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data type:", matrix.dtype)
