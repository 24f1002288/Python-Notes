Here are comprehensive notes on conditional statements in Python:

# Understanding Conditional Logic in Python: `if`, `else`, and `elif`

This document explores how to make decisions in Python programs using conditional statements. These statements allow your code to execute different blocks of instructions based on whether certain conditions are true or false.

## Key Concepts for Conditional Logic

Before diving into examples, let's understand some fundamental tools:

### 1. Taking User Input

Programs often need to interact with users. Python's `input()` function is used to get information directly from the user.

*   **`input()` Function:**
    *   When `input("Your message here: ")` is called, the message inside the parentheses is displayed to the user.
    *   The program then pauses, waiting for the user to type something and press Enter.
    *   Whatever the user types is returned as a **string** (text).

*   **`int()` Function for Type Conversion:**
    *   Since `input()` always returns a string, if you need to perform mathematical operations (like checking if a number is even or odd), you must convert the input string to a number.
    *   The `int()` function converts a string representation of a number into an integer (whole number).
    *   **Example:** `num_str = input("Enter a number: ")` would store "123" (as text), while `num_int = int(num_str)` would store `123` (as a number).

### 2. The Modulo Operator (`%`)

The modulo operator is incredibly useful for number-related checks.

*   **Purpose:** It calculates the **remainder** after division.
*   **How it works:** `A % B` gives you what's left over when `A` is divided by `B`.
    *   Example: `5 % 2` is `1` (because 5 divided by 2 is 2 with a remainder of 1).
    *   Example: `10 % 2` is `0` (because 10 divided by 2 is 5 with a remainder of 0).
*   **Common Use Cases:**
    *   **Even/Odd Check:** If a number `X % 2` is `0`, `X` is even. Otherwise, it's odd.
    *   **Last Digit Check:** `X % 10` gives you the last digit of number `X`. (e.g., `123 % 10` is `3`).

### 3. Comparison Operators

These operators are used to compare values and form conditions that evaluate to either `True` or `False`.

*   `==` (Equal to)
*   `!=` (Not equal to)
*   `>` (Greater than)
*   `<` (Less than)
*   `>=` (Greater than or equal to)
*   `<=` (Less than or equal to)

### 4. Logical Operators

These operators combine multiple conditions.

*   `and`: Both conditions must be `True` for the overall condition to be `True`.
*   `or`: At least one condition must be `True` for the overall condition to be `True`.
*   `not`: Reverses the truth value of a condition (e.g., `not True` is `False`).

## Problem 1: Checking for Even or Odd Numbers

This problem demonstrates the basic `if-else` structure.

**Problem Statement:** Determine if a given number is even or odd.

**Logic:**
An even number is any integer that is exactly divisible by 2, leaving no remainder. An odd number leaves a remainder of 1 when divided by 2. We can use the modulo operator (`%`) for this.

**Detailed Steps:**
1.  Ask the user to `enter a number`.
2.  Store this input in a variable, ensuring it's converted to an integer.
3.  Check if the number modulo 2 (`num % 2`) is equal to 0.
    *   If `True`, the number is even.
    *   If `False`, the number is odd.

**Code Example 1: Even or Odd**

```python
# 1. Accept input from the user and convert it to an integer
num = int(input("Enter a number: "))

# 2. Use an if-else statement to check the condition
if num % 2 == 0:
    # This block executes if the condition (num % 2 == 0) is True
    print(f"{num} is an even number.")
else:
    # This block executes if the condition is False
    print(f"{num} is an odd number.")

# How it works:
# If the user enters 4:
#   num = 4
#   4 % 2 == 0  (True) -> Prints "4 is an even number."
# If the user enters 5:
#   num = 5
#   5 % 2 == 0  (False) -> Executes the else block -> Prints "5 is an odd number."
# This also works for negative numbers and zero:
# If the user enters 0:
#   0 % 2 == 0 (True) -> Prints "0 is an even number."
# If the user enters -7:
#   -7 % 2 == -1 or 1 (depending on Python version/implementation specifics,
#                       but the remainder is non-zero, so the condition is False)
#                     -> Prints "-7 is an odd number."
```

