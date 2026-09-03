# NumPy Preparation Notes for Placements

> **Goal:** Learn the important NumPy concepts required for placements, coding assessments, data-related roles, Python interviews, and basic Data Science preparation.
>
> These notes intentionally focus on **important and practical topics**, not every NumPy feature.

---

# 1. What is NumPy?

**NumPy** stands for **Numerical Python**.

It is a Python library mainly used for:

- Numerical computing
- Working with arrays
- Mathematical operations
- Matrix operations
- Data analysis and preprocessing
- Scientific computing

The main object in NumPy is:

```python
numpy.ndarray
```

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)
```

Output:

```text
[10 20 30 40]
```

---

# 2. Why NumPy Instead of Python Lists?

NumPy arrays are generally preferred for numerical work because they provide:

- Faster operations
- Less memory usage
- Vectorized calculations
- Multi-dimensional arrays
- Mathematical and statistical functions

### Python List

```python
numbers = [1, 2, 3, 4]

result = []

for x in numbers:
    result.append(x * 2)
```

### NumPy Array

```python
arr = np.array([1, 2, 3, 4])

result = arr * 2

print(result)
```

Output:

```text
[2 4 6 8]
```

This is called **vectorization**.

---

# 3. Creating NumPy Arrays

## From a Python List

```python
arr = np.array([1, 2, 3, 4])
```

## 2D Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## Important: Array Dimensions

### 1D Array

```python
np.array([1, 2, 3])
```

### 2D Array

```python
np.array([
    [1, 2],
    [3, 4]
])
```

### 3D Array

```python
np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
```

For placements, **1D and 2D arrays are the most important**.

---

# 4. Important Array Attributes

Consider:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## `ndim`

Returns the number of dimensions.

```python
arr.ndim
```

Output:

```text
2
```

---

## `shape`

Returns the structure of the array.

```python
arr.shape
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 rows
3 columns
```

---

## `size`

Returns the total number of elements.

```python
arr.size
```

Output:

```text
6
```

---

## `dtype`

Returns the data type.

```python
arr.dtype
```

Example output:

```text
int64
```

---

## Quick Interview Difference

| Attribute | Meaning |
|---|---|
| `ndim` | Number of dimensions |
| `shape` | Size of each dimension |
| `size` | Total elements |
| `dtype` | Data type |

---

# 5. Special NumPy Arrays

These are very commonly used.

## Zeros

```python
np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

2D:

```python
np.zeros((2, 3))
```

---

## Ones

```python
np.ones(5)
```

```python
np.ones((2, 3))
```

---

## Identity Matrix

```python
np.eye(3)
```

Output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

## Full Array

```python
np.full((2, 3), 7)
```

Output:

```text
[[7 7 7]
 [7 7 7]]
```

---

# 6. `arange()` and `linspace()`

## `np.arange()`

Similar to Python's `range()`.

```python
np.arange(1, 10)
```

Output:

```text
[1 2 3 4 5 6 7 8 9]
```

With step:

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

---

## `np.linspace()`

Creates equally spaced values.

```python
np.linspace(0, 10, 5)
```

Output:

```text
[ 0.   2.5  5.   7.5 10. ]
```

### Difference

- `arange()` → based on **step size**
- `linspace()` → based on **number of values**

---

# 7. Array Indexing

Consider:

```python
arr = np.array([10, 20, 30, 40, 50])
```

## Accessing Elements

```python
arr[0]
```

Output:

```text
10
```

```python
arr[-1]
```

Output:

```text
50
```

---

# 8. 2D Array Indexing

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Access:

```python
arr[0, 1]
```

Output:

```text
20
```

Meaning:

```text
row 0, column 1
```

Another example:

```python
arr[1, 2]
```

Output:

```text
60
```

---

# 9. Array Slicing

## 1D Slicing

```python
arr = np.array([10, 20, 30, 40, 50])
```

```python
arr[1:4]
```

Output:

```text
[20 30 40]
```

---

## 2D Slicing

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

Get first two rows:

```python
arr[:2]
```

Get specific rows and columns:

```python
arr[:2, 1:]
```

Output:

```text
[[2 3]
 [5 6]]
```

---

# 10. Changing Array Values

```python
arr = np.array([10, 20, 30])

arr[1] = 100

print(arr)
```

Output:

```text
[ 10 100  30]
```

For 2D arrays:

```python
arr[0, 1] = 999
```

---

# 11. Vectorized Operations

One of the **most important NumPy concepts for interviews**.

```python
arr = np.array([1, 2, 3, 4])
```

Addition:

```python
arr + 10
```

Multiplication:

```python
arr * 2
```

Division:

```python
arr / 2
```

Power:

```python
arr ** 2
```

Output:

```text
[ 1  4  9 16]
```

