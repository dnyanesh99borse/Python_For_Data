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