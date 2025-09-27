# Matrix Multiplication Using Functions

This document provides a comprehensive guide to understanding and implementing matrix multiplication in Python using a modular approach with functions. It emphasizes simplifying complex problems by breaking them into smaller, manageable parts.

## Key Topics

### 1. Introduction to Matrix Multiplication (Review)

Matrix multiplication is a fundamental operation in linear algebra. When multiplying two matrices, say matrix A and matrix B, to get a resulting matrix C, each entry `C_ij` (read as "C sub i j") is calculated as a **dot product**.

*   **`C_ij` Definition:** The entry at the `i`-th row and `j`-th column of the result matrix C (`C_ij`) is found by taking the dot product of the `i`-th row of matrix A and the `j`-th column of matrix B.
    *   **Example:** To find `C_11` (first row, first column), you multiply the elements of the first row of A with the corresponding elements of the first column of B and sum them up.
*   **Dot Product:** The dot product of two vectors (or lists in programming) is calculated by multiplying corresponding elements and then summing these products.
    *   **Example:** For vectors `U = [u1, u2, u3]` and `V = [v1, v2, v3]`, their dot product is `u1*v1 + u2*v2 + u3*v3`.
*   **Initial Approach (Without Functions):** A direct implementation of matrix multiplication typically involves three nested loops. While conceptually sound, this can lead to code that is difficult to read, understand, and debug, especially for beginners. The mental overhead of tracking multiple loops and indices can be high.

### 2. The Power of Functions: A Modular Approach

When dealing with complex problems in programming, it's easy for the mind to get overwhelmed and confused. The idea of using functions offers a structured and "easy way" to tackle such challenges.

*   **Why Use Functions?**
    *   **Organization:** Functions help keep your code organized by grouping related operations into distinct blocks.
    *   **Modularity:** They allow you to write small, independent pieces of code (modules) that perform specific tasks.
    *   **Reusability:** Once a function is written and tested, it can be called and reused multiple times throughout your program, or even in other programs, without rewriting the code. This is like having a specialized "tool" that you can use whenever needed.
    *   **Reduced Complexity:** By breaking a large problem into smaller sub-problems, you can focus on solving one small piece at a time, simplifying the overall thought process.
    *   **Easier Debugging:** If an issue arises, you can isolate and test individual functions, making it easier to pinpoint and fix errors.
*   **The `def` Keyword in Python:** In Python, functions are defined using the `def` keyword, followed by the function name, parentheses for parameters, and a colon.
    ```python
    def my_function(parameter1, parameter2):
        # Code block for the function
        # ...
        return result
    ```
*   **Breaking Down Matrix Multiplication:** To implement matrix multiplication using functions, we can identify the core, repeatable tasks:
    1.  Initializing a result matrix with zeros.
    2.  Calculating the dot product of two lists (vectors).
    3.  Extracting a specific row from a matrix.
    4.  Extracting a specific column from a matrix.

### 3. Implementing Core Functions

Let's create individual functions for each of the identified sub-routines.

#### 3.1. `initialize_mat(dim)`: Creating a Zero Matrix

This function creates a square matrix of a given `dimension` (`dim`) where all entries are initialized to zero.

*   **Goal:** To return a `dim` x `dim` list of lists, like `[[0, 0, 0], [0, 0, 0], [0, 0, 0]]` for `dim=3`.
*   **Common Pitfalls:** A common mistake is trying to create nested lists incorrectly, which might lead to all rows referencing the same list object. The correct way involves appending distinct lists for each row.
*   **How it Works:**
    1.  Start with an empty list `C`. This will hold the rows of the matrix.
    2.  Loop `dim` times (once for each row). In each iteration, append an empty list `[]` to `C`. This creates the `dim` empty rows.
    3.  Then, for each of these empty rows (`C[i]`), loop `dim` times again and append `0` to it. This fills each row with `dim` zeros.
