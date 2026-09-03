








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


#====================FITERING DATA=========================
#Filtering means selecting only the data that matches a condition
# For example:
# Employees earning more than ₹50,000
# Students older than 21
# Employees from the IT department
# Sales from a particular region

import pandas as pd
data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Age": [22, 24, 21, 23, 25],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [45000, 40000, 50000, 55000, 48000]
}

df = pd.DataFrame(data)
print(df)


#Filtering with One Condition-----
#Employees with salary greater than 45000
print(df[df["Salary"] > 45000])


# Other Conditions
# Greater than or equal to
# df[df["Age"] >= 23]
# Less than
# df[df["Age"] < 23]
# Equal to 
# df[df["Department"] == "IT"]
# Not equal to
# df[df["Department"] != "HR"]

#----MULTIPLE CONDIIONS - AND(&)
#Employees older than 22 AND salary greater than 45000

output = df[
    (df["Age">22]) &
    (df["Salary"] > 45000)
]

#Employees from IT OR Finance.
output = df[
    (df["Department"] == "IT") |
    (df["Department"] == "Finance")
]


#---Important Operations----
# &  → AND
# |  → OR
# ~  → NOT


#========= isin() ===========
#Very useful when checking multiple values
#instead of:
df[
    (df["Department"] =="IT") |
    (df["Department"] == "HR")
]

#you can write: Cleaner and more professional.
df[df["Department"].isin(["IT", "HR"])]


#======== between() =========
#useful for filtering a range
df[df["Age"].between(22, 24)]

#this selects employees aged: 22 to 24
#By default, both endpoints are included.


#========= String Filtering ==================
#Sometimes you need to filter text.

#Names starting with "A"
df[df["Name"].str.startswith("A")]

#Names ending with "a"
df[df["Name"].str.endswith("a")]

#Names containing "h"
df[df["Name"].str.contains("h")]

#For case-insensitive search:
df[
    df["Name"].str.contains("H", case=False)
]


#========ADDING, UPDATING AND DELETING COLUMNS=========
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Sneha"],
    "Age": [22, 24, 21],
    "Salary": [45000, 40000, 50000]
})

#===Adding a New Column===
df["Bonus"] = df["Salary"]*0.10   #now every employee gets a 10% bonus.

print(df)
print(df["Bonus"])

#===Add a fixed value===
df["Company"] = "ABC Pvt Ltd"

#Updating a Column
#Increase everyone's salary by 10%
df["Salary"] = df["Salary"] * 1.10

#You can also update based on a condition:
df.loc[df["Age"] < 23, "Category"] = "Junior"

#===Renaming a Column===
df.rename(columns={"Salary": "Monthly_Salary"}, inplace = True)

#===Deleting a Column===
df.drop(columns=["Age"], inplace = True)

#--for multiple columns--
df.drop(columns=["Age","Salary"], inplace=True)



#============MISSING DATA HANDLING=============
#Missing data is extremely common in real datasets

import pandas as pd
import numpy  as np

df = pd.DataFrame({
    "Name" : ["Amit", "Rahul", "Sneha", "Priya"],
    "Age" : [22, np.nan, 21, np.nan],
    "Salary" : [45000, 50000, np.nan, 55000]
})

print(df,"\n")

#===Detect Missing Values===
#Check each value:
print(df.isnull())

#Count missing values
print(df.isnull().sum(),"\n")

#===Remove Missing Values===
# Removes rows containing missing values.
# Use carefully—you might lose important data.
#before: 
print(df)
df.dropna(inplace = True) #inplace=True helps to show the changes in this dataframe only
#after
print(df)


#===Fill Missing Values===
# Fill with a fixed value:
df["Age"] = df["Age"].fillna(0)
# Fill with Mean:
df["Age"] = df["Age"].fillna(df["Age"].mean())
# Fill with Median:
df["Age"] = df["Age"].fillna(df["Age"].median())
# Fill text values:
df["Name"] = df["Name"].fillna("Unknown")



