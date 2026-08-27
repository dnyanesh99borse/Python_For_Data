#----------------SETS--------------
#A set stores unique values.

numbers = {10, 20, 30, 40}

#1. Duplicate Values
numbers = {10, 20, 10, 30, 20}
print(numbers)

#Set is Unordered
# Don't depend on positions:
# numbers = {10, 20, 30}
# # numbers[0]
# You cannot access set elements using indexes like:
# numbers[0]

numbers = {10, 20, 10, 30, 20}
# Adding Elements
numbers.add(40)
print(numbers)
# Removing Elements
numbers.remove(20)
numbers.discard(20)
print(numbers)


# Difference
# remove() → gives an error if element doesn't exist.
# discard() → does nothing if element doesn't exist.

#-----------SET OPERATIONS-----------------
#This is where sets become very useful.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#UNION : Everything from both sets.
print(A | B)

#INTERSECTION : Common elements.
print(A & B) #OR
print(A.intersection(B))

#Difference.
print(A - B)

#SYMMETRIC DIFFERENCE: Elements that are in either set, but not both
set = A ^ B
print(set)

