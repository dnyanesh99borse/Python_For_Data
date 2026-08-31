#------------------Topic 3: Tuples------------------------

 
# collection whose contents you generally don't want to change.

#-----creating a Tuple-------------------

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(numbers[0])
print(numbers[2])

#---slicing----
print(numbers[1:3])

print(numbers[1:5])

#-----MAIN DIFFERENCE IN LIST AND TUPPLE--------------------
# 2. Main Difference: List vs Tuple ⭐⭐⭐
# List
# numbers = [10, 20, 30]
# numbers[0] = 100

#--Allowed.

# Tuple
# numbers = (10, 20, 30)
# numbers[0] = 100

#---Error.

# A tuple is immutable.

# List → mutable
# Tuple → immutable

# This is the most important thing to remember.

student = ("Dnyanesh", 22, "Computer Science")
print(student)


# Tuple with One Element
# This is a common Python beginner mistake.

#This is not a tuple:
x = (10) #python treat it as an integer

x = (10,) #this is a tuple.. comma needed here..


#----Tuple Unpacking----
#One of Python's very useful features.

student = ("Dnyanesh",22,"Python")

name, age, language = student

print(name)
print(age)
print(language)

#----------swapping Variables-------------
a = 10
b = 20

a, b = b, a 

print(a)
print(b)

#----------Tuple Methods-----------
#1. count()
numbers = (10, 20, 10, 30, 10)
print("count: ", numbers.count(10))

#index()
print(numbers.index(20))


