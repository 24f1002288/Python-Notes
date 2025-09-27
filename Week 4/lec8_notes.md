# Programming Matrix Multiplication

This guide explores how to implement matrix multiplication using a computer program. While the mathematical process of multiplying matrices is often learned in high school, converting this concept into a functional program requires a precise understanding of how each element is calculated and tracked.

## Key Concepts

### Understanding Matrix Representation

In programming, matrices are typically represented as "lists of lists" (or arrays of arrays in other languages). For example, a 2x2 matrix:
```
[[1, 2],
 [3, 4]]
```
Here, `[1, 2]` is the first row (at index 0), and `[3, 4]` is the second row (at index 1).

### The Foundation: Calculating a Single Element in the Result Matrix

Let's say we have two matrices, `A` and `B`, and their product is matrix `C`.
If `A` is an `m x n` matrix and `B` is an `n x p` matrix, then `C` will be an `m x p` matrix. This means the number of columns in `A` must equal the number of rows in `B`.

The core idea is that *each individual element* in the result matrix `C` is found by performing a specific calculation involving one row from `A` and one column from `B`.

#### 0-Based Indexing: A Crucial Detail

Unlike traditional mathematical notation where rows and columns usually start from 1, programming languages like Python use **0-based indexing**. This means:
*   The first row is at index `0`.
*   The second row is at index `1`.
*   ...and so on.
The same applies to columns.

For example, if we refer to `A[i][k]`, it means the element in the `(i+1)`-th row and `(k+1)`-th column of matrix `A`.

#### How to Calculate `C[i][j]`

To find the element at row `i` and column `j` in the result matrix `C` (written as `C[i][j]`):

1.  Take the entire `i`-th row from matrix `A`.
2.  Take the entire `j`-th column from matrix `B`.
3.  Perform a "dot product" operation:
    *   Multiply the first element of `A`'s `i`-th row by the first element of `B`'s `j`-th column.
    *   Multiply the second element of `A`'s `i`-th row by the second element of `B`'s `j`-th column.
    *   Continue this process for all corresponding elements.
    *   Sum up all these products.

Let's illustrate with an example for `C[3][2]` (which means the element in the 4th row, 3rd column, using 0-based indexing):

To calculate `C[3][2]`:
*   We use the `3`-rd row of matrix `A`.
*   We use the `2`-nd column of matrix `B`.

The calculation for `C[3][2]` would look like this:
`C[3][2] = (A[3][0] * B[0][2]) + (A[3][1] * B[1][2]) + (A[3][2] * B[2][2]) + ...` (This continues for as many elements are in the row/column).

Notice the patterns:
*   The first index of `A` (`3`) always matches the row index of `C` (`i`).
*   The second index of `B` (`2`) always matches the column index of `C` (`j`).
*   A new index `k` (0, 1, 2, ...) changes for both `A`'s column and `B`'s row in each multiplication step. This `k` cycles through the elements needed for the dot product.

### The General Formula for `C[i][j]`

Putting this pattern into a general formula:

`C[i][j] = Sum ( A[i][k] * B[k][j] )`

Where `k` goes from `0` up to `(number of columns in A) - 1` (or `(number of rows in B) - 1`, since these must be equal).

This formula means that for each position `(i, j)` in the result matrix `C`, you need to:
1.  Initialize a sum for `C[i][j]` to zero.
2.  Loop `k` from `0` to the common dimension size (e.g., `n`).
3.  In each step of the `k` loop, add the product of `A[i][k]` and `B[k][j]` to your sum.

### Code Examples

#### 1. Calculating a Single Element `C[i][j]`

Let's consider two simple matrices, `A` (2x3) and `B` (3x2), and calculate one element, say `C[0][1]` (the element in the first row, second column of the result matrix).

