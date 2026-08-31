# Strings are extremely important because you'll use them everywhere—in input handling, files, APIs, data processing, and coding interviews.

# A string is a sequence of characters.
#Strings are immutable

#----REVERSE A STRING-------------
name = "Dnyanesh"
print(name[::-1])


#---------IMPORTANT STRING METHODS------------
# Important String Methods Summary
# Method	Purpose
# upper()	Uppercase
# lower()	Lowercase
# strip()	Remove outer spaces
# replace()	Replace text
# split()	String → List
# join()	List → String
# find()	Find position
# count()	Count occurrences
# isdigit()	Check digits
# isalpha()	Check letters
# isalnum()	Check letters + numbers


#--------palindrome----------
str = "madamu" #not palindrome

str2 = str[::-1]
if str == str2:
    print("isPalindrome")
else:
    print("notPalindrome")



#--------count Vowels----------
str = "Hello python"
vowels = ('a','e','i','o','u')
count = 0

for char in str:
    if char in vowels:
        count += 1

print(count)


#--------Word Count----------
str = "I am learning Python programming"

newstr = str.split()
print(len(newstr)) #will print the count of words



#--------Character Frequency----------
str = "programming"
dict = {}

for char in str:
    if char in dict:
        dict[char] = dict.get(char)+1
    else:
        dict[char] = 1

print(dict) 
