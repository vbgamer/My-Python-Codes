import numpy as np

# Example array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Extract odd numbers
odd_numbers = arr[arr % 2 != 0]

print("Odd numbers from the array:")
print(odd_numbers)
