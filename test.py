import numpy as np

grid = np.random.randint(2, size=(10, 5))

# print(grid)
print("\n")

pattern = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

# Replicate the pattern to fill the grid
grid2 = np.tile(pattern, (10 // len(pattern), 1))

# print(grid2)


griddd = np.zeros((2, 2))
print(griddd)
