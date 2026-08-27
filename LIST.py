#--------LIST IS LIKE ARRAYLIST IN PYTHON----------------------

#It can store all type of data like: [int, String, bool] etc
#List is Mutable

list = [10,20,30,40,50,60]

print(list)

#----------LOOPING THROUGH LIST---------------
list = [10,20,30,40,50,60]
for i in list:
    print(i)

#---------ACCESSING ELEMENT USING INDEX-----------
list = [10,20,30,40,50,60]

print(list[0])
print(list[2])
print(list[5])

#-------Negative indexing-----------
#Note: Negative Indexing in python starts from " -1 "
list = [10,20,30,40,50,60]

print(list[-1])
print(list[-2])
print(list[-5])


#------------CHANGING ELEMENTS--------------
numbers = [10, 20, 30]

numbers[1] = 100
numbers[2] = 300
print(numbers)

#-------------ADDING ELEMENTS-----------------
#----append()
data = [10, "Python", 3.14, True]

data.append("banana")
data.append("keliii")
print(data)

#-------------ADDING ELEMENTS-----------------
#----add at specific posistion----------
#---as we'll move inserting the elements their postiions will change
#----insert(idx, element)


numbers = [10, 100, 20, 30, 40]
numbers.insert(2,999)
numbers.insert(0,101)
print(numbers)

#---------------REMOVING ELEMENTS-------------
#-----------It removes the first occurrence-------------------
#----remove(element)
numbers = [10, 100, 20, 30, 40]

numbers.remove(20)
numbers.remove(40)
print(numbers)


#---------------Removes an element using its index.------------
#----pop(idx)
numbers = [10, 20, 30]

numbers.pop(1)
# numbers.pop(2) #this will throw error cause after removing 1st element there's no idx = 2

numbers.pop(1)
print(numbers)

#pop() without index will remove the last element
numbers.pop()
print(numbers)


#------del()------
# You can also delete using del.
numbers = [10, 20, 30]

del numbers[1]
print(numbers)


#---------len()-----------------------
#It is used to compute the length of list

numbers = [10, 20, 30, 40]

length = len(numbers)
print(length)


#---------Checking if an Element Exists-----------
numbers = [10, 20, 30, 40]

print(20 in numbers) #true

print(90 not in numbers) #True

print(40 not in numbers) #False


#===============LIST SLICING==========================
#list[start:end]
numbers = [10, 20, 30, 40, 50]


print(numbers[1:4]) #LAST IDX EXCLUDED
print(numbers[1:5]) #you can include like this

print(numbers[:2]) #starting idx is 0 and upto that elem

print(numbers[2:]) #from idx 2 last idx including

print(numbers[:]) #COPIES THE WHOLE LIST


#------------------STEP OR INTERVAL SLICING-------------------------
#    [start : end : step]
numbers = [10, 20, 30, 40, 50]

print(numbers[::2]) #step of 2

print(numbers[1:4:2]) #step of 3 (in our way 2)

#----------------Reverse a List----------------
numbers = [10, 20, 30, 40, 50]
list = numbers[::-1]
print(list)


#-----------IMPORTANT METHODS-----------------------------
# 10. Important List Methods

# You should know these:

# Method	Purpose
# append()	Add at end
# insert()	Add at position
# remove()	Remove value
# pop()	Remove by index / last
# sort()	Sort list
# reverse()	Reverse list
# count()	Count occurrences
# index()	Find index
# clear()	Remove everything


numbers = [30, 10, 20, 10]
numbers.count(10)
print(numbers.sort())
print(numbers)



# One important difference: sort() vs sorted()
# sort()

# Changes the original list:

# numbers.sort()
# sorted()

# Returns a new sorted list:

# numbers = [30, 10, 20]

# new_numbers = sorted(numbers)

# print(numbers)
# print(new_numbers)


#--------------FIND THE LARGEST NUMBER WITHOUT USING MAX()----------------------
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(numbers[-1])  # Prints 9



#------------------MAXIMUM SUMARRAY SUM-----------------
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum = 0
maxsum = numbers[0]  # Fixed: Start with the first number instead of 0

# Fixed: Use range(len()) so 'i' is a valid list index (0, 1, 2...)
for i in range(len(numbers)):
    if numbers[i] < 0:
        sum = 0
    else:
        sum += numbers[i]
        maxsum = max(maxsum, sum)
    maxsum = max(maxsum, sum)
print(maxsum)
