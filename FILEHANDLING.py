#File handling means using python to create, read, and modify files.
# This is important because real programs often need to store data permanently.
# For example:
# User data
# Logs
# Configuration files
# Text files
# CSV files

#----Opening a File - open()--------
#basic syntax: 
# file = open("filename.txt", "mode")

# file = open("EXCEPTIONHANDLING.txt", "r")
# content = file.read()
# print(content)
# file.close()

#after running the above code it will give the error:cause windows is 
# trying to decode the file using cp1252 encoding, but your file contains some 
# characters that cannot be decoded using that encoding
# therefore,
# use "UTF-8 Encoding"

# with open("EXCEPTIONHANDLING.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)


#-------READING a file Line by Line-----------------
# with open("EXCEPTIONHANDLING.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line)


# You may see extra blank lines
# Because every line already contains a newline character (\n), and print() also adds a new line.
# A cleaner approach:
# with open("EXCEPTIONHANDLING.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())


#---------readline()----------------
# readline() reads one line at a time.

# with open("EXCEPTIONHANDLING.txt", "r", encoding = "utf-8") as file:
#     line1 = file.readline()
#     line2 = file.readline()

#     print(line1)
#     print(line2)

#--------readlines()--------------
# This reads all lines and stores them inside a Python list.
# with open("EXCEPTIONHANDLING.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

# print(lines)


#---------------WRITING TO A FILE--------------------
#now let's write data into a file
# with open("EXCEPTIONHANDLING.txt", "w", encoding = "utf-8") as file:
#     file.write("I am learning Python")



# with open("MYNOTES.txt", "w", encoding="utf-8") as file:
#     file.write("I am learning Python")

# If MYNOTES.txt doesn't exist:
# Python creates it.
# If it already exists:
# Python overwrites the old content.


# with open("MYNOTES.txt", "w", encoding="utf-8") as file:
#     file.write("Python\n")
#     file.write("Java\n")
#     file.write("JavaScript\n")
# Your file will contain:
# Python
# Java
# JavaScript
# Most Important: "w" Overwrites
# Suppose your file contains:
# Hello World
# Then you run:
# with open("MYNOTES.txt", "w", encoding="utf-8") as file:
#     file.write("Python")
# The file now becomes:
# Python
# Hello World is deleted.
# So remember:
# "w" = Write + Overwrite existing content.


#----------------Append Mode — "a"----------------- 

# If you don't want to delete existing content, use:

# "a"

# Example:

# with open("MYNOTES.txt", "a", encoding="utf-8") as file:
#     file.write("\nI am learning File Handling")

# Now the old content remains, and the new content is added.

#------------CREATE NEW FILE : "x" -----------------
with open("newfile.txt", "x", encoding = "utf-8") as file:
    file.write("Hello!")

# "x" means:

# Create a new file only.
# If the file already exists:
# FileExistsError
# So this is useful when you specifically want to avoid accidentally overwriting an existing file.

#-------------------Read + Write — "r+"-----------------------
#you can read and write using:
#"r+"

with open("mynotes.txt", "r+", encoding = "utf-8") as file:
    content = file.read()
    print(content)
    file.write("\nNew Content")

    
