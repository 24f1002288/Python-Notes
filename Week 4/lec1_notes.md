# Introduction to Python Programming Practice

This week is dedicated to diving into practical programming, focusing on gaining comfort and familiarity with writing Python code. The primary goal is hands-on experience and getting used to the coding environment, rather than introducing entirely new Python features. The aim is to help everyone, regardless of their current coding proficiency, build a solid foundation and feel more at ease with writing programs.

## Introduction: The Path to Coding Comfort

The focus for this period is to transition into a more practical coding mindset. The emphasis is on actively writing programs to familiarize yourself with the general programming environment and develop the habit of constructing longer pieces of code. This practical approach is designed to ensure everyone builds confidence in their coding abilities.

## Core Programming Challenges for the Week

This week, we will explore a set of foundational programming problems. These problems are chosen because they will be revisited in future sessions. As new Python concepts are introduced, we will learn how to enhance and optimize the initial solutions we create this week.

### 1. The Birthday Paradox

The Birthday Paradox is a fascinating concept from probability theory. It asks: in a group of randomly chosen people, what is the probability that at least two people will share the same birthday? Surprisingly, the probability becomes quite high even with a relatively small number of people (e.g., a 50% chance with just 23 people).

*   **Understanding the Paradox**: It highlights how our intuition about probability can sometimes be misleading. We'll be looking at how to simulate this kind of problem using code.
*   **Relevance**: This problem is excellent for understanding how to use randomness in programming and how to simulate real-world scenarios to estimate probabilities.

**Code Example: Simulating Random Birthdays (Conceptual)**

To begin understanding the Birthday Paradox in code, we first need to be able to generate random birthdays. A simple approach is to assign a random number between 1 and 365 (ignoring leap years for simplicity) for each person's birthday.

```python
import random

def generate_random_birthday():
    """Generates a random day of the year (1-365) to represent a birthday."""
    return random.randint(1, 365)

# How it works:
# 1. 'import random' makes Python's random number tools available.
# 2. 'random.randint(1, 365)' picks a whole number randomly between 1 and 365,
#    including both 1 and 365. Each number represents a unique day of the year.

# Example of generating a single birthday:
first_person_birthday = generate_random_birthday()
print(f"First person's birthday: Day {first_person_birthday}")

# To check for shared birthdays, we'd generate multiple birthdays and store them,
# then compare them. This will be the basis for solving the full paradox.
```

### 2. Simple List Searching

Searching is a fundamental operation in computer science. It involves finding a specific item within a collection of items (like a list). For this week, we'll start with the most basic and straightforward way to search.

*   **Understanding the Method**: This initial approach will be a "linear search" – checking each item one by one from the beginning of the list until the desired item is found or the end of the list is reached.
*   **Pain Point**: While simple, this method can be slow for very large lists. We'll see why in later discussions.

**Code Example: Linear Search**

```python
def find_item_linear(data_list, target_item):
    """
    Searches for a target_item in a data_list using a simple linear scan.
    Returns True if the item is found, False otherwise.
    """
    for item in data_list:  # Go through each 'item' in the 'data_list'
        if item == target_item: # If the current item is what we're looking for
            return True         # We found it, so stop and say True
    return False            # If the loop finishes, the item wasn't found

# How it works:
# 1. The 'for' loop iterates through each element in 'data_list' one by one.
# 2. Inside the loop, an 'if' statement compares the current 'item' with the 'target_item'.
# 3. If a match is found, 'True' is returned immediately, and the function stops.
# 4. If the loop completes without finding a match, it means the item isn't in the list,
#    so 'False' is returned.

# Example usage:
my_numbers = [5, 12, 3, 9, 18, 1]
print(f"Is 9 in the list? {find_item_linear(my_numbers, 9)}")  # Expected: True
print(f"Is 7 in the list? {find_item_linear(my_numbers, 7)}")  # Expected: False
```

### 3. Basic List Sorting

Sorting involves arranging items in a list into a specific order, such as ascending (smallest to largest) or descending (largest to smallest). We will begin with a "very obvious" way to sort, which is easy to understand, though not the most efficient.