---

## Array-to-Array Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

```python
a + b
```

```text
[5 7 9]
```

```python
a * b
```

```text
[ 4 10 18]
```

### Important

`a * b` performs **element-wise multiplication**, not matrix multiplication.

---

# 12. Comparison Operations

```python
arr = np.array([10, 20, 30, 40])
```

```python
arr > 20
```

Output:

```text
[False False  True  True]
```

Other comparisons:

```python
arr == 20
arr < 30
arr >= 20
```

These Boolean results are important for filtering.

---

# 13. Boolean Indexing / Filtering

Very important for Data Analysis.

```python
arr = np.array([10, 20, 30, 40, 50])
```

Get values greater than 25:

```python
arr[arr > 25]
```

Output:

```text
[30 40 50]
```

Another example:

```python
arr[arr % 2 == 0]
```

This returns even numbers.

---

# 14. Aggregation Functions

Consider:

```python
arr = np.array([10, 20, 30, 40])
```

## Sum

```python
np.sum(arr)
```

## Mean

```python
np.mean(arr)
```

## Minimum

```python
np.min(arr)
```

## Maximum

```python
np.max(arr)
```

## Standard Deviation

```python
np.std(arr)
```

## Variance

```python
np.var(arr)
```

These are especially useful in **Data Science and Data Analyst interviews**.

---

# 15. `axis` Concept (VERY IMPORTANT)

Consider:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## `axis=0`

Operation happens **column-wise**.

```python
np.sum(arr, axis=0)
```

Output:

```text
[5 7 9]
```

Because:

```text
1+4
2+5
3+6
```

---

## `axis=1`

Operation happens **row-wise**.

```python
np.sum(arr, axis=1)
```

Output:

```text
[ 6 15]
```

### Easy Memory Trick

```text
axis=0 → move down rows → result for columns
axis=1 → move across columns → result for rows
```

This is a frequently asked concept.

---

# 16. Reshaping Arrays

Consider:

```python
arr = np.arange(1, 7)
```

Output:

```text
[1 2 3 4 5 6]
```

Reshape:

```python
arr.reshape(2, 3)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

### Rule

The total number of elements must remain the same.

```text
6 elements → (2 × 3) = 6
```

---

## Using `-1`

```python
arr.reshape(2, -1)
```

NumPy automatically calculates the remaining dimension.

---

# 17. Flattening Arrays

Convert a multi-dimensional array into 1D.

```python
arr = np.array([
    [1, 2],
    [3, 4]
])
```

## `flatten()`

```python
arr.flatten()
```

Output:

```text
[1 2 3 4]
```

## `ravel()`

```python
arr.ravel()
```

Both are commonly used for flattening.

### Basic Interview Difference

- `flatten()` generally returns a **copy**
- `ravel()` often returns a **view** when possible

For placements, knowing this basic difference is enough.

---

# 18. Transpose

Transpose converts:

```text
Rows → Columns
Columns → Rows
```

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

```python
arr.T
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

---

# 19. Joining Arrays

## Concatenate

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate((a, b))
```

Output:

```text
[1 2 3 4 5 6]
```

---

## Vertical Stack

```python
np.vstack((a, b))
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

## Horizontal Stack

```python
np.hstack((a, b))
```

Output:

```text
[1 2 3 4 5 6]
```

---

# 20. Splitting Arrays

```python
arr = np.array([1, 2, 3, 4, 5, 6])
```

```python
np.split(arr, 3)
```

Output:

```text
[array([1, 2]), array([3, 4]), array([5, 6])]
```

For interview preparation, know the concept of:

- `split()`
- `hsplit()`
- `vsplit()`

---

# 21. Sorting

```python
arr = np.array([30, 10, 50, 20])
```

```python
np.sort(arr)
```

Output:

```text
[10 20 30 50]
```

Descending:

```python
np.sort(arr)[::-1]
```

---

# 22. `argmin()` and `argmax()`

These return the **index**, not the value.

```python
arr = np.array([10, 50, 20, 30])
```

Maximum value index:

```python
np.argmax(arr)
```

Output:

```text
1
```

Minimum value index:

```python
np.argmin(arr)
```

Output:

```text
0
```

---

# 23. Unique Values

```python
arr = np.array([1, 2, 2, 3, 3, 3])
```

```python
np.unique(arr)
```

Output:

```text
[1 2 3]
```

Useful for basic data cleaning and analysis.

---

# 24. Random Numbers

NumPy provides random number generation.

## Random Float

```python
np.random.rand(3)
```

## Random Integer

```python
np.random.randint(1, 10, 5)
```

Meaning:

```text
Generate 5 random integers from 1 to 9
```

## Random Matrix

```python
np.random.rand(3, 3)
```

---

# 25. Random Seed

