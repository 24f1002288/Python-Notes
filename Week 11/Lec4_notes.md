# Functional Programming in Python (Part 2)

This document explores advanced Python features that allow for more concise and expressive code, building on concepts like iterators and generators. The focus is on writing "inline" statements to condense multiple lines of code into a single one, improving brevity.

## 1. Inline `if-else` Statements (Ternary Operator)

Traditionally, `if-else` statements span multiple lines to conditionally assign a value to a variable. Python offers a way to write this entire logic in a single line, often referred to as a "ternary operator."

### Traditional `if-else` Structure:

```python
a = 10
b = 20
if a < b:
    small = a
else:
    small = b
print(small) # Output: 10
```

This code block assigns the smaller of `a` or `b` to the variable `small`.

### Inline `if-else` Syntax:

The same logic can be written in a single line using the following structure:

`variable = value_if_true if condition else value_if_false`

### How it Works:

The expression `value_if_true if condition else value_if_false` evaluates the `condition`.
*   If `condition` is `True`, `value_if_true` is chosen.
*   If `condition` is `False`, `value_if_false` is chosen.
The selected value is then assigned to `variable`.

### Code Example:

```python
a = 10
b = 20

# Inline if-else statement
small = a if a < b else b
print(small) # Output: 10

a = 100
b = 20
small = a if a < b else b
print(small) # Output: 20
```

**Explanation:**
*   In the first case (`a=10, b=20`), `a < b` (10 < 20) is `True`. So, `a` (which is 10) is assigned to `small`.
*   In the second case (`a=100, b=20`), `a < b` (100 < 20) is `False`. So, `b` (which is 20) is assigned to `small`.

### Advantages:

*   **Brevity:** Reduces the number of lines of code, making the program potentially shorter.
*   **Readability (for simple cases):** For straightforward conditional assignments, the single-line version can be more readable.

### Performance:

There is generally no significant performance difference between the multi-line `if-else` and its inline counterpart. The primary benefit is code conciseness.

## 2. Inline Loops

Similar to `if-else` statements, simple `while` and `for` loops can also be written in a single line. However, this practice is usually recommended only for very short and simple loop bodies due to potential readability issues.

### 2.1 Inline `while` Loops

A traditional `while` loop often involves a condition check and multiple statements inside its body. For very simple loops, these statements can be placed on a single line.

### Traditional `while` Loop Structure:

```python
a = 5
while a > 0:
    print(a)
    a = a - 1 # or a -= 1
# Output:
# 5
# 4
# 3
# 2
# 1
```

### Inline `while` Loop Syntax:

Statements within the loop body can be separated by semicolons (`;`) to put them on a single line.

`while condition: statement1; statement2; ...`

### Code Example:

```python
a = 5
while a > 0: print(a); a -= 1
# Output:
# 5
# 4
# 3
# 2
# 1
```

**Explanation:**
*   The `while a > 0:` condition is checked.
*   If true, `print(a)` executes, followed by `a -= 1`.
*   The loop continues until `a` is no longer greater than 0.

### Considerations:

*   **Readability:** While it reduces lines of code, for loops with many or complex statements, a single-line `while` loop can become very difficult to read and understand.
*   **Best Use:** Best suited for very small, self-contained loop bodies.

## 3. List Comprehension (Inline `for` Loops for List Creation)

While simple `for` loops can theoretically be inlined similar to `while` loops, Python provides a more elegant and powerful feature specifically for creating lists based on an existing iterable: **List Comprehension**. This is a powerful application of inline `for` loops, often combined with `if` conditions.

### The Problem: Filtering and Transforming a List

Consider a common task: iterating through a list, applying a condition to filter elements, and then transforming the filtered elements before adding them to a new list.

### Traditional Approach:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for fruit in fruits:
    if 'n' in fruit: # Filter: check for 'n' in the fruit name
        new_list.append(fruit.capitalize()) # Transform: capitalize and add to new list

print(new_list) # Output: ['Banana', 'Mango']
```

**Explanation:**
This code iterates through `fruits`. If a fruit's name contains the letter 'n', it's capitalized and added to `new_list`.

### List Comprehension Syntax:

`new_list = [expression for item in iterable if condition]`

### How it Works:

List comprehension creates a new list by:
1.  Iterating through each `item` in `iterable`.
2.  Optionally applying a `condition` to filter items.
3.  Applying an `expression` to the `item` (or filtered `item`) to determine what value is added to the new list.

### Reading Order (Important for Understanding):

1.  **`for item in iterable`**: Start by identifying what you are iterating over and what each item is called temporarily.
2.  **`if condition` (optional)**: Then, check if there's a filtering condition. If so, only items satisfying this condition will proceed.
3.  **`expression`**: Finally, apply the expression to the `item` (or filtered `item`) to produce the actual value that goes into the new list.

### Code Example (Recreating the above logic):

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# List comprehension:
new_list = [fruit.capitalize() for fruit in fruits if 'n' in fruit]

print(new_list) # Output: ['Banana', 'Mango']
```

**Explanation:**
*   `for fruit in fruits`: We iterate through each `fruit` in the `fruits` list.
*   `if 'n' in fruit`: This is our filter. Only fruits containing the letter 'n' will be considered.
*   `fruit.capitalize()`: For each `fruit` that passes the filter, this expression capitalizes its first letter.
*   The results of `fruit.capitalize()` are then collected into `new_list`.

### Addressing a Potential Syntax Error (as discussed in the lecture):

A common mistake when first learning list comprehension is to include a colon after the `if` condition, which is incorrect syntax.
Incorrect: `[fruit.capitalize() for fruit in fruits if 'n' in fruit:]` (The colon after `fruit` is wrong)
Correct: `[fruit.capitalize() for fruit in fruits if 'n' in fruit]`

### Advantages of List Comprehension:

*   **Conciseness:** Dramatically reduces the number of lines of code compared to traditional loops for list creation.
*   **Readability:** For many common list processing tasks (filtering, transforming), list comprehensions are often more readable and expressive than multi-line `for` loops. They clearly state *what* the new list contains rather than *how* it's built step-by-step.
*   **Efficiency:** List comprehensions are generally more efficient than traditional `for` loops for creating new lists, as they are optimized at a lower level in Python.

## Summary

This session introduced powerful Python features that enhance code conciseness:

*   **Inline `if-else` (Ternary Operator):** A single-line way to assign a value based on a condition (`value_if_true if condition else value_if_false`).
*   **Inline `while` Loops:** Condensing simple `while` loops by separating statements with semicolons. Best used sparingly for very short loop bodies.
*   **List Comprehension:** A highly efficient and readable way to create new lists by iterating, filtering (optional `if` condition), and transforming elements from an existing iterable. Syntax: `[expression for item in iterable if condition]`.

The main advantage of these "functional programming" approaches is **code brevity and improved readability** for specific use cases. They allow you to express operations more directly and succintly.

### Important Tips:

*   **Practice:** Try converting some of your previously written Python code that uses `if-else` blocks, `while` loops, or `for` loops for list creation into these inline or comprehension forms.
*   **Readability vs. Brevity:** While these features reduce line count, always prioritize code readability. Don't force complex logic into a single line if it makes the code harder to understand. List comprehensions are generally very readable for their intended purpose, while inline `while` loops can quickly become obscure.
*   **Functional Thinking:** Think about what you *want* to achieve with your data (e.g., filter a list, transform elements) rather than the step-by-step instructions, and these constructs will often fit naturally.