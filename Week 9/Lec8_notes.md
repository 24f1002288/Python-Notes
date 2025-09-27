# Pandas Data Structures and Advanced Operations

This document provides a comprehensive overview of fundamental Pandas data structures and advanced techniques for data manipulation and analysis, building upon basic data loading and inspection methods.

## Key Topics

### I. Understanding Pandas Data Structures

Pandas introduces specialized data structures to efficiently handle tabular and one-dimensional data.

#### 1. DataFrame

A DataFrame is a core Pandas data structure designed to store data in a two-dimensional, tabular format, similar to a spreadsheet or a SQL table.

*   **Definition:** A two-dimensional (2D) data structure used to store tabular data, featuring rows and columns.
*   **Purpose:** Ideal for representing entire datasets loaded from files like CSVs.
*   **Checking the type:** You can verify that a loaded dataset (e.g., `scores`) is indeed a DataFrame.

**Code Example:**
```python
import pandas as pd

# Assuming 'scores.csv' exists with tabular data
# Load a CSV file into a DataFrame
scores = pd.read_csv('scores.csv')

# Print the type of the 'scores' variable
print(type(scores))
```
**How it works:** This code first loads a CSV file into a variable named `scores`. Then, `type(scores)` checks and confirms that `scores` is a `pandas.core.frame.DataFrame` object, indicating it's a two-dimensional table.

#### 2. Series

A Series is a one-dimensional data structure in Pandas, representing a single column from a DataFrame.

*   **Definition:** A one-dimensional (1D) array-like object capable of holding any data type (integers, strings, floats, Python objects, etc.).
*   **Purpose:** When you extract a single column from a DataFrame, it becomes a Series.
*   **Analogy:** Think of it as a single column of data from your spreadsheet.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Access a specific column, e.g., 'Name'
name_column = scores['Name']

# Print the type of the 'name_column' variable
print(type(name_column))
```
**How it works:** Here, `scores['Name']` selects the 'Name' column from the `scores` DataFrame. `type(name_column)` then shows that this extracted column is a `pandas.core.series.Series` object, confirming its one-dimensional nature.

### II. Efficient Data Access and Inspection

When dealing with large datasets, it's often impractical or impossible to view the entire DataFrame. Pandas provides methods to inspect parts of your data.

#### 1. Viewing Sample Rows

*   **`head()`:** Displays the first 5 rows of the DataFrame by default. Useful for a quick glance at the beginning of your data.
*   **`tail()`:** Displays the last 5 rows of the DataFrame by default. Useful for checking the end of your data, especially if it's sorted or has specific ending patterns.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Display the first 5 rows
print("Top 5 rows:")
print(scores.head())

# Display the last 5 rows
print("\nBottom 5 rows:")
print(scores.tail())
```
**How it works:** `scores.head()` returns a new DataFrame containing only the first 5 rows, including their original index. `scores.tail()` does the same for the last 5 rows. You can pass an integer argument, e.g., `scores.head(10)`, to view a different number of rows.

#### 2. Accessing Data by Row (Filtering)

Pandas allows powerful filtering of data based on specific conditions, retrieving entire rows that match criteria.

*   **Row-wise Filtering:** Unlike simply selecting columns, you can select rows based on the values within one or more columns.

**Pain Point:** Initially, you might think Pandas only supports column-wise access. However, it's very capable of row-wise selection based on conditions.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Find all details for a student named 'Nisha'
nisha_details = scores[scores['Name'] == 'Nisha']
print(nisha_details)
```
**How it works:**
1.  `scores['Name'] == 'Nisha'` creates a `Series` of `True`/`False` values. For each row, it's `True` if the 'Name' column is 'Nisha', and `False` otherwise.
2.  `scores[...]` uses this `True`/`False` Series to select only those rows where the condition was `True`. This effectively filters the DataFrame to show all columns for the student 'Nisha'.

### III. Advanced Filtering and Aggregation

Moving beyond simple data access, Pandas excels at performing complex filtering, aggregation, and categorization tasks with concise code.

#### 1. Filtering for Specific Groups and Aggregating

You can combine filtering with aggregation functions (like `max`, `min`, `mean`) to derive insights from specific subsets of your data.

**Problem:** Find the maximum score among boys and girls separately.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Step 1: Filter for male students
male_students = scores[scores['Gender'] == 'M']

# Step 2: From male students, select the 'Total' score column (which is a Series)
male_total_scores = male_students['Total']

# Step 3: Find the maximum total score among male students
topper_boy_score = male_total_scores.max()
print(f"Topper boy's score: {topper_boy_score}")

# Combine into a single line for female students
topper_girl_score = scores[scores['Gender'] == 'F']['Total'].max()
print(f"Topper girl's score: {topper_girl_score}")
```
**How it works:** This demonstrates a multi-step process that can be chained together.
1.  First, a boolean condition `scores['Gender'] == 'M'` selects all rows where the gender is 'M'.
2.  Then, `['Total']` selects only the 'Total' column from this filtered DataFrame. This results in a Pandas Series.
3.  Finally, `.max()` is called on this Series to find the highest value within it.