## Problem 2: Determining the Last Digit (0 or 5)

This problem introduces **nested `if` statements**, where one conditional check is inside another.

**Problem Statement:** Find whether a given number ends with 0, 5, or any other digit.

**Logic:**
The last digit of any number can be found using the modulo 10 operator (`num % 10`).
*   If `num % 10` is `0`, the number ends in 0.
*   If `num % 10` is `5`, the number ends in 5.
*   Otherwise, it ends with another digit.

However, a more efficient way when dealing with 0 and 5 specifically:
*   Numbers ending in 0 are always divisible by 10 (and thus by 5).
*   Numbers ending in 5 are always divisible by 5 (but not by 10).

Therefore, we can check for divisibility by 5 first. If it's divisible by 5, then we perform a *second* check to see if it's also divisible by 10.

**Detailed Steps:**
1.  Accept a number from the user and convert it to an integer.
2.  **Outer Condition:** Check if the number is divisible by 5 (`num % 5 == 0`).
    *   If `True` (divisible by 5):
        *   **Inner Condition:** Check if the number is also divisible by 10 (`num % 10 == 0`).
            *   If `True`, the number ends with 0.
            *   If `False` (meaning it's divisible by 5 but not 10), the number must end with 5.
    *   If `False` (not divisible by 5):
        *   The number ends with "any other number".

**Code Example 2: Checking the Last Digit**

```python
# 1. Accept input from the user and convert it to an integer
num = int(input("Enter a number: "))

# 2. Check if the number is divisible by 5
if num % 5 == 0:
    # If divisible by 5, now check if it's also divisible by 10
    if num % 10 == 0:
        print(f"The number {num} ends with 0.")
    else:
        # If divisible by 5 but not by 10, it must end with 5
        print(f"The number {num} ends with 5.")
else:
    # If not divisible by 5 at all
    print(f"The number {num} ends with some other digit.")

# How it works:
# If the user enters 20:
#   num = 20
#   20 % 5 == 0 (True) -> Enters first 'if' block
#   20 % 10 == 0 (True) -> Enters inner 'if' block -> Prints "The number 20 ends with 0."
# If the user enters 14:
#   num = 14
#   14 % 5 == 0 (False) -> Enters outer 'else' block -> Prints "The number 14 ends with some other digit."
# If the user enters 5:
#   num = 5
#   5 % 5 == 0 (True) -> Enters first 'if' block
#   5 % 10 == 0 (False) -> Enters inner 'else' block -> Prints "The number 5 ends with 5."
```

## Problem 3: Calculating Student Grades

This problem highlights the benefits of `elif` for handling multiple, mutually exclusive conditions.

**Problem Statement:** Assign a grade (A, B, C, D, E) based on marks (0-100) using the following scale:
*   A: marks >= 90
*   B: marks >= 80 and < 90
*   C: marks >= 70 and < 80
*   D: marks >= 60 and < 70
*   E: marks < 60
*   Invalid Input: marks < 0 or > 100

### Initial Approach (using independent `if` statements)

An initial thought might be to use a series of `if` statements for each grade.

```python
# Initial (less optimal) approach for grades
marks = int(input("Enter marks: "))

# Problem: If a student gets 95, all these 'if' conditions might be checked.
# Also, if not structured carefully, a student with 95 might technically satisfy
# 'marks >= 80' as well, leading to multiple prints or incorrect logic.

# Pain Point 1: Typos (NameError)
# If you misspell 'marks' (e.g., 'markss') in input or any condition,
# Python will raise a 'NameError' because the variable isn't defined with that spelling.
# Example: markss = int(input("Enter marks: "))
#          if marks >= 90: # This 'marks' is not defined, leading to NameError

# Pain Point 2: Handling Invalid Input Range
# The problem statement specifies marks from 0 to 100. What if the user enters -5 or 110?
# Without explicit checks, these values would fall into the 'E' grade category, which is incorrect.
# Example with initial separate ifs:
# If marks = -5:
#   if -5 >= 90 (False)
#   if -5 >= 80 and -5 < 90 (False)
#   ...
#   if -5 < 60 (True) -> Prints 'E' (Expected: 'Invalid Input')

# To fix the invalid input range:
if marks >= 0 and marks <= 100:
    if marks >= 90:
        print("Grade A")
    if marks >= 80 and marks < 90: # This 'and marks < 90' is crucial here
        print("Grade B")
    if marks >= 70 and marks < 80:
        print("Grade C")
    if marks >= 60 and marks < 70:
        print("Grade D")
    if marks < 60:
        print("Grade E")
else:
    print("Invalid Input")

# While this works, notice the repeated 'and marks < X' conditions.
# This makes the code a bit verbose and less efficient, as each 'if' is checked independently.
```

### Introducing `elif` (Else-If)

The `elif` statement is designed for situations where you have multiple conditions, and only one should be executed. It's a cleaner and more efficient way to handle chained conditionals.

*   **How `elif` works:**
    1.  The `if` condition is checked first. If `True`, its block executes, and the rest of the `elif`/`else` chain is skipped.
    2.  If the `if` condition is `False`, the first `elif` condition is checked. If `True`, its block executes, and the rest are skipped.
    3.  This continues down the chain.
    4.  If none of the `if` or `elif` conditions are `True`, the `else` block (if present) executes.

**Advantage of `elif`:**
When an `elif` condition is checked, you *already know* that the previous `if` or `elif` conditions were `False`. This means you don't need to explicitly add `and marks < 90` in the B grade condition, because if `marks >= 90` had been true, the B grade `elif` would never have been reached.

**Code Example 3: Student Grades with `elif`**

```python
marks = int(input("Enter marks: "))

# First, check for valid input range
if marks >= 0 and marks <= 100:
    # Now, use elif for the grade conditions.
    # The order matters here (highest marks first)!
    if marks >= 90:
        print("Grade A")
    elif marks >= 80: # We only reach here if marks < 90, so 'and marks < 90' is implicit
        print("Grade B")
    elif marks >= 70: # We only reach here if marks < 80, so 'and marks < 80' is implicit
        print("Grade C")
    elif marks >= 60: # We only reach here if marks < 70, so 'and marks < 70' is implicit
        print("Grade D")
    else: # We only reach here if marks < 60 (and valid range), so this covers Grade E
        print("Grade E")
else:
    print("Invalid Input")

# How it works:
# If the user enters 95:
#   marks = 95
#   95 >= 0 and 95 <= 100 (True) -> Enters outer 'if'
#   95 >= 90 (True) -> Prints "Grade A" -> The rest of the elif/else chain is skipped.
# If the user enters 87:
#   marks = 87
#   87 >= 0 and 87 <= 100 (True) -> Enters outer 'if'
#   87 >= 90 (False)
#   87 >= 80 (True) -> Prints "Grade B" -> The rest of the elif/else chain is skipped.
# If the user enters -5:
#   marks = -5
#   -5 >= 0 and -5 <= 100 (False) -> Enters outer 'else' -> Prints "Invalid Input".
```

## Problem 4: Translating a Flowchart into Python Code

This problem demonstrates how to translate a visual, logical flow (like a flowchart) into structured Python code using nested `if-else` blocks and user-defined thresholds.

**Problem Statement:** Convert a given travel flowchart into Python code. The flowchart describes a travel decision process based on time and price, where "longer time" and "higher price" are user-defined.

**Key Idea:** The words "longer" and "higher" are relative. Instead of hardcoding values, we should ask the user to define what "longer" time or "higher" price means to them.

**Flowchart Logic Breakdown:**
1.  **Start:** Print "Travel from City A to City B".
2.  **Input Time & Longer Threshold:** Ask for the `time` and what `longer` time means (e.g., in hours).
3.  **Decision 1: Time Comparison (`if time >= longer`):**
    *   **If Time is Longer (True Branch):**
        *   Input `price` and what `higher` price means.
        *   **Decision 2: Price Comparison (`if price >= higher`):**
            *   **If Price is Higher (True Branch):** Print "Choose Train".
            *   **If Price is Lower (False Branch):** Print "Choose Coach".
    *   **If Time is Shorter (False Branch - `else`):**
        *   Input `price` and what `higher` price means.
        *   **Decision 3: Price Comparison (`if price >= higher`):**
            *   **If Price is Higher (True Branch):** Print "Choose Day Time Flight".
            *   **If Price is Lower (False Branch):** Print "Choose Red Eye Flight".
4.  **End (outside all `if-else` blocks):** Print "Arrive City B".

**Code Example 4: Flowchart Conversion**

```python
print("Travel from City A to City B")

# Get user input for time and the definition of 'longer'
time = int(input("Enter time (in hours): "))
longer_threshold = int(input("Define 'longer' time (e.g., 5 for 5 hours): "))

# First main decision based on time
if time >= longer_threshold:
    print("\nTime is considered 'longer'.")
    # Nested decision for price if time is longer
    price = int(input("Enter price: "))
    higher_threshold = int(input("Define 'higher' price: "))

    if price >= higher_threshold:
        print("Choose Train")
    else:
        print("Choose Coach")
else:
    print("\nTime is considered 'shorter'.")
    # Nested decision for price if time is shorter
    price = int(input("Enter price: "))
    higher_threshold = int(input("Define 'higher' price: "))

    if price >= higher_threshold:
        print("Choose Day Time Flight")
    else:
        print("Choose Red Eye Flight")

# This statement executes regardless of the time and price decisions
print("Arrive City B")

# How it works:
# The program starts by printing the first travel message.
# It then prompts for 'time' and a 'longer_threshold'.
# The first 'if time >= longer_threshold' acts as the main fork in the flowchart.
#   - If True, it follows the "longer time" path, asking for price and higher_threshold,
#     and then makes a decision between "Train" and "Coach".
#   - If False, it follows the "shorter time" path (the 'else' block), asking for price
#     and higher_threshold, and then makes a decision between "Day Time Flight" and "Red Eye Flight".
# Finally, after all conditional decisions are made, "Arrive City B" is printed,
# as it's outside all the conditional blocks and always executes.
```

---

## Summary and Important Tips

*   **Conditional statements (`if`, `else`, `elif`)** are fundamental for creating programs that can make decisions and respond differently to various inputs or situations.
*   **`input()` and `int()`:** Always remember that `input()` returns a string, so use `int()` (or `float()`) to convert user input to numbers when performing mathematical comparisons.
*   **Modulo Operator (`%`):** A powerful tool for checking divisibility and extracting last digits.
*   **Indentation is Key:** Python relies on indentation (usually 4 spaces) to define code blocks within `if`, `elif`, and `else` statements. Incorrect indentation will lead to errors.
*   **`if-else` vs. `if-elif-else`:**
    *   Use `if-else` for two possible outcomes.
    *   Use `if-elif-else` for multiple mutually exclusive outcomes, where only one condition can be true. This makes your code more readable and efficient.
*   **Nested `if` statements:** Use them when a condition depends on the outcome of a previous condition.
*   **Order of Conditions:** In `if-elif-else` chains, the order of conditions matters, especially when ranges overlap (e.g., checking for `marks >= 90` before `marks >= 80`).
*   **Comprehensive Testing:** Always test your code with a variety of inputs:
    *   **Typical values:** Expected inputs (e.g., a number ending in 0 or 5).
    *   **Edge cases:** Values at the boundaries of your conditions (e.g., 0, 100 for grades; 2 for even/odd).
    *   **Negative values:** If applicable (e.g., negative numbers for even/odd).
    *   **Invalid inputs:** Values outside the expected range (e.g., 110 or -5 for grades) to ensure proper error handling or "invalid input" messages.