*   **Understanding the Method**: We will explore an intuitive sorting algorithm like selection sort or bubble sort. These methods involve repeatedly comparing and swapping elements until the list is in the desired order.
*   **Pain Point**: Similar to linear search, these simple sorting methods can become very slow as the list size grows.

**Code Example: Selection Sort**

Selection sort works by repeatedly finding the minimum element from the unsorted part of the list and putting it at the beginning.

```python
def selection_sort(data_list):
    """
    Sorts a list of numbers using the selection sort algorithm.
    Modifies the list in-place.
    """
    n = len(data_list) # Get the total number of items in the list

    # Loop through the list from the first item to the second-to-last item
    # (The last item will naturally be in place after the others are sorted)
    for i in range(n):
        # Assume the current item 'i' is the smallest initially
        min_index = i

        # Look at the rest of the unsorted part of the list
        for j in range(i + 1, n):
            # If we find an item that is smaller than our current 'min_index' item
            if data_list[j] < data_list[min_index]:
                min_index = j # Update 'min_index' to point to this new smallest item

        # After checking all items, if 'min_index' is different from 'i',
        # it means we found a smaller item. Swap it with the current item 'i'.
        if min_index != i:
            data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    return data_list # Return the sorted list

# How it works:
# 1. The outer loop ('for i in range(n)') moves a "boundary" through the list,
#    separating the sorted part (left) from the unsorted part (right).
# 2. For each pass of the outer loop, the inner loop ('for j in range(i + 1, n)')
#    finds the smallest element in the unsorted portion.
# 3. 'min_index' keeps track of where this smallest element is located.
# 4. Once the smallest element is found, it's swapped with the element at the
#    current position 'i', effectively moving it to the sorted part.

# Example usage:
my_unsorted_list = [64, 25, 12, 22, 11]
print(f"Original list: {my_unsorted_list}")
sorted_list = selection_sort(my_unsorted_list.copy()) # Use .copy() to not modify original if needed
print(f"Sorted list: {sorted_list}") # Expected: [11, 12, 22, 25, 64]
```

### 4. Introduction to Matrix Operations

Matrices are rectangular arrays of numbers and are fundamental in many areas of science, engineering, and computer graphics. This week, we'll learn how to represent matrices in Python and perform basic operations like addition and multiplication.

*   **Python Representation**: Matrices are typically represented as "lists of lists" in Python. For example, a 2x3 matrix can be `[[1, 2, 3], [4, 5, 6]]`.
*   **Topics Covered**: We will specifically look at how to find the sum and product of two matrices.
*   **Pain Point**: Matrix operations require careful handling of dimensions (number of rows and columns). Incorrect dimensions will lead to errors.

**Code Example 1: Matrix Addition**

Matrix addition is straightforward: you add corresponding elements. This means both matrices must have the exact same number of rows and columns.

```python
def add_matrices(matrix1, matrix2):
    """
    Adds two matrices. Both matrices must have the same dimensions.
    Returns a new matrix representing their sum.
    """
    # First, check if the matrices can be added (same dimensions)
    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) # Assuming non-empty matrix
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if rows1 != rows2 or cols1 != cols2:
        print("Error: Matrices must have the same dimensions for addition.")
        return None # Indicate an error

    # Create a new matrix to store the result, filled with zeros initially
    result_matrix = [[0 for _ in range(cols1)] for _ in range(rows1)]

    # Loop through each row and each column to add corresponding elements
    for i in range(rows1):
        for j in range(cols1):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

# How it works:
# 1. It first checks if the matrices have compatible sizes (same number of rows and columns).
# 2. It creates an empty 'result_matrix' of the same size, initialized with zeros.
# 3. Using nested 'for' loops, it iterates through each cell (i, j) of the matrices.
# 4. It adds the element at (i, j) from 'matrix1' to the element at (i, j) from 'matrix2'
#    and stores the sum in the corresponding cell of 'result_matrix'.

# Example usage:
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10, 11, 12]]

C = [[1, 2],
     [3, 4]]

sum_AB = add_matrices(A, B)
if sum_AB:
    print("Matrix A + B:")
    for row in sum_AB:
        print(row)
# Expected output:
# [8, 10, 12]
# [14, 16, 18]

sum_AC = add_matrices(A, C) # This will print an error message
```