#### 2. Categorizing Data using Conditions

You can easily categorize data based on value ranges within a column.

*   **`between()` method:** A convenient way to check if values fall within a specified range (inclusive by default).

**Problem:** Categorize students based on their Physics marks into four grades (A: >85, B: 70-85, C: 60-70, D: <60) and count students in each.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Category A: Physics marks > 85
grade_a_students = scores[scores['Physics'] > 85]
print(f"Grade A students (Physics > 85):\n{grade_a_students}")
print(f"Number of Grade A students: {grade_a_students.shape[0]}\n")

# Category B: Physics marks between 70 and 85 (inclusive)
# Using .between() for clear range checking
grade_b_students = scores[scores['Physics'].between(70, 85)]
print(f"Grade B students (Physics 70-85):\n{grade_b_students}")
print(f"Number of Grade B students: {grade_b_students.shape[0]}\n")

# Category C: Physics marks between 60 and 70
grade_c_students = scores[scores['Physics'].between(60, 70)]
print(f"Grade C students (Physics 60-70):\n{grade_c_students}")
print(f"Number of Grade C students: {grade_c_students.shape[0]}\n")

# Category D: Physics marks < 60
grade_d_students = scores[scores['Physics'] < 60]
print(f"Grade D students (Physics < 60):\n{grade_d_students}")
print(f"Number of Grade D students: {grade_d_students.shape[0]}\n")
```
**How it works:**
1.  For Grade A, `scores['Physics'] > 85` generates a boolean Series, which filters the DataFrame.
2.  For Grade B, `scores['Physics'].between(70, 85)` provides a clean way to define the range.
3.  `.shape` returns a tuple `(number_of_rows, number_of_columns)`. `.shape[0]` specifically extracts the number of rows, giving us the count of students in each category.

#### 3. Combining Multiple Conditions (across different columns)

You can filter data based on multiple conditions simultaneously, even if these conditions apply to different columns.

**Pain Point:** Unlike standard Python's `and` operator, Pandas requires the bitwise `&` (ampersand) for combining boolean Series. Using `and` will lead to an error. Each condition *must* also be enclosed in parentheses.

**Problem:** Find how many female students scored above 85 in Physics, and how many male students did.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Number of female students with Physics marks > 85
female_above_85_physics = scores[(scores['Gender'] == 'F') & (scores['Physics'] > 85)]
print(f"Female students with Physics > 85: {female_above_85_physics.shape[0]}")

# Number of male students with Physics marks > 85
male_above_85_physics = scores[(scores['Gender'] == 'M') & (scores['Physics'] > 85)]
print(f"Male students with Physics > 85: {male_above_85_physics.shape[0]}")
```
**How it works:**
1.  `(scores['Gender'] == 'F')` creates a boolean Series for female students.
2.  `(scores['Physics'] > 85)` creates a boolean Series for high physics scores.
3.  The `&` operator combines these two boolean Series element-wise. A row is `True` only if *both* corresponding values in the two Series are `True`.
4.  The combined boolean Series is then used to filter the `scores` DataFrame.

#### 4. Automating with Loops for Dynamic Analysis

When you need to perform similar operations across multiple columns or categories, loops provide an elegant and efficient solution, preventing repetitive code.

**Problem:** Find the gender-wise split (number of female and male students) for students scoring above 85 in Mathematics, Physics, and Chemistry. Then, extend this to finding students scoring above the *average* for each subject.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

subjects = ['Mathematics', 'Physics', 'Chemistry']
genders = ['F', 'M']

print("--- Students scoring above 85 (Gender-wise) ---")
for subject in subjects:
    for gender in genders:
        filtered_students = scores[(scores['Gender'] == gender) & (scores[subject] > 85)]
        count = filtered_students.shape[0]
        print(f"Above 85 in {subject} ({gender}): {count} students")
print("\n")

print("--- Students scoring above AVERAGE (Gender-wise) ---")
for subject in subjects:
    # Calculate average for the current subject
    avg_score = scores[subject].mean()
    print(f"Average for {subject}: {avg_score:.2f}") # .2f for 2 decimal places

    for gender in genders:
        # Filter for students in the current gender and above the subject's average
        filtered_students = scores[(scores['Gender'] == gender) & (scores[subject] > avg_score)]
        count = filtered_students.shape[0]
        print(f"Above Average in {subject} ({gender}): {count} students")
    print("-" * 30) # Separator for readability
