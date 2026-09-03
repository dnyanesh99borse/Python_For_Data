








# ==4. Selecting Rows & Columns (loc and iloc)

# In real data analysis, you constantly need to select:

# Specific columns
# Specific rows
# Specific cells
# A range of rows/columns

# Let's learn them properly.

import pandas as pd

data = {
    "Name" : ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Age" : [22, 24, 21, 23, 25],
    "Department" : ["IT", "HR", "IT", "Finance", "HR"],
    "Salary" : [45000, 40000, 50000, 55000, 48000]
}

df = pd.DataFrame(data)

# print(df)


#----SELECTING COLUMNS----
#select one column
# print(df["Name"])

# print(df["Salary"])

#select multiple column
# print(df[["Name", "Salary"]])


#----Note----------
# df["Name"]              # One column → Series
# df[["Name", "Salary"]]  # Multiple columns → DataFrame


#============SELECTING ROW USING: 'iloc'=================
# iloc means: Integer Location
# It selects data using position/index numbers.

# Select One Row
print(df.iloc[0]) #gets the first row

print(df.iloc[2]) #gets the third row

# Remember: 0 → First row
#           1 → Second row
#           2 → Third row


#-----SELECT MULTIPLE ROWS---------
# df.iloc[0:3]     Output: Rows → 0, 1, 2
                   #Just like Python slicing, the ending index is excluded.


#=======Selecting Rows Using loc===========
# loc means: Label Location
# It selects data using labels.

# With our current DataFrame:
# 0
# 1
# 2
# 3
# 4

# these happen to look like numbers, but they are labels.

# print(df.loc[0])   #Gets the row with label 0.

# Important Difference: loc vs iloc
# loc	                         iloc
# Uses labels	             Uses positions
# Label-based	             Integer-position based
# Slice end is included	     Slice end is excluded

df.loc[0:2]  #gets: 0, 1, 2
df.iloc[0:2] #get: 0, 1



#=========SELECTING SPECIFIC ROWS AND COLUMNS WITH LOC===========
#---------USING LOC--------------
#syntax: 
        #  df.loc[row_selection, column_selection]

print(df.loc[0, "Name"])   #o/p: Amit


#select multiple rows and columns
print(df.loc[0:2, ["Name", "Salary"]])

# This selects: Rows 0 to 2 &
# Name and Salary columns

#----------USING ILOC----------
#syntax: 
        # df.iloc[row_position, column_position]

print(df.iloc[0,1])    #Row: 0, Column: 1

#select multiple rows and columns
df.iloc[0:3, 0:2]     #rows: 0, 1, 2
                      #columns: 0 and 1


#selecting specific columns using iloc
#Remeber the column positions:
# 0 → Name
# 1 → Age
# 2 → Department
# 3 → Salary

print(df.iloc[:,0])  #Gets the Name column.
#means    -All rows
#         -Column 0

print(df.iloc[:, [0, 3]])   #Gets Name + Salary column and all rows






# Real-World Examples 
# Get Name and Salary
# df[["Name", "Salary"]]
# Get the first 3 employees
# df.iloc[0:3]
# Get employee at row 2
# df.loc[2]
# Get Salary of Priya's row
# df.loc[3, "Salary"]
# Get Name and Department for the first 3 employees
# df.loc[0:2, ["Name", "Department"]]
# The Golden Rule
# Use loc when you know:

# Row/Column Labels

# df.loc[0, "Name"]
# Use iloc when you know:

# Positions

# df.iloc[0, 0]
# Quick Cheat Sheet
# # One column
# df["Name"]

# # Multiple columns
# df[["Name", "Salary"]]

# # iloc → position
# df.iloc[0]
# df.iloc[0:3]
# df.iloc[0, 1]
# df.iloc[:, 0]

# # loc → labels
# df.loc[0]
# df.loc[0:2]
# df.loc[0, "Name"]
# df.loc[0:2, ["Name", "Salary"]]
# Practice Questions

# Using our df:

# Q1
# Select only:
# Name
# Salary

# Q2
# Select the first 3 rows using iloc.

# Q3
# Select rows from 0 to 2 using loc.
# Notice the difference.

# Q4
# Get the:
# Name and Department
# of rows 1 to 3.

# Q5
# Using iloc, get:
# Rows 1 to 3
# Columns Name and Age

# Interview Question
# What is the difference between loc and iloc?

# Answer:
# loc is label-based indexing, while iloc is integer position-based indexing. Also, label slicing with loc includes the ending label, whereas slicing with iloc excludes the ending position.