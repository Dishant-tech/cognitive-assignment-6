import numpy as np

# Given data
y = np.array([40, 65, 30, 85])

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

# a. Shape and dimensions
print("Shape:", X.shape)
print("Dimensions:", X.ndim)

# b. Transpose
print("\nX.T:")
print(X.T)

# c. X.T @ X
XT_X = X.T @ X
print("\nX.T @ X:")
print(XT_X)

# d. Inverse
inverse = np.linalg.inv(XT_X)
print("\nInverse:")
print(inverse)

# e. OLS equation
XT_y = X.T @ y
beta = inverse @ XT_y

print("\nCoefficients:")
print(beta)

# f. Coefficients
print("\nSleep coefficient:", beta[0])
print("Activity coefficient:", beta[1])
print("Stress coefficient:", beta[2])

# g. Prediction
new_user = np.array([5, 40, 7])

prediction = new_user @ beta

print("\nPredicted assistance score:", prediction)
