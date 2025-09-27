# Operators and Expressions in Python

This document provides a comprehensive overview of operators and expressions in Python, focusing on their types, how they work, and practical examples.

---

## Key Topics

Python operators are categorized into three main types:
1.  **Arithmetic Operators**: Used for mathematical calculations.
2.  **Relational Operators**: Used for comparing values.
3.  **Logical Operators**: Used for combining or modifying Boolean expressions.

### 1. Arithmetic Operators

Arithmetic operators perform standard mathematical operations on numbers.

*   **Basic Arithmetic Operators:** These are familiar from basic mathematics.
    *   **Addition (`+`)**: Adds two operands.
        ```python
        print(2 + 3) # Output: 5
        ```
    *   **Subtraction (`-`)**: Subtracts the right operand from the left.
        ```python
        print(9 - 1) # Output: 8
        ```
    *   **Multiplication (`*`)**: Multiplies two operands.
        ```python
        print(5 * 4) # Output: 20
        ```
    *   **Division (`/`)**: Divides the left operand by the right operand. The result is always a **floating-point number** (a number with a decimal part), even if the division is exact.
        ```python
        print(7 / 3) # Output: 2.3333333333333335
        ```
        *   **Pain Point**: Remember that even `10 / 2` will result in `5.0` (a float), not `5` (an integer). This is a common difference compared to some other programming languages.

*   **Specialized Arithmetic Operators:** These offer more specific mathematical functionalities.
    *   **Floor Division (`//`)**: Divides the left operand by the right operand and returns only the **integer part** of the quotient. It effectively "floors" the result, meaning it rounds down to the nearest whole number.
        ```python
        print(7 // 3) # Output: 2
        ```
        *   **How it works**: For `7 // 3`, the actual division `7 / 3` is `2.333...`. Floor division takes only the integer part, which is `2`.
        *   **Confusion Point**: While `/` gives `2.333...`, `//` gives `2`. The key is that `//` discards the fractional part.

    *   **Modulus (`%`)**: Divides the left operand by the right operand and returns the **remainder** of the division.
        ```python
        print(7 % 3) # Output: 1
        ```
        *   **How it works**: When `7` is divided by `3`, `3` goes into `7` two times (`3 * 2 = 6`), and there is `1` left over (`7 - 6 = 1`). This `1` is the remainder.
        *   **Practical Use**: Useful for tasks like checking if a number is even or odd (a number `% 2` will be `0` if even, `1` if odd), or for cyclic operations.

    *   **Exponential (`**`)**: Raises the left operand to the power of the right operand.
        ```python
        print(6 ** 2) # Output: 36
        ```
        *   **How it works**: `6 ** 2` means 6 raised to the power of 2, which is `6 * 6 = 36`.

### 2. Relational Operators (Comparison Operators)

Relational operators are used to compare two values. They always return a **Boolean value**: `True` or `False`.

*   **Greater Than (`>`)**: Checks if the left operand is greater than the right operand.
    ```python
    print(5 > 10) # Output: False (5 is not greater than 10)
    print(10 > 5) # Output: True (10 is greater than 5)
    ```

*   **Less Than (`<`)**: Checks if the left operand is less than the right operand.
    ```python
    print(5 < 10) # Output: True (5 is less than 10)
    print(10 < 5) # Output: False (10 is not less than 5)
    ```

*   **Greater Than or Equal To (`>=`)**: Checks if the left operand is greater than or equal to the right operand.
    ```python
    print(5 > 5)  # Output: False (5 is not strictly greater than 5)
    print(5 >= 5) # Output: True (5 is equal to 5, satisfying the "equal to" part)
    ```
    *   **Confusion Point**: `>` requires strict inequality, while `>=` allows for equality.

*   **Less Than or Equal To (`<=`)**: Checks if the left operand is less than or equal to the right operand.
    ```python
    print(5 < 5)  # Output: False (5 is not strictly less than 5)
    print(5 <= 5) # Output: True (5 is equal to 5, satisfying the "equal to" part)
    ```

*   **Equal To (`==`)**: Checks if the two operands are equal.
    ```python
    print(5 == 50) # Output: False (5 is not equal to 50)
    print(5 == 5)  # Output: True (5 is equal to 5)
    ```
    *   **Crucial Pain Point**: Do **NOT** confuse `==` (comparison operator) with `=` (assignment operator).
        *   `x = 5` **assigns** the value `5` to the variable `x`.
        *   `x == 5` **checks** if the value of `x` is `5`.

*   **Not Equal To (`!=`)**: Checks if the two operands are not equal. This is the exact opposite of the `==` operator.
    ```python
    print(5 != 50) # Output: True (5 is indeed not equal to 50)
    print(5 != 5)  # Output: False (5 is equal to 5, so it's not "not equal to")
    ```

### 3. Logical Operators

Logical operators combine or modify Boolean expressions (expressions that evaluate to `True` or `False`). They also return a Boolean value.

*   **`and` Operator**: Returns `True` if **both** operands are `True`. Otherwise, it returns `False`.
    ```python
    print(True and True)   # Output: True
    print(True and False)  # Output: False
    print(False and True)  # Output: False
    print(False and False) # Output: False
    ```
    *   **How it works**: Think of it as requiring all conditions to be met. If even one condition is `False`, the entire `and` expression becomes `False`.

*   **`or` Operator**: Returns `True` if **at least one** of the operands is `True`. It only returns `False` if both operands are `False`.
    ```python
    print(True or True)   # Output: True
    print(True or False)  # Output: True
    print(False or True)  # Output: True
    print(False or False) # Output: False
    ```
    *   **How it works**: Think of it as needing just one condition to be met. If any condition is `True`, the entire `or` expression becomes `True`.

*   **`not` Operator**: This is a unary operator, meaning it operates on a single operand. It **inverts** the Boolean value of its operand. If the operand is `True`, `not` makes it `False`, and vice versa.
    ```python
    print(not True)  # Output: False
    print(not False) # Output: True
    ```
    *   **Parentheses Usage**: The `not` operator can be used with or without parentheses around the operand. Both `not True` and `not (True)` will produce the same result. It's often good practice to use parentheses for clarity with more complex expressions.
        ```python
        print(not (5 > 10)) # Output: True (because 5 > 10 is False, and not False is True)
        ```

---

## Summary and Important Tips

*   **Operators are building blocks**: They allow you to perform calculations, make comparisons, and control logic in your programs.
*   **Know your types**:
    *   Arithmetic operators often work with numbers and produce numbers (integers or floats).
    *   Relational and Logical operators always produce **Boolean values** (`True` or `False`).
*   **Floor Division vs. Regular Division**: Remember `//` gives the whole number part, while `/` always gives a decimal number (float).
*   **Modulus for Remainders**: The `%` operator is incredibly useful for specific checks, like even/odd numbers.
*   **Comparison vs. Assignment**: Always use `==` for checking equality, and `=` for assigning values to variables. This is a very common beginner mistake.
*   **Logical Operator Logic**:
    *   `and` requires *all* parts to be true.
    *   `or` requires *at least one* part to be true.
    *   `not` simply flips the truth value.
*   **Practice is key**: The best way to understand these operators is to experiment with them in your Python code editor. Try different combinations and predict the output before running your code.