```python
# Example matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

# We want to calculate C[0][1]
# This requires the 0th row of A and the 1st column of B

# Initialize the sum for C[0][1]
c_0_1 = 0

# Loop through the common dimension (number of columns in A, or rows in B)
# In this case, it's 3 (elements A[0][0], A[0][1], A[0][2] and B[0][1], B[1][1], B[2][1])
for k in range(len(A[0])): # len(A[0]) gives the number of columns in A
    c_0_1 += A[0][k] * B[k][1]

print(f"The element C[0][1] is: {c_0_1}")
# Let's trace C[0][1]:
# k=0: A[0][0]*B[0][1] = 1*8 = 8
# k=1: A[0][1]*B[1][1] = 2*10 = 20
# k=2: A[0][2]*B[2][1] = 3*12 = 36
# Sum = 8 + 20 + 36 = 64
```

**How it works:**
The code iterates through `k` (0, 1, 2). For each `k`:
*   `A[0][k]` accesses elements from the 0th row of `A`.
*   `B[k][1]` accesses elements from the 1st column of `B`.
The products are accumulated in `c_0_1`.

#### 2. Full Matrix Multiplication

To get the entire result matrix `C`, we need to repeat the above calculation for every possible `(i, j)` pair. This requires nesting loops.

```python
# Example matrices (A is 2x3, B is 3x2)
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

# Get dimensions
rows_A = len(A)        # 2
cols_A = len(A[0])     # 3
rows_B = len(B)        # 3
cols_B = len(B[0])     # 2

# Check if multiplication is possible (cols_A must equal rows_B)
if cols_A != rows_B:
    print("Error: Cannot multiply matrices. Number of columns in A must equal number of rows in B.")
else:
    # Initialize the result matrix C with zeros
    # C will have dimensions rows_A x cols_B (2x2 in this example)
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Loop through rows of A (determines 'i' for C)
    for i in range(rows_A):
        # Loop through columns of B (determines 'j' for C)
        for j in range(cols_B):
            # This inner loop calculates the dot product for C[i][j]
            # 'k' iterates through the common dimension
            for k in range(cols_A): # Can also use range(rows_B)
                C[i][j] += A[i][k] * B[k][j]

    print("Result Matrix C:")
    for row in C:
        print(row)

# Expected output for C:
# C[0][0] = (1*7) + (2*9) + (3*11) = 7 + 18 + 33 = 58
# C[0][1] = (1*8) + (2*10) + (3*12) = 8 + 20 + 36 = 64
# C[1][0] = (4*7) + (5*9) + (6*11) = 28 + 45 + 66 = 139
# C[1][1] = (4*8) + (5*10) + (6*12) = 32 + 50 + 72 = 154
# Result: [[58, 64], [139, 154]]
```

**How it works:**
1.  **Outer Loops (`i` and `j`):** These two loops iterate through every possible `(row, column)` position in the target matrix `C`.
    *   `i` represents the current row of `C` (and thus the row from `A` to use).
    *   `j` represents the current column of `C` (and thus the column from `B` to use).
2.  **Inner Loop (`k`):** For each `(i, j)` pair, this loop calculates the sum of products (the "dot product") as explained earlier.
    *   `k` acts as the "moving" index that links the column of `A` and the row of `B`.
3.  **Accumulation:** `C[i][j] += A[i][k] * B[k][j]` adds each product to the running total for the specific `C[i][j]` element.

## Summary and Important Tips

*   **Core Idea:** Matrix multiplication boils down to computing each element `C[i][j]` as a sum of products from `A`'s `i`-th row and `B`'s `j`-th column.
*   **0-Based Indexing:** Always remember that programming languages typically use 0-based indexing for rows and columns, which might differ from mathematical notation. This is a common point of confusion.
*   **Dimensionality Check:** Ensure that the number of columns in the first matrix (`A`) matches the number of rows in the second matrix (`B`). If not, multiplication is impossible.
*   **Result Matrix Size:** If `A` is `m x n` and `B` is `n x p`, the result `C` will be `m x p`.
*   **Start Simple:** When first programming matrix multiplication, begin with small matrices (like 2x2 or 3x3) where you can easily verify the results by hand. This helps build confidence and understand the loop structure.
*   **Patience is Key:** It's normal to find this concept a bit tricky at first, especially with the nested loops and changing indices. Break down the problem into calculating one element, then generalize.