*   **Code Example:**
    ```python
    def initialize_mat(dim):
        """
        Initializes a dim x dim matrix with all entries set to 0.
        """
        C = []
        for i in range(dim):
            C.append([])  # Append an empty list for each row
            for j in range(dim):
                C[i].append(0) # Fill each row with zeros
        return C

    # How it works:
    # 1. C = []
    # 2. First loop (i=0):
    #    - C.append([]) -> C = [[]]
    #    - Second loop (j=0,1,2 for dim=3):
    #      - C[0].append(0) -> C = [[0]]
    #      - C[0].append(0) -> C = [[0, 0]]
    #      - C[0].append(0) -> C = [[0, 0, 0]]
    # 3. Second loop (i=1):
    #    - C.append([]) -> C = [[0,0,0], []]
    #    - Second loop (j=0,1,2 for dim=3):
    #      - C[1].append(0) -> C = [[0,0,0], [0]]
    #      - ... -> C = [[0,0,0], [0,0,0]]
    # 4. Continues until C is fully initialized.

    # Example Usage:
    matrix_3x3 = initialize_mat(3)
    print("Initialized 3x3 matrix:")
    print(matrix_3x3)
    # Expected output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    matrix_2x2 = initialize_mat(2)
    print("\nInitialized 2x2 matrix:")
    print(matrix_2x2)
    # Expected output: [[0, 0], [0, 0]]
    ```

#### 3.2. `dot_product(U, V)`: Calculating the Dot Product of Two Vectors

This function takes two lists (representing vectors) and calculates their dot product.

*   **Assumptions:** It assumes that the two input lists, `U` and `V`, have the same length (dimension). This is crucial for valid dot product calculation.
*   **How it Works:**
    1.  Initialize a variable `ans` to `0`. This will store the sum of products.
    2.  Determine the `dim` (length) of the vectors (e.g., `len(U)`).
    3.  Loop from `0` up to `dim-1` (using a loop variable like `i`).
    4.  In each iteration, multiply the `i`-th element of `U` with the `i`-th element of `V` (`U[i] * V[i]`) and add this product to `ans`.
    5.  Return the final `ans`.
*   **Code Example:**
    ```python
    def dot_product(U, V):
        """
        Calculates the dot product of two vectors (lists).
        Assumes U and V have the same length.
        """
        ans = 0
        dim = len(U) # Get the dimension (length) of the vectors
        for i in range(dim):
            ans += U[i] * V[i] # Sum of corresponding element products
        return ans

    # How it works:
    # U = [1, 2, 3], V = [7, 1, 2]
    # 1. ans = 0, dim = 3
    # 2. i = 0: ans = 0 + (U[0] * V[0]) = 0 + (1 * 7) = 7
    # 3. i = 1: ans = 7 + (U[1] * V[1]) = 7 + (2 * 1) = 9
    # 4. i = 2: ans = 9 + (U[2] * V[2]) = 9 + (3 * 2) = 15
    # 5. Returns 15

    # Example Usage:
    vector_X = [1, 2, 3]
    vector_Y = [7, 1, 2]
    result_dot_product = dot_product(vector_X, vector_Y)
    print(f"\nDot product of {vector_X} and {vector_Y}: {result_dot_product}")
    # Expected output: 15

    vector_A = [1, 2]
    vector_B = [7, 3]
    print(f"Dot product of {vector_A} and {vector_B}: {dot_product(vector_A, vector_B)}")
    # Expected output: 13 (1*7 + 2*3 = 7 + 6 = 13)
    ```
*   **Important Note on Variable Names:** When defining a function, the parameter names (like `U` and `V`) are placeholders. You can call the function with any variable names outside, and those values will be passed into `U` and `V` inside the function.

#### 3.3. `row_i(M, i)`: Extracting a Specific Row from a Matrix

This function takes a matrix `M` (list of lists) and an index `i`, and returns the `i`-th row of that matrix.