```
**How it works:**
1.  **Lists for Iteration:** Lists like `subjects` and `genders` are created to hold the values we want to loop through.
2.  **Nested Loops:** The outer loop iterates through each `subject`, and the inner loop iterates through each `gender`.
3.  **Dynamic Filtering:** Inside the loops, `subject` and `gender` variables are used in the filtering conditions. This means the same line of code is applied dynamically to different subjects and genders.
4.  **Dynamic Average:** For the "above average" scenario, `scores[subject].mean()` calculates the average *for the current subject* within each iteration, making the analysis highly flexible.

### IV. Grouping Data with `groupby()`

The `groupby()` function is a powerful feature for dividing your data into logical "bins" based on the unique values in one or more columns. It's especially useful for performing aggregations on these groups.

*   **Concept:** Similar to the "binning" concept in computational thinking, `groupby()` partitions your DataFrame into sub-groups.
*   **Purpose:** Ideal for understanding the distribution or properties of data within distinct categories (e.g., all male students, all female students).
*   **`groupby('ColumnName').groups`:** This specific usage returns a dictionary.
    *   **Keys:** The unique values found in the specified `ColumnName` (e.g., 'F' and 'M' for 'Gender').
    *   **Values:** A list of the *index labels* (or card numbers, if the index is set to card numbers) of the rows belonging to that group.

**Problem:** Divide all students into groups based on their gender and list their associated card numbers/indices. Then, extend this to students scoring above average in a subject, grouped by gender.

**Code Example:**
```python
import pandas as pd

scores = pd.read_csv('scores.csv') # Assuming 'scores' DataFrame is loaded

# Group the entire DataFrame by 'Gender' and view the groups
print("--- All students grouped by Gender ---")
gender_groups = scores.groupby('Gender').groups
print(gender_groups)
print("\n")

# Interpretation of output:
# {'F': Index([ 0,  1,  3,  4,  5,  6,  8, 10, 11, 13, 16, 17, 18, 19], dtype='int64'),
#  'M': Index([ 2,  7,  9, 12, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], dtype='int64')}
# 'F' and 'M' are keys, and the lists are the original row indices of female and male students, respectively.

# Apply groupby after a filter
subjects = ['Mathematics', 'Physics', 'Chemistry']

print("--- Students above average, grouped by Gender ---")
for subject in subjects:
    avg_score = scores[subject].mean()
    # Filter for students above average in the current subject
    above_average_students = scores[scores[subject] > avg_score]

    # Now, group *these filtered students* by gender and see their indices
    gender_split_above_average = above_average_students.groupby('Gender').groups

    print(f"For {subject} (above average {avg_score:.2f}):")
    print(gender_split_above_average)
    print("-" * 30)
```
**How it works:**
1.  `scores.groupby('Gender').groups` directly creates a dictionary mapping each unique gender ('F', 'M') to the list of index values for students of that gender. This shows you *which* specific students belong to each group.
2.  When chained with filtering, `scores[scores[subject] > avg_score].groupby('Gender').groups` first filters the `scores` DataFrame to include only students above average for the current `subject`. Then, `groupby('Gender').groups` is applied to *this filtered subset*, providing a gender-wise breakdown of *those particular* students by their indices. This is more informative than just counts, as it points to specific students.

## Summary and Important Tips

Pandas is an incredibly powerful library that simplifies complex data operations that would otherwise require many lines of traditional Python code.

*   **Data Structures:** Remember that `DataFrames` are 2D tables, and `Series` are 1D columns derived from DataFrames.
*   **Efficient Access:** Use `head()` and `tail()` for quick data previews.
*   **Filtering Power:** Pandas allows flexible filtering of rows based on single or multiple conditions, even across different columns.
*   **Combine Conditions Safely:** When combining multiple conditions, always use the `&` (bitwise AND) operator and enclose each condition in parentheses. Avoid the regular `and` keyword.
*   **Dynamic Analysis:** Leverage loops and dynamic calculation (like `.mean()`) within your filtering logic to automate repetitive tasks and adapt to changing data.
*   **`groupby()` for Categorization:** The `groupby()` method is excellent for splitting data into logical groups and examining their contents or performing group-specific aggregations. `groupby().groups` is particularly useful for seeing the indices of items in each group.

The features covered in these notes represent a strong foundation for working with Pandas. While the library offers vast capabilities, these introductory concepts are more than sufficient for many analytical tasks and for further learning in related courses. Focus on mastering these fundamentals rather than getting overwhelmed by the entirety of Pandas' extensive documentation.