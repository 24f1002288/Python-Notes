# Data Types and Type Conversion

This document covers fundamental data types in programming, including a new type called Boolean, and explains how to convert data from one type to another.

## 1. Review of Basic Data Types

Before diving into new concepts, let's quickly recap the basic data types and how to check them. Each piece of data has a specific type that tells the computer what kind of value it is.

*   **Integers (`int`):** Whole numbers (e.g., 10, -5, 0).
*   **Floating-point numbers (`float`):** Numbers with decimal points (e.g., 5.6, -1.25, 3.0).
*   **Strings (`str`):** Sequences of characters, enclosed in single or double quotes (e.g., "India", 'Hello World').

### Checking a Variable's Type

You can find out the data type of any variable using the `type()` command.

**Code Example:**

```python
i = 10
f = 5.6
s = "India"

print(type(i)) # Output: <class 'int'>
print(type(f)) # Output: <class 'float'>
print(type(s)) # Output: <class 'str'>
```

## 2. Introducing the Boolean Data Type

The Boolean data type is a special type that can only hold one of two values: `True` or `False`. It's fundamental for making decisions in programs.

*   **Values:**
    *   `True`
    *   `False`
*   **Case Sensitivity:** It's crucial to remember that `True` and `False` must start with a **capital letter 'T' and 'F'** respectively. Using `true` or `false` (lowercase) will result in an error or be treated as a different kind of value.

**Code Example:**

```python
# Assigning Boolean values
b1 = True
b2 = False

# Printing the values and their types
print(b1)       # Output: True
print(b2)       # Output: False
print(type(b1)) # Output: <class 'bool'>
print(type(b2)) # Output: <class 'bool'>

# Incorrect capitalization will cause an error
# b3 = true # This would cause a NameError
```

## 3. Type Conversion (Type Casting)

Type conversion, also known as type casting, is the process of changing a value from one data type to another. This is often necessary when you need to perform operations that require specific data types or to store data in a particular format.

We use built-in functions like `int()`, `float()`, `str()`, and `bool()` to perform these conversions.

### 3.1. Converting to Integers (`int()`)

You can convert floats and strings to integers using the `int()` function.

*   **From Float to Integer:**
    *   When converting a floating-point number to an integer, the decimal part (the digits after the dot) is **truncated (cut off)**. The number is *not* rounded up or down; it simply discards the fractional part.
    *   **Pain Point:** Students often expect rounding. Remember, `int()` from float *always truncates*.
*   **From String to Integer:**
    *   A string can be converted to an integer if it contains a valid representation of a whole number (e.g., "10", "-5").
    *   **Pain Point:** If the string contains non-digit characters (like "5.7" or "hello") or is an empty string, it will result in a `ValueError`.

**Code Example:**

```python
# Converting from float to integer
a = int(5.7)  # 5.7 is a float
print(a)      # Output: 5
print(type(a))# Output: <class 'int'>
# Explanation: The .7 part is simply ignored.

# Converting from string to integer
b = int("10") # "10" is a string
print(b)      # Output: 10
print(type(b))# Output: <class 'int'>
# Explanation: The string representation of 10 is converted to the integer 10.

# Example of a common error (ValueError)
# c = int("5.7") # This would cause a ValueError because "5.7" is not a pure integer string.
# d = int("hello") # This would also cause a ValueError.
```

### 3.2. Converting to Floats (`float()`)

You can convert integers and strings to floats using the `float()` function.

*   **From Integer to Float:**
    *   An integer is converted to a float by adding a `.0` decimal part (e.g., `9` becomes `9.0`).
*   **From String to Float:**
    *   A string can be converted to a float if it contains a valid representation of a number, including decimals (e.g., "5.3", "-10", "3.14").
    *   **Pain Point:** Similar to `int()`, if the string cannot be interpreted as a number (e.g., "hello"), it will raise a `ValueError`.

**Code Example:**

```python
# Converting from integer to float
x = float(9)  # 9 is an integer
print(x)      # Output: 9.0
print(type(x))# Output: <class 'float'>
# Explanation: The integer 9 gains a decimal part to become a float.

# Converting from string to float
y = float("5.3") # "5.3" is a string
print(y)      # Output: 5.3
print(type(y))# Output: <class 'float'>
# Explanation: The string "5.3" is interpreted as the floating-point number 5.3.

z = float("-10") # Even an integer-like string can become a float
print(z)      # Output: -10.0
print(type(z))# Output: <class 'float'>
```

### 3.3. Converting to Strings (`str()`)

You can convert integers and floats to strings using the `str()` function.

*   **From Integer to String:**
    *   The numeric value of the integer is converted into its textual representation.
*   **From Float to String:**
    *   The numeric value of the float is converted into its textual representation, including the decimal point.

**Code Example:**