*   **Goal:** To get a list representing the `i`-th row. For example, in `[[1,2,3],[4,5,6],[7,8,9]]`, `row_i(M, 0)` should return `[1,2,3]`.
*   **How it Works:**
    1.  Initialize an empty list `l`. This will store the elements of the extracted row.
    2.  Determine the `dim` (number of columns) of the matrix. Assuming a square matrix, `len(M)` or `len(M[0])` works.
    3.  Loop through the column indices (`k` from `0` to `dim-1`).
    4.  In each iteration, append the element at `M[i][k]` to `l`. Here, `i` (the target row index) remains constant, while `k` (the column index) changes.
    5.  Return `l`.
*   **Code Example:**
    ```python
    def row_i(M, i):
        """
        Extracts the i-th row from a matrix M.
        """
        l = [] # List to store the row elements
        dim = len(M) # Assuming M is a square matrix
        # Loop through columns (k) for the specific row (i)
        for k in range(dim):
            l.append(M[i][k]) # Append element at row i, column k
        return l

    # How it works:
    # M = [[1,2,3],[4,5,6],[7,8,9]], i = 0
    # 1. l = [], dim = 3
    # 2. k = 0: l.append(M[0][0]) -> l.append(1) -> l = [1]
    # 3. k = 1: l.append(M[0][1]) -> l.append(2) -> l = [1, 2]
    # 4. k = 2: l.append(M[0][2]) -> l.append(3) -> l = [1, 2, 3]
    # 5. Returns [1, 2, 3]

    # Example Usage:
    matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"\nMatrix A:\n{matrix_A[0]}\n{matrix_A[1]}\n{matrix_A[2]}")
    print(f"First row (index 0) of A: {row_i(matrix_A, 0)}")
    # Expected output: [1, 2, 3]
    print(f"Second row (index 1) of A: {row_i(matrix_A, 1)}")
    # Expected output: [4, 5, 6]
    # print(f"Invalid row (index 3) of A: {row_i(matrix_A, 3)}") # This would cause an IndexError
    ```
*   **Confusion Point:** Be careful to use different variable names for the input row index (`i`) and the loop variable (`k`) to avoid confusion, especially if you're thinking about the `i`-th row, `j`-th column overall.

#### 3.4. `column_j(M, j)`: Extracting a Specific Column from a Matrix

This function takes a matrix `M` and an index `j`, and returns the `j`-th column of that matrix.

*   **Goal:** To get a list representing the `j`-th column. For example, in `[[1,2,3],[4,5,6],[7,8,9]]`, `column_j(M, 0)` should return `[1,4,7]`.
*   **How it Works:**
    1.  Initialize an empty list `l`.
    2.  Determine the `dim` (number of rows) of the matrix.
    3.  Loop through the row indices (`k` from `0` to `dim-1`).
    4.  In each iteration, append the element at `M[k][j]` to `l`. Here, `j` (the target column index) remains constant, while `k` (the row index) changes.
    5.  Return `l`.
*   **Code Example:**
    ```python
    def column_j(M, j):
        """
        Extracts the j-th column from a matrix M.
        """
        l = [] # List to store the column elements
        dim = len(M) # Assuming M is a square matrix
        # Loop through rows (k) for the specific column (j)
        for k in range(dim):
            l.append(M[k][j]) # Append element at row k, column j
        return l

    # How it works:
    # M = [[1,2,3],[4,5,6],[7,8,9]], j = 0
    # 1. l = [], dim = 3
    # 2. k = 0: l.append(M[0][0]) -> l.append(1) -> l = [1]
    # 3. k = 1: l.append(M[1][0]) -> l.append(4) -> l = [1, 4]
    # 4. k = 2: l.append(M[2][0]) -> l.append(7) -> l = [1, 4, 7]
    # 5. Returns [1, 4, 7]

    # Example Usage:
    matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"\nMatrix A:\n{matrix_A[0]}\n{matrix_A[1]}\n{matrix_A[2]}")
    print(f"First column (index 0) of A: {column_j(matrix_A, 0)}")
    # Expected output: [1, 4, 7]
    print(f"Third column (index 2) of A: {column_j(matrix_A, 2)}")
    # Expected output: [3, 6, 9]
    ```