#================= SORTING & BASIC DATA ANALYSIS ========================
#use this dataset:
import pandas as pd
df = pd.DataFrame({
    "Name" : ["Amit", "Rahul", "Sneha", "Priya"],
    "Age" : [22, 24, 21, 33],
    "Salary" : [45000, 40000, 50000, 55000]
})

#=== Sorting Data -- sort_values()
#Sort Salary in ascending order:
df.sort_values("Salary")

#Descending order:
df.sort_values("Salary", ascending = False)

#Sort by multiple columns:
df.sort_values(
    ["Age", "Salary"],
    ascending = [True, False]
)

#==== Basic Analysis Functions ====
#Minimum
print(df["Salary"].min())

#Maximum
print(df["Salary"].max())

#Average
print(df["Salary"].mean())

#Median
print(df["Salary"].median())

#Total
print(df["Salary"].median())

#Count
print(df["Salary"].count())


#=== GET Top/Bottom Records ===
#Highest 2 Salaries
df.nlargest(2, "Salary")

#Lowest 2 Salaries
df.nsmallest(2, "Salary")




#========== groupby() & Aggregation ==========
# groupby() is used when you want to group data by a category and perform calculations on each group.

# For example:
# Average salary by department
# Total sales by region
# Number of employees in each department
# Maximum salary in each department

#Demo Dataset
import pandas as pd
df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [45000, 40000, 50000, 55000, 48000]
})

print(df,"\n")

#==== Basic groupby() ====
#Find Average Salary by Department
avgsal = df.groupby("Department")["Salary"].mean()
print(avgsal)


#==== Other Aggregations ====
#Total Salary by Department
totalsaldept = df.groupby("Department")["Salary"].sum()
print(totalsaldept)

# Maximum Salary by Department
df.groupby("Department")["Salary"].max()

# Minimum Salary
df.groupby("Department")["Salary"].min()

# Number of Employees
df.groupby("Department")["Name"].count()



#=====rouping by Multiple Columns=====
# Suppose your dataset has:
# Department
# City
# Salary

# you can group by both:
df.groupby(
    ["Department", "City"]
)["Salary"].mean()

#This gives Average Salary for each Department + City combination



#============ MERGING AND JOINING DATAFRAMES ==============
#SIMILAR TO SQL JOINS

#In real projects, data is often stored in multiple tables/files
#eg:
#Employee Data
import pandas as pd
df1 = pd.DataFrame({
    "Employee_ID": [1, 2, 3, 4],
    "Name": ["Amit", "Rahul", "Sneha", "Priya"],
    "Department_ID": [101, 102, 101, 103]
})

#Department Data
df2 = pd.DataFrame({
    "Department_ID": [101, 102, 103],
    "Department": ["IT", "HR", "Finance"]
})

#we want to combine them using: pd.merge()

#=== Basic Merge ===
result = pd.merge(
    df1,
    df2,
    on = "Department_ID"
)

print(result)



#=============== TYPES OF JOINS ================

# These are important to understand.

# INNER JOIN
# pd.merge(df1, df2, on="Department_ID", how="inner")

# Keeps only matching records from both DataFrames.

# LEFT JOIN
# pd.merge(df1, df2, on="Department_ID", how="left")

# Keeps all records from the left DataFrame (df1).

# If no matching data exists in df2, Pandas puts NaN.

# RIGHT JOIN
# pd.merge(df1, df2, on="Department_ID", how="right")

# Keeps all records from the right DataFrame.

# OUTER JOIN
# pd.merge(df1, df2, on="Department_ID", how="outer")

# Keeps all records from both DataFrames.

# Missing matches become NaN.

# Easy Join Memory Trick
# INNER → Only common records

# LEFT  → Everything from left

# RIGHT → Everything from right

# OUTER → Everything from both
# Most Important Real-World Pattern

# Usually, you'll use:

# pd.merge(
#     df1,
#     df2,
#     on="Common_Column",
#     how="left"
# )

# Why?

# Because often you have a main dataset, and you want to add information from another dataset without losing rows from your main dataset.

