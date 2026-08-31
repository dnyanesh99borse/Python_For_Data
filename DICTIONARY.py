# What is a Dictionary?

# A dictionary stores data in key → value pairs.

#------SIMILAR TO HASHMAP OF THE JAVA---------------
student = {
    "name" : "Dnyanesh",
    "age" : 22,
    "branch" : "Information Technology"
}

#Accessing Values
student = {
    "name" : "Dnyanesh",
    "age" : 22
}
print(student["name"])
print(student["age"])

# You access a dictionary using its key, not an index.

# You access a dictionary using its key, not an index.
student = {
    "name" : "Dnyanesh",
    "age" : 22
}
student["city"] = "Pune"
print(student)
print(student["city"])

# Updating a Value
student["age"] = 23

# Removing Elements: pop(), clear()
student.pop("age") #removes the key value pair
del student["city"]
print(student)

# Checking if a Key Exists
#USE in
student = {
    "name" : "Dnyanesh",
    "age" : 22
}

print("name" in student) #True

if "age" in student:
    print("Age exists")

#------get()----------------
student = {
    "name" : "Dnyanesh",
    "age" : 22
}
print(student.get("name"))

#-----------get() vs student["city"] = ?----------------------
# get() will show you: None if error occurs
# student["city"] this can cause a KeyError if "city" doesn't exist.

#---------------------#Getting Keys, Values and Items--------------------
student = {
    "name": "Dnyanesh",
    "age": 22,
    "branch": "CS"
}

#---keys(): gives the dictionary's keys.
print(student.keys())

#---values(): gives the dictionary's values
print(student.values())

#give key-value pairs
print(student.items())


#-------------Looping Through a Dictionary--------------
for key,value in student.items():
    print(key, value)

#Nested Dictionaries
# A dictionary can contain another dictionary
students = {
    "student1":{
        "name" : "Rahul",
        "age" : 21
    },
    "student2":{
        "name": "Amit",
        "age":22
    }
}

print(students["student1"]["name"])

#---------------Dictionary with List--------
student = {
    "name": "Dnyanesh",
    "marks": [85, 90,78]
}

print(student["marks"][0])

#-------------Dictionary Comprehension----------------
squares = {}

for i in range(1, 6):
    squares[i] = i * i

print(squares)

#------------but using dictionary you can directly write-----------
squares = {i : i * i for i in range(1,6)}
print(squares)
