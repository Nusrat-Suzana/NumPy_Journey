import numpy as np

# From a list
array_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", array_from_list)

# Using built-in functions
zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
ones_array = np.ones((3, 2))     # 3x2 array of ones
print("Zeros array:\n", zeros_array)
print("Ones array:\n", ones_array)

print("\n")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
sum_array = a + b
print("Sum:", sum_array)

# Element-wise multiplication
product_array = a * b
print("Product:", product_array)

print("\n")

array = np.array([10, 20, 30, 40, 50])

# Accessing elements
print("First element:", array[0])
print("Last element:", array[-1])

# Slicing
sub_array = array[1:4]  # Elements from index 1 to 3
print("Sliced array:", sub_array)

# Modifying an element
array[2] = 100
print("Modified array:", array)

print("\n")

# built-in functions to compute statistics.

data = np.array([10, 20, 30, 40, 50])

mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