### 4. Assembling the Main Logic: `mat_multiplication(A, B)`

Now that all the helper functions are ready, we can combine them to perform the full matrix multiplication.

*   **Assumptions:** For simplicity in this introductory context, we assume that both input matrices `A` and `B` are square matrices of the same dimension.
*   **How it Works:**
    1.  Determine the `dim` (dimension) of the matrices (e.g., `len(A)`).
    2.  Initialize a result matrix `C` with zeros using `initialize_mat(dim)`.
    3.  Use two nested loops:
        *   The outer loop iterates through `i` (row index for matrix C, from `0` to `dim-1`).
        *   The inner loop iterates through `j` (column index for matrix C, from `0` to `dim-1`).
    4.  Inside these loops, for each `C[i][j]` entry:
        *   Extract the `i`-th row of matrix `A` using `row_i(A, i)`.
        *   Extract the `j`-th column of matrix `B` using `column_j(B, j)`.
        *   Calculate the dot product of these two extracted vectors using `dot_product()`.
        *   Assign the result to `C[i][j]`.
    5.  Return the final matrix `C`.
*   **Code Example:**
    ```python
    def mat_multiplication(A, B):
        """
        Multiplies two square matrices A and B using helper functions.
        Assumes A and B are square matrices of the same dimension.
        """
        dim = len(A) # Get the dimension of the matrices
        C = initialize_mat(dim) # Initialize the result matrix C with zeros

        # Iterate through rows of C (i)
        for i in range(dim):
            # Iterate through columns of C (j)
            for j in range(dim):
                # Calculate C[i][j] as the dot product of
                # the i-th row of A and the j-th column of B
                C[i][j] = dot_product(row_i(A, i), column_j(B, j))
        return C

    # Example Usage:
    matrix_A_example = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]

    matrix_B_example = [[1, 2, 1],
                        [3, 1, 7],
                        [6, 2, 3]]

    result_matrix = mat_multiplication(matrix_A_example, matrix_B_example)
    print("\nResult of Matrix Multiplication (A * B):")
    for row in result_matrix:
        print(row)

    # Expected output verification (e.g., for C[0][0]):
    # Row 0 of A: [1, 2, 3]
    # Column 0 of B: [1, 3, 6]
    # Dot product: (1*1) + (2*3) + (3*6) = 1 + 6 + 18 = 25
    # The output C[0][0] should be 25.
    # (Other entries can be verified similarly, e.g., C[1][2] = 57 from the lecture)
    ```

### 5. Summary and Important Tips

By breaking down the matrix multiplication problem into smaller, specialized functions, we achieved a much clearer, more manageable, and reusable code structure. This "functional approach to programming" is a powerful technique for handling complexity.

*   **Key Advantages of Using Functions:**
    *   **Clarity:** The code becomes easier to read and understand because each function has a single, well-defined purpose.
    *   **Maintainability:** Changes or fixes to a specific logic can be done within a single function without affecting other parts of the code.
    *   **Reusability:** Functions like `dot_product`, `row_i`, and `column_j` can be reused in other matrix-related operations or programs.
    *   **Manageable Thinking:** You only need to think about one small task at a time (e.g., "how to initialize a matrix" or "how to get a row"), rather than the entire complex problem at once.
*   **Psychology of a Programmer:** The journey of programming often involves moments of frustration (when code doesn't work), slow thinking, debugging, and ultimately, immense satisfaction when the code runs correctly. This is a natural part of the learning process.
*   **Practical Tip:** The best way to learn and internalize these concepts is to actively code alongside. Open a Python editor or interpreter and type out each function, test it, and then combine them. This hands-on practice helps solidify understanding and build confidence.
*   **Future Concepts:** While not explicitly covered in detail here, understanding the "scope" of variables (which variables are accessible where) becomes important when using functions. This is a concept to explore further in advanced programming.