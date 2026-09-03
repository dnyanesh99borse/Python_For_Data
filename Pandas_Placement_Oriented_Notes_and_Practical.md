# Pandas — Placement-Oriented Notes & Practical Guide

> **Level:** Fresher / Data Analyst / Data-related roles  
> **Goal:** Learn the important Pandas concepts without unnecessary depth.

---

# 1. Introduction

```python
import pandas as pd
```

Pandas is a Python library used for:

- Reading datasets
- Cleaning data
- Manipulating tabular data
- Filtering data
- Analyzing data
- Grouping and aggregating data

## Main Data Structures

- **Series** → 1-dimensional labeled data
- **DataFrame** → 2-dimensional tabular data

---

# 2. Pandas Series

```python
numbers = pd.Series([10, 20, 30, 40])
print(numbers)
```

Custom index:

```python
marks = pd.Series(
    [85, 90, 75],
    index=["Math", "Science", "English"]
)

print(marks["Math"])
```

---

# 3. Pandas DataFrame

```python
data = {
    "Name": ["Amit", "Rahul", "Sneha"],
    "Age": [22, 24, 21],
    "Salary": [45000, 40000, 50000]
}

df = pd.DataFrame(data)
print(df)
```

A DataFrame contains:

- Rows
- Columns
- Index
- Different data types

---

# 4. Understanding a Dataset

```python
df.head()
df.head(3)

df.tail()
df.tail(3)

df.shape
df.columns
df.dtypes
df.index
```

## Important Dataset Exploration

```python
df.info()
df.describe()
df.nunique()
```

For categorical columns:

```python
df.describe(include="object")
```

Unique values:

```python
df["Department"].unique()
df["Department"].nunique()
```

Frequency:

```python
df["Department"].value_counts()
```

---

# 5. Reading CSV and Excel Files

## CSV

```python
df = pd.read_csv("employees.csv")
```

## Excel

```python
df = pd.read_excel("employees.xlsx")
```

Specific Excel sheet:

```python
df = pd.read_excel(
    "company_data.xlsx",
    sheet_name="Employees"
)
```

If required:

```bash
pip install openpyxl
```

## Saving Data

```python
df.to_csv("output.csv", index=False)

df.to_excel("output.xlsx", index=False)
```

---

# 6. Selecting Columns

One column:

```python
df["Name"]
```

Multiple columns:

```python
df[["Name", "Salary"]]
```

Remember:

```python
df["Name"]                 # Series

df[["Name", "Salary"]]     # DataFrame
```

---

# 7. loc and iloc

## iloc → Integer Position Based

```python
df.iloc[0]
df.iloc[0:3]

df.iloc[0, 1]

df.iloc[:, 0]

df.iloc[0:3, 0:2]
```

## loc → Label Based

```python
df.loc[0]

df.loc[0:2]

df.loc[0, "Name"]

df.loc[0:2, ["Name", "Salary"]]
```

## Difference

| loc | iloc |
|---|---|
| Label-based | Position-based |
| End label is included in slicing | End position is excluded |

---

# 8. Filtering Data

## One Condition

```python
df[df["Salary"] > 45000]

df[df["Age"] >= 22]

df[df["Department"] == "IT"]

df[df["Department"] != "HR"]
```

## AND

```python
df[
    (df["Age"] >= 22) &
    (df["Salary"] > 45000)
]
```

## OR

```python
df[
    (df["Department"] == "IT") |
    (df["Department"] == "HR")
]
```

## Multiple Values with isin()

```python
df[
    df["Department"].isin(["IT", "HR"])
]
```

## Range

```python
df[
    df["Age"].between(22, 25)
]
```

## String Filtering

```python
df[df["Name"].str.startswith("A")]

df[df["Name"].str.endswith("a")]

df[df["Name"].str.contains("h", case=False)]
```

## Filtering + Selecting Columns

```python
df.loc[
    df["Salary"] > 45000,
    ["Name", "Salary"]
]
```

---

# 9. Adding and Updating Columns

## Add Calculated Column

```python
df["Bonus"] = df["Salary"] * 0.10
```

## Add Fixed Value

```python
df["Company"] = "ABC Pvt Ltd"
```

## Update Column

```python
df["Salary"] = df["Salary"] * 1.10
```

## Conditional Update

```python
df.loc[
    df["Age"] < 23,
    "Category"
] = "Junior"
```

---

# 10. Renaming and Deleting Columns

## Rename

```python
df.rename(
    columns={"Salary": "Monthly_Salary"},
    inplace=True
)
```

## Delete

```python
df.drop(
    columns=["Age"],
    inplace=True
)
```

---

# 11. Missing Data Handling

Import NumPy when needed:

```python
import numpy as np
```

Example:

```python
df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Sneha"],
    "Age": [22, np.nan, 21],
    "Salary": [45000, 50000, np.nan]
})
```

## Detect Missing Values

```python
df.isnull()

df.isnull().sum()
```

## Remove Missing Values