**Code Example 2: Matrix Multiplication**

Matrix multiplication is more complex than addition. If you multiply matrix A (m x n) by matrix B (n x p), the result is a matrix C (m x p). A crucial rule is that the number of columns in the first matrix must equal the number of rows in the second matrix.

```python
def multiply_matrices(matrix1, matrix2):
    """
    Multiplies two matrices.
    The number of columns in matrix1 must equal the number of rows in matrix2.
    Returns a new matrix representing their product.
    """
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Check for compatible dimensions for multiplication
    if cols1 != rows2:
        print("Error: For multiplication, columns of first matrix must equal rows of second matrix.")
        return None

    # Create a result matrix with dimensions rows1 x cols2, initialized with zeros
    result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):  # Iterate through rows of matrix1
        for j in range(cols2):  # Iterate through columns of matrix2
            for k in range(cols1):  # Iterate through columns of matrix1 / rows of matrix2
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

# How it works:
# 1. It first checks if the matrices have compatible dimensions: the number of
#    columns in the first matrix must match the number of rows in the second.
# 2. It creates a 'result_matrix' with dimensions (rows of matrix1) x (columns of matrix2),
#    initialized with zeros.
# 3. It uses three nested 'for' loops:
#    - The outer two loops (`i` and `j`) determine the position in the 'result_matrix'.
#    - The innermost loop (`k`) performs the dot product of the i-th row of 'matrix1'
#      and the j-th column of 'matrix2', summing up the products.

# Example usage:
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

C = [[1, 2, 3],
     [4, 5, 6]]

product_AB = multiply_matrices(A, B)
if product_AB:
    print("Matrix A * B:")
    for row in product_AB:
        print(row)
# Expected output:
# [19, 22]  (1*5 + 2*7 = 19, 1*6 + 2*8 = 22)
# [43, 50]  (3*5 + 4*7 = 43, 3*6 + 4*8 = 50)

product_AC = multiply_matrices(A, C) # This will print an error message (A is 2x2, C is 2x3. cols A = rows C, so this should work!)
# Oh, my manual error check for the example was wrong. A is 2x2, C is 2x3. cols A (2) == rows C (2). So, A*C is valid.
# Let's re-evaluate A*C: (2x2) * (2x3) -> (2x3)
# A = [[1, 2], [3, 4]]
# C = [[1, 2, 3], [4, 5, 6]]
# (1*1 + 2*4) = 9, (1*2 + 2*5) = 12, (1*3 + 2*6) = 15
# (3*1 + 4*4) = 19, (3*2 + 4*5) = 26, (3*3 + 4*6) = 33
# Expected output: [[9, 12, 15], [19, 26, 33]]

product_AC = multiply_matrices(A, C)
if product_AC:
    print("\nMatrix A * C:")
    for row in product_AC:
        print(row)
```

## Summary and Important Tips

This week is a dedicated workshop for honing your practical coding skills. It's perfectly normal if you feel you are ahead or behind others; the goal is to bring everyone to a comfortable and consistent level of understanding and practice.

**Key Takeaways:**

*   **Hands-on Practice**: The entire week is devoted to writing code for common computational problems.
*   **Foundational Problems**: The problems introduced (Birthday Paradox, searching, sorting, matrix operations) are fundamental and will serve as building blocks for more advanced topics.
*   **Iterative Learning**: The code you write this week for these problems will be revisited and improved upon as you learn more powerful Python features in the future.

**The Most Important Tip for Learning to Code:**

The best way to become proficient in coding is through **repeated practice**. Do not be afraid to write the same program multiple times.

*   **Observe**: Watch how a piece of code is constructed and explained.
*   **Delete**: Once you've understood it, delete the code you just saw.
*   **Redo Independently**: Try to write the code yourself from scratch, without looking at the example.
*   **Repeat**: Do this process multiple times until you feel entirely comfortable and confident in your ability to write that particular piece of code on your own.

This active, iterative approach to practice is crucial for solidifying your understanding and building muscle memory for coding. Good luck!