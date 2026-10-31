import numpy as np

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

# a. Total steps
print("Total steps:", np.sum(steps))

# b. Mean
print("Mean steps:", np.mean(steps))

# c. Maximum and minimum
print("Maximum:", np.max(steps))
print("Minimum:", np.min(steps))

# d. Total for each day
print("Total steps for each day:", np.sum(steps, axis=0))

# e. Total for each user
print("Total steps for each user:", np.sum(steps, axis=1))

# f. Position of maximum value
position = np.unravel_index(np.argmax(steps), steps.shape)
print("Position of maximum:", position)
print("Maximum value:", steps[position])