Used for reproducibility.

```python
np.random.seed(42)
```

Then random results can be reproduced consistently.

This is useful in:

- Machine Learning
- Experiments
- Testing

---

# 26. Broadcasting (IMPORTANT CONCEPT)

Broadcasting allows NumPy to perform operations on arrays with different shapes when their dimensions are compatible.

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr + 10
```

Output:

```text
[[11 12 13]
 [14 15 16]]
```

NumPy applies `10` to every element.

Another example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

arr + b
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

### Simple Understanding

Broadcasting means NumPy automatically expands compatible dimensions for calculations.

For placements, understand:

- Scalar with array
- 1D array with compatible 2D array

You do not need to memorize complex broadcasting rules initially.

---

# 27. Copy vs View (IMPORTANT INTERVIEW CONCEPT)

## Copy

A copy creates independent data.

```python
a = np.array([1, 2, 3])

b = a.copy()

b[0] = 100
```

`a` remains unchanged.

---

## View

A view may share the same underlying data.

```python
a = np.array([1, 2, 3])

b = a.view()

b[0] = 100
```

Changes may affect `a`.

### Interview Answer

> A copy creates independent data, while a view generally shares the original array's underlying data.

---

# 28. Data Types and Type Conversion

Create an array with a specific type:

```python
arr = np.array([1, 2, 3], dtype=float)
```

Convert type:

```python
arr.astype(float)
```

Example:

```python
arr = np.array([1.2, 2.8, 3.5])

arr.astype(int)
```

---

# 29. Handling Missing Values (`NaN`)

In numerical datasets, missing values are often represented as:

```python
np.nan
```

Example:

```python
arr = np.array([1, 2, np.nan, 4])
```

Check missing values:

```python
np.isnan(arr)
```

Calculate while ignoring `NaN`:

```python
np.nanmean(arr)
```

Other useful functions:

```python
np.nansum(arr)
np.nanmin(arr)
np.nanmax(arr)
```

For basic placement preparation, this level is enough.

---

# 30. Matrix Multiplication

Consider:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
```

## Element-wise Multiplication

```python
A * B
```

## Matrix Multiplication

```python
A @ B
```

or:

```python
np.dot(A, B)
```

### Important Difference

```text
*     → Element-wise multiplication
@     → Matrix multiplication
```

This is a common interview question.

---

# 31. Practical Mini Example: Student Data

```python
marks = np.array([75, 82, 91, 60, 88, 95])
```

## Average

```python
np.mean(marks)
```

## Highest Marks

```python
np.max(marks)
```

## Lowest Marks

```python
np.min(marks)
```

## Students Who Scored Above 80

```python
marks[marks > 80]
```

## Add Grace Marks

```python
marks + 5
```

This demonstrates how NumPy is used for numerical data processing.

---

# 32. Practical Mini Example: Sales Data

```python
sales = np.array([
    [100, 120, 130],
    [200, 220, 250],
    [150, 170, 180]
])
```

Assume:

```text
Rows    → Products
Columns → Months
```

## Total Sales per Product

```python
np.sum(sales, axis=1)
```

## Total Sales per Month

```python
np.sum(sales, axis=0)
```

## Overall Average

```python
np.mean(sales)
```

This type of example is useful for **Data Analyst interviews**.

---

# 33. Most Important NumPy Functions to Remember

```python
np.array()
np.zeros()
np.ones()
np.eye()
np.full()

np.arange()
np.linspace()

np.sum()
np.mean()
np.min()
np.max()
np.std()
np.var()

np.reshape()
np.concatenate()
np.vstack()
np.hstack()

np.sort()
np.unique()

np.argmax()
np.argmin()

np.random.rand()
np.random.randint()

np.isnan()
np.nanmean()
```

---

# 34. NumPy Concepts You MUST Know for Placements

## HIGH PRIORITY

### 1. NumPy Arrays

Know:

- What NumPy is
- Why NumPy is faster than lists
- `ndarray`

### 2. Array Properties

Know:

```python
ndim
shape
size
dtype
```

### 3. Indexing and Slicing

Especially:

- 1D arrays
- 2D arrays

### 4. Vectorization

Perform operations without loops.

### 5. Boolean Indexing

Example:

```python
arr[arr > 50]
```

### 6. Aggregation Functions

Know:

```python
sum
mean
min
max
std
```

### 7. Axis

Understand:

```text
axis=0 → column-wise
axis=1 → row-wise
```

### 8. Reshape

Know:

```python
reshape()
flatten()
```

### 9. Broadcasting

Understand the basic concept.

### 10. Copy vs View

Know the interview-level difference.

### 11. Matrix Multiplication

Know:

```text
*  vs  @
```

---

# 35. Common Placement Interview Questions

