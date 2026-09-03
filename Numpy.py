# NUMPY — Topic 1: Introduction & NumPy Arrays
# What is NumPy?

# NumPy = Numerical Python

# It is a Python library mainly used for:

# Numerical computations
# Working efficiently with large datasets
# Arrays and matrices
# Mathematical operations
# Data Science and Machine Learning

# The main object in NumPy is:

#---ndarray---

# N-dimensional array

import numpy as np

numbers = np.array([1,2,3,4,5])

print(numbers * 2)


# NumPy vs Python List
# ----Python List----	 ----NumPy Array----
# General-purpose	         Numerical computing
# Can store mixed types	     Usually homogeneous data
# Slower for numerical       Faster
# operations	
# Requires loops often	     Vectorized operations
# Less memory efficient	     More memory efficient

# Interview answer:
# NumPy is used for efficient numerical computing. Its arrays are faster and more memory-efficient than Python lists and support vectorized mathematical operations.


#------CREATING A NUMPY ARRAY--------------

#---One-Dimensional Array
import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print(arr)

#---Two-Dimensional Array-----
import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)


#---Three Dimensional Array----- 
#(just know it)
import numpy as np
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr)


#----------IMPORTANT ARRAY PROPERTIES---------------
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

#---ndim---
# Tells the number of dimensions.
print(arr.ndim)

#---shape---
# tells the structure
print(arr.shape)

# output: (2, 3)
# Meaning:
# 2 rows
# 3 columns
# shape is extremely important in Data Science.

#---size---
print(arr.size)

#---dtype---
print(arr.dtype)


#--------INDEXING NUMPY ARRAYS------------

#--1D--
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

#--negative indexing works--
print(arr[-1])

#--2D--
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])

# means: arr[row, column]

#----------SLICING NUMPY ARRAYS---------------
# similar to Python lists

arr = np.array([10, 20, 30, 40, 50])
print(arr[1 : 4]) #o/p: 20 30 40

#2D Slicing
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

#--first row--
print(arr[0])

#--second column--
print(arr[: , 1]) #o/p: 20 50

# Understand this:
# arr[:, 1]

# Means:

# : → All rows
# 1 → Column index 1

# This syntax is very important.


# ----------Vectorized Operations---------
# This is one of the biggest strengths of NumPy.

# arr = np.array([1, 2, 3, 4])
# print(arr + 10)

# Output:
# [11 12 13 14]

# You can perform:
# arr * 2
# arr / 2
# arr ** 2

# All operations happen element by element.

# Example
# arr = np.array([1, 2, 3, 4])
# print(arr ** 2)

# Output:
# [ 1  4  9 16]



#======================NumPy Topic 2: Creating Arrays Efficiently=============================

# Previously, we created arrays manually using:

# np.array([1, 2, 3])

# But in Data Analysis, we often need to create arrays automatically.

# 1. np.zeros()

# Creates an array filled with 0.

# 1D array:
# import numpy as np

# arr = np.zeros(5)

# print(arr)

# Output:

# [0. 0. 0. 0. 0.]
# 2D array:
# arr = np.zeros((3, 4))

# print(arr)

# Output:

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# Remember:
# np.zeros((rows, columns))
# 2. np.ones()

# Creates an array filled with 1.

# arr = np.ones(5)

# print(arr)

# Output:

# [1. 1. 1. 1. 1.]
# 2D:
# arr = np.ones((2, 3))

# print(arr)

# Output:

# [[1. 1. 1.]
#  [1. 1. 1.]]
# 3. np.full()

# Creates an array filled with any value you want.

# arr = np.full(5, 10)

# print(arr)

# Output:

# [10 10 10 10 10]
# 2D example:
# arr = np.full((3, 3), 7)

# print(arr)

# Output:

# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]
# 4. np.arange() 

# Very important.

# Similar to Python's range(), but it creates a NumPy array.

# arr = np.arange(5)

# print(arr)

# Output:

# [0 1 2 3 4]
# Start and Stop
# arr = np.arange(1, 10)

# print(arr)

# Output:

# [1 2 3 4 5 6 7 8 9]

# The ending value is excluded.

# Step
# arr = np.arange(0, 20, 2)

# print(arr)

# Output:

# [ 0  2  4  6  8 10 12 14 16 18]
# Syntax:
# np.arange(start, stop, step)
# range() vs np.arange()
# range(5)

# Python range object

# np.arange(5)

# NumPy array

# For numerical operations, NumPy arrays are more useful.

# 5. np.linspace() 

# This is slightly different from arange().

# linspace() creates a specified number of equally spaced values.

# arr = np.linspace(0, 10, 5)

# print(arr)

# Output:

# [ 0.   2.5  5.   7.5 10. ]
# Syntax:
# np.linspace(start, stop, number_of_values)
# Important difference:
# arange()   → You specify the STEP

# linspace() → You specify the NUMBER OF VALUES

# Example:

# np.arange(0, 10, 2)

# You decide the step:

# 0, 2, 4, 6, 8

# But:

# np.linspace(0, 10, 5)

# You decide how many values you want:

# 0, 2.5, 5, 7.5, 10

# This difference is a good interview point.

# 6. Random Arrays 

# NumPy can generate random data.

# First:

# import numpy as np
# np.random.rand()

# Creates random decimal values between 0 and 1.

# arr = np.random.rand(5)

# print(arr)

# Example:

# [0.23 0.87 0.45 0.12 0.67]

# Every run may give different values.

# 2D:
# arr = np.random.rand(3, 2)

# print(arr)
# np.random.randint()

# Generates random integers.

# arr = np.random.randint(1, 10, 5)

# print(arr)

# This generates 5 random integers between:

# 1 → included
# 10 → excluded

# Example:

# [4 7 2 9 5]
# 2D example:
# arr = np.random.randint(1, 100, (3, 4))

# print(arr)
# 7. reshape()

# This is one of the most important NumPy concepts.

# Suppose:

# arr = np.arange(1, 13)

# print(arr)

# Output:

# [ 1  2  3  4  5  6  7  8  9 10 11 12]

# Now convert it into a matrix:

# new_arr = arr.reshape(3, 4)

# print(new_arr)

# Output:

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# Rule 

# The total number of elements must remain the same.

# 3 × 4 = 12 

# You cannot do:

# arr.reshape(5, 5)

# Because:

# 5 × 5 = 25 

# but the array has only 12 elements.

# Using -1 in reshape() 
# NumPy can automatically calculate one dimension.

# arr = np.arange(12)

# arr.reshape(3, -1)

# NumPy calculates:

# 12 ÷ 3 = 4

# Result shape:

# (3, 4)

# Similarly:

# arr.reshape(-1, 2)

# Result:

# (6, 2)

# Very useful when working with datasets.

# 8. flatten()

# Converts a multi-dimensional array into a 1D array.

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# flat = arr.flatten()

# print(flat)

# Output:

# [1 2 3 4 5 6]

# So:

# 2D → 1D
# Important Functions from This Topic

# You should remember these:

# np.zeros()
# np.ones()
# np.full()
# np.arange()
# np.linspace()
# np.random.rand()
# np.random.randint()
# reshape()
# flatten()
# Quick Cheat Sheet
# Function	Purpose
# np.zeros(5)	Array of zeros
# np.ones(5)	Array of ones
# np.full(5, 10)	Fill with a value
# np.arange()	Create values using a step
# np.linspace()	Create equally spaced values
# np.random.rand()	Random decimals
# np.random.randint()	Random integers
# reshape()	Change array shape
# flatten()	Convert to 1D