# What About join()?

# Pandas also has:

# df1.join(df2)

# But for your current level:
# Focus mainly on pd.merge().

# It is clearer, more commonly used, and easier to understand.

# Quick Practice
# Create these:

# employees = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["Amit", "Rahul", "Sneha"],
#     "Dept_ID": [101, 102, 103]
# })

# departments = pd.DataFrame({
#     "Dept_ID": [101, 102, 104],
#     "Department": ["IT", "HR", "Finance"]
# })

# Try:
# 1. Inner Merge
# pd.merge(employees, departments, on="Dept_ID", how="inner")
# 2. Left Merge
# pd.merge(employees, departments, on="Dept_ID", how="left")
# 3. Outer Merge
# pd.merge(employees, departments, on="Dept_ID", how="outer")

# Observe carefully which rows are kept and where NaN appears. 🔥

# Must Remember for Interviews
# Pandas merge() combines DataFrames using a common column, similar to SQL joins. The main join types are inner, left, right, and outer joins.





#======================= DUPLICATES + BASIC DATA CLEANING ==========================
# Real-world datasets are often messy. Common problems include:

# Duplicate rows
# Missing values
# Incorrect column names
# Extra spaces in text
# Wrong data types

# Let's learn the important basics.


#===== DETECT DUPLICATE ROWS ======
import pandas as pd
df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Sneha", "Amit"],
    "Age": [22, 24, 21, 22],
    "Salary": [45000, 40000, 50000, 45000]
})
print(df)

#check duplicates:
print(df.duplicated())

#count duplicates
countdupli = df.duplicated().sum()
print(countdupli)


#====== REMOVE DUPLICATES =======
df = df.drop_duplicates()
print(df)  #now duplicate rows are removed


#====== CLEANING COLUMN NAMES ======
#Real datasets may have messy column names:
# " Employee Name "
# "Salary "
# " DEPARTMENT"

#Clean them:
df.columns = df.columns.str.strip()
print(df.columns)

#convert to Lowercase
df.columns = df.columns.str.lower()

#Replace spaces with underscores:
df.columns = df.columns.str.replace(" ","_")

# Professional combination
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print(df)

# Example:
# Employee Name
# becomes: 
# employee_name


#======== CLEANING TEXT VALUES ============
#Sometimes values contain unnecessary spaces.
# example:
# " IT "
# "HR "
# " Finance"

#clean a column
df["Department"] = df["Department"].str.strip()

#convert to lowercase
df["Department"] = df["Department"].str.lower()

#==== Replacing Values =====
# suppose: 
# Male --> M
# Female --> F

df["Gender"] = df["Gender"].replace({
    "Male":"M",
    "Female":"F"
})

df["Status"] = df["Status"].replace({
    "Yes": True,
    "No" : False
})


#===== CHANGING DATA TYPES =====
#Sometimes numerical data is stroed as text
# eg:
df["Age"] = df["Age"].astype(int)
# or
df["Salary"] = df["Salary"].astype(float)

print(df.types)


Basic Data Cleaning Workflow 🔥

When you receive a real dataset:

# Understand dataset
df.info()

# Missing values
df.isnull().sum()

# Duplicates
df.duplicated().sum()

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove duplicates
df = df.drop_duplicates()


# This is a very good fresher-level data cleaning workflow.

# Must Remember
# df.duplicated().sum()

# df.drop_duplicates()

# df.columns.str.strip()

# df["column"].str.strip()

# df.replace()

# df.astype()
# Quick Practice

# Try this:

# df = pd.DataFrame({
#     " Name ": [" Amit", "Rahul ", "Sneha", " Amit"],
#     "Department": [" IT", "HR ", "IT", " IT"],
#     "Salary": [45000, 40000, 50000, 45000]
# })

# Perform:
# Clean column names.
# Remove extra spaces from Name.
# Remove extra spaces from Department.
# Check duplicate rows.
# Remove duplicates.
# Print the final cleaned DataFrame.