```python
new_df = df.dropna()
```

Or:

```python
df = df.dropna()
```

## Fill Missing Values

Fixed value:

```python
df.fillna(0)
```

Mean:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

Median:

```python
df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)
```

Text:

```python
df["Name"] = df["Name"].fillna("Unknown")
```

### Mean vs Median

- **Mean** → useful when there are no major outliers
- **Median** → often better when outliers exist

---

# 12. Sorting

Ascending:

```python
df.sort_values("Salary")
```

Descending:

```python
df.sort_values(
    "Salary",
    ascending=False
)
```

Multiple columns:

```python
df.sort_values(
    ["Age", "Salary"],
    ascending=[True, False]
)
```

---

# 13. Basic Analysis Functions

```python
df["Salary"].min()

df["Salary"].max()

df["Salary"].mean()

df["Salary"].median()

df["Salary"].sum()

df["Salary"].count()
```

Top records:

```python
df.nlargest(3, "Salary")

df.nsmallest(3, "Salary")
```

---

# 14. groupby() and Aggregation

Example:

```python
df.groupby("Department")["Salary"].mean()
```

Total:

```python
df.groupby("Department")["Salary"].sum()
```

Maximum:

```python
df.groupby("Department")["Salary"].max()
```

Count:

```python
df.groupby("Department")["Name"].count()
```

## Multiple Aggregations

```python
df.groupby("Department")["Salary"].agg(
    ["count", "mean", "min", "max", "sum"]
)
```

Grouping by multiple columns:

```python
df.groupby(
    ["Department", "City"]
)["Salary"].mean()
```

---

# 15. Merging DataFrames

```python
employees = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Rahul", "Sneha"],
    "Dept_ID": [101, 102, 103]
})

departments = pd.DataFrame({
    "Dept_ID": [101, 102, 104],
    "Department": ["IT", "HR", "Finance"]
})
```

## Inner Join

```python
pd.merge(
    employees,
    departments,
    on="Dept_ID",
    how="inner"
)
```

## Left Join

```python
pd.merge(
    employees,
    departments,
    on="Dept_ID",
    how="left"
)
```

## Right Join

```python
pd.merge(
    employees,
    departments,
    on="Dept_ID",
    how="right"
)
```

## Outer Join

```python
pd.merge(
    employees,
    departments,
    on="Dept_ID",
    how="outer"
)
```

### Remember

- **inner** → only matching records
- **left** → everything from left DataFrame
- **right** → everything from right DataFrame
- **outer** → everything from both

---

# 16. Duplicates

Check duplicates:

```python
df.duplicated()
```

Count duplicates:

```python
df.duplicated().sum()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

Based on specific columns:

```python
df = df.drop_duplicates(
    subset=["Name"]
)
```

---

# 17. Basic Data Cleaning

## Clean Column Names

```python
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
```

Example:

```text
" Employee Name "
```

becomes:

```text
employee_name
```

## Clean Text Values

```python
df["Department"] = (
    df["Department"]
    .str.strip()
)
```

## Replace Values

```python
df["Gender"] = df["Gender"].replace({
    "Male": "M",
    "Female": "F"
})
```

## Change Data Type

```python
df["Age"] = df["Age"].astype(int)

df["Salary"] = df["Salary"].astype(float)
```

Check:

```python
df.dtypes
```

---

# 18. Final Practical Exercise — Employee Data Analysis

## Complete Code with Solution

```python
import pandas as pd
import numpy as np

# =====================================================
# STEP 1: CREATE A REALISTIC DEMO DATASET
# =====================================================

data = {
    "Employee ID": [101, 102, 103, 104, 105, 106, 106],
    "Name": [
        " Amit",
        "Rahul ",
        "Sneha",
        "Priya",
        "Rohan",
        "Anjali",
        "Anjali"
    ],
    "Department": [
        " IT",
        "HR ",
        "IT",
        "Finance",
        "HR",
        " IT",
        " IT"
    ],
    "Age": [22, 24, np.nan, 23, 25, 21, 21],
    "Salary": [
        45000,
        40000,
        50000,
        np.nan,
        48000,
        60000,
        60000
    ]
}

df = pd.DataFrame(data)

print("\n========== ORIGINAL DATA ==========")
print(df)


# =====================================================
# STEP 2: EXPLORE THE DATASET
# =====================================================

print("\n========== DATASET PREVIEW ==========")
print(df.head())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== COLUMNS ==========")
print(df.columns)

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== DATASET INFO ==========")
df.info()

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# =====================================================
# STEP 3: CLEAN COLUMN NAMES
# =====================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\n========== CLEAN COLUMN NAMES ==========")
print(df.columns)


# =====================================================
# STEP 4: CLEAN TEXT VALUES
# =====================================================

df["name"] = df["name"].str.strip()

df["department"] = df["department"].str.strip()

print("\n========== CLEANED TEXT DATA ==========")
print(df)