## Q1. What is NumPy?

**Answer:**

> NumPy is a Python library used for numerical computing. It provides efficient multi-dimensional arrays and supports fast mathematical and vectorized operations.

---

## Q2. Why is NumPy faster than Python lists?

**Answer:**

> NumPy arrays store data efficiently and perform vectorized operations using optimized low-level implementations, which reduces the overhead of Python loops.

---

## Q3. What is the difference between a Python list and a NumPy array?

| Python List | NumPy Array |
|---|---|
| General-purpose | Numerical computing |
| Slower for large calculations | Faster numerical operations |
| Python loops often needed | Vectorization supported |
| More flexible data types | Usually homogeneous data type |

---

## Q4. What is vectorization?

**Answer:**

> Vectorization means performing operations on an entire array at once instead of using explicit Python loops.

Example:

```python
arr * 2
```

---

## Q5. What is broadcasting?

**Answer:**

> Broadcasting allows NumPy to perform operations on arrays with compatible shapes by automatically expanding dimensions where possible.

---

## Q6. What is the difference between `shape` and `size`?

**Answer:**

> `shape` tells us the dimensions of an array, while `size` tells us the total number of elements.

---

## Q7. Explain `axis=0` and `axis=1`.

**Answer:**

> In a 2D array, `axis=0` performs operations column-wise, while `axis=1` performs operations row-wise.

---

## Q8. Difference between `flatten()` and `ravel()`?

**Answer:**

> `flatten()` generally returns a copy, while `ravel()` often returns a view when possible.

---

## Q9. Difference between `*` and `@`?

**Answer:**

> `*` performs element-wise multiplication, while `@` performs matrix multiplication.

---

## Q10. What is the difference between copy and view?

**Answer:**

> A copy creates independent data, while a view generally shares the underlying data with the original array.

---

# 36. Placement-Oriented Practice Questions

Try solving these yourself.

### Basic

1. Create a NumPy array containing numbers from 1 to 20.
2. Find its shape, size, dimension, and data type.
3. Find all numbers greater than 10.
4. Find the mean, maximum, and minimum.
5. Convert the array into a 4 × 5 matrix.

### Intermediate

6. Create two arrays and perform addition, subtraction, multiplication, and division.
7. Find all even numbers from an array.
8. Replace values greater than 50 with 0.
9. Find the index of the maximum value.
10. Sort an array in descending order.

### Data-Oriented

11. Given a sales matrix, calculate total sales by product.
12. Calculate total sales by month.
13. Find products with average sales above a threshold.
14. Handle `NaN` values.
15. Normalize a simple numerical array.

---

# 37. Final Placement Preparation Roadmap

Follow this order:

```text
1. What is NumPy?
        ↓
2. Creating Arrays
        ↓
3. ndim, shape, size, dtype
        ↓
4. Indexing and Slicing
        ↓
5. Vectorized Operations
        ↓
6. Boolean Indexing
        ↓
7. Aggregations
        ↓
8. axis=0 and axis=1
        ↓
9. Reshape and Flatten
        ↓
10. Joining and Splitting
        ↓
11. Sorting and Unique Values
        ↓
12. Broadcasting
        ↓
13. Copy vs View
        ↓
14. Random Numbers
        ↓
15. Matrix Multiplication
        ↓
16. Practical Data Exercises
```

---

# 38. Final Revision Cheat Sheet

```python
import numpy as np

# Create
np.array([1, 2, 3])
np.zeros((2, 3))
np.ones((2, 3))
np.arange(0, 10, 2)
np.linspace(0, 10, 5)

# Properties
arr.ndim
arr.shape
arr.size
arr.dtype

# Indexing
arr[0]
arr[-1]
arr[1:4]

# Operations
arr + 10
arr * 2
arr ** 2

# Filtering
arr[arr > 10]

# Aggregation
np.sum(arr)
np.mean(arr)
np.min(arr)
np.max(arr)
np.std(arr)

# Reshape
arr.reshape(2, 3)
arr.flatten()

# Sorting
np.sort(arr)

# Unique
np.unique(arr)

# Index of min/max
np.argmax(arr)
np.argmin(arr)

# Matrix multiplication
A @ B

# Missing values
np.isnan(arr)
np.nanmean(arr)
```

---

# Final Advice for Placements

You do **not** need to memorize the entire NumPy library.

For placements, make sure you can confidently explain and practically use:

- NumPy arrays
- Array attributes
- Indexing and slicing
- Vectorization
- Boolean filtering
- Aggregation functions
- `axis`
- Reshaping
- Broadcasting
- Copy vs view
- Basic random functions
- Matrix multiplication

If you can understand these concepts and solve small practical problems using them, your NumPy preparation is **strong enough for most placement interviews and data-related roles**.