```python
# Converting from integer to string
s_int = str(9)  # 9 is an integer
print(s_int)      # Output: 9
print(type(s_int))# Output: <class 'str'>
# Explanation: The number 9 is now treated as the character '9'.

# Converting from float to string
s_float = str(5.3) # 5.3 is a float
print(s_float)      # Output: 5.3
print(type(s_float))# Output: <class 'str'>
# Explanation: The number 5.3 is now treated as the sequence of characters '5', '.', '3'.
```

### 3.4. Converting to Booleans (`bool()`)

Converting other data types to Boolean (`bool()`) follows specific rules, especially concerning what is considered "truthy" (`True`) and "falsy" (`False`).

*   **From Integer to Boolean:**
    *   **`0` (zero) is converted to `False`.**
    *   **Any non-zero integer** (positive or negative) is converted to `True`.
    *   **Pain Point:** A negative number like `-10` is still considered `True`. Only `0` is `False`.

**Code Example (Integer to Boolean):**

```python
b_int_1 = bool(10)  # 10 is a non-zero integer
b_int_0 = bool(0)   # 0 is zero
b_int_neg = bool(-10) # -10 is a non-zero integer

print(b_int_1)      # Output: True
print(b_int_0)      # Output: False
print(b_int_neg)    # Output: True

print(type(b_int_1))# Output: <class 'bool'>
print(type(b_int_0))# Output: <class 'bool'>
print(type(b_int_neg))# Output: <class 'bool'>
```

*   **From Float to Boolean:**
    *   **`0.0` (zero with a decimal) is converted to `False`.**
    *   **Any non-zero float** (positive or negative) is converted to `True`.
    *   **Pain Point:** `0.0` and `0` behave the same way; they both evaluate to `False`.

**Code Example (Float to Boolean):**

```python
b_float_1 = bool(10.0)    # 10.0 is a non-zero float
b_float_0 = bool(0.0)     # 0.0 is zero
b_float_neg = bool(-10.4) # -10.4 is a non-zero float

print(b_float_1)      # Output: True
print(b_float_0)      # Output: False
print(b_float_neg)    # Output: True

print(type(b_float_1))# Output: <class 'bool'>
print(type(b_float_0))# Output: <class 'bool'>
print(type(b_float_neg))# Output: <class 'bool'>
```

*   **From String to Boolean:**
    *   **Any non-empty string** is converted to `True`. This includes strings containing numbers, spaces, or any characters.
    *   **Only an empty string (`""` or `''`) is converted to `False`.**
    *   **Pain Point:** This is a common point of confusion. The string `"0"` (which contains the character '0') is considered `True`, because it's *not* an empty string. This is different from the integer `0`, which is `False`. Similarly, a string containing only spaces `" "` is `True` because it's not empty.

**Code Example (String to Boolean):**

```python
b_str_word = bool("India")    # Non-empty string
b_str_num = bool("10")        # Non-empty string (even if it looks like a number)
b_str_zero_char = bool("0")   # Non-empty string (contains the character '0')
b_str_neg_float = bool("-10.4") # Non-empty string

print(b_str_word)       # Output: True
print(b_str_num)        # Output: True
print(b_str_zero_char)  # Output: True
print(b_str_neg_float)  # Output: True
print("-" * 20)

# The ONLY string that converts to False: an empty string
b_str_empty = bool("")    # Empty string (no characters between the quotes)
print(b_str_empty)      # Output: False
print(type(b_str_empty))# Output: <class 'bool'>
```

## Summary and Important Tips

### Key Takeaways:

*   **Boolean Type:** Introduced `True` and `False` as the only two values for the `bool` data type. Remember their capitalization.
*   **Type Conversion:** The ability to change a value's data type using functions like `int()`, `float()`, `str()`, and `bool()`. This is crucial for data manipulation.
*   **`int()` Conversion:** Truncates (chops off) the decimal part from floats. Strings must be pure integer representations.
*   **`float()` Conversion:** Adds `.0` to integers. Strings can represent whole numbers or decimals.
*   **`str()` Conversion:** Converts any data type into its textual representation.
*   **`bool()` Conversion Rules (Crucial!):**
    *   **`False` values:** `0`, `0.0`, and the `""` (empty string).
    *   **`True` values:** Any non-zero integer, any non-zero float, and any non-empty string.

### Important Tips:

*   **Watch for `ValueError`:** When converting strings to numbers (`int()` or `float()`), make sure the string can actually be interpreted as a number. If not, your program will crash with a `ValueError`.
*   **Truncation vs. Rounding:** Remember that `int(float_value)` *always truncates*, it does not round. So, `int(5.9)` is `5`, not `6`.
*   **String `"0"` vs. Integer `0`:** This is the most common point of confusion with `bool()`. The string `"0"` is `True` (because it's not empty), while the integer `0` is `False`. Always be mindful of the data type when evaluating truthiness.
*   **Capitalization for Booleans:** `True` and `False` are specific keywords; `true` and `false` are not and will cause errors.