# =====================================================
# STEP 5: CHECK MISSING VALUES
# =====================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# =====================================================
# STEP 6: HANDLE MISSING VALUES
# =====================================================

# Fill missing age using mean
df["age"] = df["age"].fillna(
    df["age"].mean()
)

# Fill missing salary using median
df["salary"] = df["salary"].fillna(
    df["salary"].median()
)

print("\n========== AFTER HANDLING MISSING VALUES ==========")
print(df)

print("\nMissing Values Remaining:")
print(df.isnull().sum())


# =====================================================
# STEP 7: CHECK AND REMOVE DUPLICATES
# =====================================================

print("\n========== DUPLICATES ==========")
print("Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("\n========== AFTER REMOVING DUPLICATES ==========")
print(df)


# =====================================================
# STEP 8: FILTER DATA
# =====================================================

print("\n========== EMPLOYEES WITH SALARY > 45000 ==========")

high_salary = df[
    df["salary"] > 45000
]

print(high_salary)


# =====================================================
# STEP 9: ADD A BONUS COLUMN
# =====================================================

df["bonus"] = df["salary"] * 0.10

print("\n========== DATA WITH BONUS ==========")
print(df)


# =====================================================
# STEP 10: DEPARTMENT-WISE ANALYSIS
# =====================================================

department_analysis = (
    df.groupby("department")["salary"]
    .agg(["count", "mean", "min", "max", "sum"])
)

print("\n========== DEPARTMENT-WISE ANALYSIS ==========")
print(department_analysis)


# =====================================================
# STEP 11: SORT BY SALARY
# =====================================================

sorted_df = df.sort_values(
    "salary",
    ascending=False
)

print("\n========== SORTED BY SALARY ==========")
print(sorted_df)


# =====================================================
# STEP 12: TOP 3 HIGHEST PAID EMPLOYEES
# =====================================================

top_employees = df.nlargest(
    3,
    "salary"
)

print("\n========== TOP 3 HIGHEST PAID EMPLOYEES ==========")
print(top_employees[
    ["name", "department", "salary"]
])


# =====================================================
# STEP 13: FINAL INSIGHTS
# =====================================================

print("\n========== FINAL INSIGHTS ==========")

print("Total Employees:", len(df))

print(
    "Average Salary:",
    df["salary"].mean()
)

print(
    "Highest Salary:",
    df["salary"].max()
)

print(
    "Lowest Salary:",
    df["salary"].min()
)

print(
    "\nEmployees Per Department:"
)

print(
    df["department"].value_counts()
)


# =====================================================
# STEP 14: SAVE CLEANED DATA
# =====================================================

df.to_csv(
    "cleaned_employee_data.csv",
    index=False
)

print(
    "\nCleaned dataset saved successfully!"
)
```

---

# 19. Professional Data Analysis Workflow

When you receive a new dataset, follow this order:

```python
# 1. Read data
df = pd.read_csv("dataset.csv")

# 2. Preview
df.head()

# 3. Understand structure
df.shape
df.columns
df.info()
df.describe()

# 4. Check missing values
df.isnull().sum()

# 5. Check duplicates
df.duplicated().sum()

# 6. Clean data
# - column names
# - text values
# - missing values
# - duplicates

# 7. Filter data

# 8. Analyze
# groupby()
# mean()
# sum()
# value_counts()

# 9. Find insights

# 10. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
```

---

# 20. Final Pandas Cheat Sheet

```python
import pandas as pd

# Read
pd.read_csv("file.csv")
pd.read_excel("file.xlsx")

# Explore
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.dtypes

# Select
df["column"]
df[["col1", "col2"]]

# Indexing
df.loc[]
df.iloc[]

# Filter
df[df["Age"] > 22]

# Missing values
df.isnull().sum()
df.dropna()
df.fillna()

# Duplicates
df.duplicated().sum()
df.drop_duplicates()

# Sorting
df.sort_values()

# Analysis
df["Salary"].mean()
df["Salary"].sum()
df["Salary"].max()

# Grouping
df.groupby("Department")["Salary"].mean()

# Multiple aggregation
df.groupby("Department")["Salary"].agg(
    ["count", "mean", "min", "max"]
)

# Merge
pd.merge(df1, df2, on="ID", how="left")

# Save
df.to_csv("output.csv", index=False)
```

---

# Final Placement-Level Conclusion

After mastering the topics in this document, you should be comfortable with the important Pandas fundamentals required for:

- Data Analyst fresher roles
- Data-related internships
- Basic EDA tasks
- Dataset cleaning
- College projects
- Placement interviews

## Most Important Topics to Be Strong In

1. `loc` and `iloc`
2. Filtering
3. Missing value handling
4. `groupby()`
5. `agg()`
6. Sorting
7. Duplicates and cleaning
8. `merge()`
9. Dataset exploration using `info()` and `describe()`

> **Focus on practicing these concepts with real datasets. Knowing syntax is useful, but being able to analyze a dataset and explain your findings is what makes you look like a real Data Analyst.**
