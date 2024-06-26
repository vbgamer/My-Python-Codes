import numpy as np

# Example arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate arrays
concatenated_arr = np.concatenate((arr1, arr2))

# Apply mathematical operators
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2


print("Concatenated array:")
print(concatenated_arr)
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
