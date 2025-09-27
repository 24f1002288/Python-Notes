# Python Programming Notes: More on Dictionaries

## Key Topics

### 1. Introduction to Dictionaries

Dictionaries are a fundamental data structure in Python, used for storing collections of data. Unlike lists and tuples, which use numeric indices, dictionaries store data in **key-value pairs**.

*   **Syntax:** Dictionaries are defined using **curly brackets `{}`**.
    *   *Example:* `my_dict = {'name': 'Alice', 'age': 30}`
*   **Key-Value Pairs:** Each element in a dictionary consists of two parts:
    *   **Key:** A unique identifier, located on the left side of a colon `:`.
    *   **Value:** The data associated with the key, located on the right side of a colon `:`.
    *   Keys and values are separated by a colon, and multiple key-value pairs are separated by commas.
*   **Accessing Values:** You access a value in a dictionary by referring to its associated key.
    *   *Example:* `my_dict['name']` would return `'Alice'`.

**Important Rules for Keys and Values:**

*   **Keys must be unique:** No two keys in the same dictionary can be identical. If you try to add an existing key with a new value, the old value will be overwritten.
*   **Values can be duplicated:** Multiple keys can have the same value.

---

### 2. Rules for Dictionary Keys

Not all data types can be used as dictionary keys. Keys must be **immutable** and **hashable**.

*   **Allowed Data Types for Keys:**
    *   **Integers:** `1`, `100`
    *   **Floats:** `3.14`, `0.5`
    *   **Booleans:** `True`, `False`
    *   **Strings:** `'hello'`, `'Python'`
*   **Not Allowed Data Types for Keys (due to being mutable):**
    *   **Lists:** `[1, 2, 3]` (Lists can be changed after creation, making them unsuitable as stable identifiers.)
    *   **Other Dictionaries:** `{'a': 1}` (Dictionaries are also mutable.)
*   **Special Case: Tuples as Keys:**
    *   **Generally, yes:** Tuples themselves are immutable, so they *can* be used as keys.
    *   **However, no if they contain mutable elements:** If a tuple contains a list, another dictionary, or any other mutable object, then that tuple *cannot* be used as a dictionary key.
    *   **The "Hashable" Concept (Simplified):** A "hashable" object has a fixed value that doesn't change, allowing Python to quickly and consistently find it in memory. Immutable types (like numbers, strings, and pure tuples) are hashable. Mutable types (like lists and dictionaries) are not, because their content can change, which would break the hashing mechanism.

**Code Example: Valid and Invalid Keys**

```python
# --- Valid Keys ---
my_dict = {
    1: "Integer key",
    3.14: "Float key",
    True: "Boolean key",
    "name": "String key",
    (1, 2): "Tuple with immutable elements as key"
}

print("Dictionary with valid keys:", my_dict)
print("Accessing value with string key:", my_dict["name"])
print("Accessing value with tuple key:", my_dict[(1, 2)])

# --- Invalid Key Example ---
# A list cannot be a dictionary key because it is mutable.
# The following code would cause an error (TypeError).
try:
    invalid_dict = {
        [1, 2]: "This list cannot be a key" # This will raise an error!
    }
except TypeError as e:
    print(f"\nError encountered when using a list as a key: {e}")

# A tuple containing a mutable element (like a list) also cannot be a key.
try:
    invalid_tuple_key_dict = {
        (1, [2, 3]): "Tuple with mutable element as key" # This will also raise an error!
    }
except TypeError as e:
    print(f"Error encountered when using a tuple with a list as a key: {e}")
```

**How it works:**
The code demonstrates that integers, floats, booleans, strings, and tuples with only immutable elements can serve as dictionary keys. It also shows, using `try-except` blocks to handle expected `TypeError`s, why mutable types like lists, or tuples containing mutable types, cannot be used as keys. Python explicitly forbids this because it relies on keys being constant for efficient lookup.

---

### 3. Rules for Dictionary Values

In contrast to keys, there are **no restrictions** on what can be a dictionary value.

*   **Allowed Data Types for Values:**
    *   Integers, floats, Booleans, strings
    *   Lists
    *   Tuples
    *   Other Dictionaries
    *   Any other Python object

**Code Example: Diverse Values**

```python
diverse_dict = {
    'name': 'Bob',              # String
    'age': 25,                  # Integer
    'is_student': True,         # Boolean
    'grades': [90, 85, 92],     # List
    'address': ('123 Main St', 'Anytown', 'USA'), # Tuple
    'contact': {'email': 'bob@example.com', 'phone': '555-1234'}, # Another dictionary
    'hobbies': {'reading', 'hiking'} # Set (another collection type)
}

print("Dictionary with diverse values:")
for key, value in diverse_dict.items():
    print(f"  {key}: {value} (Type: {type(value).__name__})")

print("\nAccessing the list value:", diverse_dict['grades'])
print("Accessing a value within the nested dictionary:", diverse_dict['contact']['email'])
```

**How it works:**
This example demonstrates a dictionary where values are of various data types, including basic types, a list, a tuple, and even another dictionary. This highlights the flexibility of dictionary values. We can access nested values by chaining key lookups.

---

### 4. Mutability of Dictionaries and Its Implications

Dictionaries are **mutable** data structures, meaning their contents (values, and the addition/removal of key-value pairs) can be changed after the dictionary is created. This mutability has important consequences, especially when copying dictionaries or passing them to functions.

*   **Copying Dictionaries:**
    *   Simply assigning one dictionary to another (e.g., `dict2 = dict1`) does **not** create an independent copy. Instead, both variables will refer to the **same dictionary object** in memory.
    *   To create a truly independent copy, you must explicitly use the `.copy()` method.
*   **Passing Dictionaries to Functions:**
    *   When a dictionary is passed as an argument to a function, it is passed **by reference**. This means the function receives a reference to the original dictionary, not a separate copy.
    *   Any changes made to the dictionary inside the function will directly affect the original dictionary outside the function.

**Code Example: Mutability and Copying**

```python
original_dict = {'a': 1, 'b': 2}
print("Original dictionary:", original_dict)

# --- Shallow Copy (using .copy() method) ---
copied_dict = original_dict.copy()
print("Copied dictionary (using .copy()):", copied_dict)

# Modify the copied dictionary
copied_dict['b'] = 20
copied_dict['c'] = 30
print("Modified copied dictionary:", copied_dict)
print("Original dictionary (after modifying copy):", original_dict) # Original remains unchanged

# --- Assignment (not a true copy) ---
assigned_dict = original_dict # This just creates another reference to the same dictionary
print("\nAssigned dictionary (points to original):", assigned_dict)

# Modify the assigned dictionary
assigned_dict['a'] = 100
assigned_dict['d'] = 40
print("Modified assigned dictionary:", assigned_dict)
print("Original dictionary (after modifying assigned):", original_dict) # Original is also changed!

# --- Passing to a function ---
def modify_dict_in_function(d_arg):
    print("\nInside function - before modification:", d_arg)
    d_arg['new_key'] = 'new_value'
    d_arg['a'] = 999
    print("Inside function - after modification:", d_arg)

my_func_dict = {'a': 10, 'x': 20}
print("\nBefore function call:", my_func_dict)
modify_dict_in_function(my_func_dict)
print("After function call:", my_func_dict) # The original dictionary is changed!
```

**How it works:**
The example clearly shows the difference between using `d.copy()` and simple assignment (`=`). When `.copy()` is used, modifying the `copied_dict` does not affect `original_dict`. However, when `assigned_dict = original_dict` is used, changing `assigned_dict` *does* change `original_dict` because both variables point to the same dictionary object. The function example further illustrates this; modifying `d_arg` inside `modify_dict_in_function` directly alters `my_func_dict` outside, confirming dictionaries are passed by reference.

---

### 5. Iterating Over Dictionaries

You can loop through a dictionary to access its keys, values, or both.

*   **Iterating Over Keys (Default):**
    *   A simple `for` loop over a dictionary will iterate through its **keys**.
    *   You can then use these keys to retrieve their corresponding values.

**Code Example: Iterating Over Keys and Values**

```python
student_scores = {'Alice': 95, 'Bob': 88, 'Charlie': 92}

print("Iterating over keys:")
for student in student_scores: # By default, this iterates through keys
    print(f"  Student: {student}")

print("\nIterating over keys and accessing values:")
for student_name in student_scores:
    score = student_scores[student_name] # Access value using the key
    print(f"  {student_name}'s score: {score}")
```

**How it works:**
The first loop demonstrates that a `for` loop directly on a dictionary iterates through its keys. The second loop builds on this by using each `student_name` (key) to look up and print its corresponding `score` (value) from the `student_scores` dictionary.

---

### 6. Dictionary-Specific Methods

Python provides built-in methods to easily get views of a dictionary's keys, values, or key-value pairs.

*   **`.keys()` method:**
    *   Returns a **view object** that displays a list of all the keys in the dictionary.
    *   This view dynamically reflects changes to the dictionary.
*   **`.values()` method:**
    *   Returns a **view object** that displays a list of all the values in the dictionary.
    *   This view also dynamically reflects changes to the dictionary.
*   **`.items()` method:**
    *   Returns a **view object** that displays a list of **tuples**, where each tuple contains a `(key, value)` pair.
    *   This is a convenient way to iterate over both keys and values simultaneously.
    *   This method demonstrates another common internal use of tuples in Python.

**Code Example: Dictionary Methods**

```python
my_data = {'id': 101, 'product': 'Laptop', 'price': 1200}

print("Original Dictionary:", my_data)

# --- Using .keys() ---
all_keys = my_data.keys()
print("\nKeys (using .keys()):", all_keys)
print("Type of keys view:", type(all_keys))

# Iterating over keys view
print("Iterating through keys:")
for k in all_keys:
    print(f"  Key: {k}")

# --- Using .values() ---
all_values = my_data.values()
print("\nValues (using .values()):", all_values)
print("Type of values view:", type(all_values))

# Iterating over values view
print("Iterating through values:")
for v in all_values:
    print(f"  Value: {v}")

# --- Using .items() ---
all_items = my_data.items()
print("\nItems (using .items()):", all_items)
print("Type of items view:", type(all_items))

# Iterating over items view (unpacking tuples)
print("Iterating through items:")
for key, value in all_items: # Each item is a (key, value) tuple
    print(f"  Key: {key}, Value: {value}")
```

**How it works:**
The example demonstrates the use of `.keys()`, `.values()`, and `.items()` methods.
*   `.keys()` provides access to all keys.
*   `.values()` provides access to all values.
*   `.items()` provides access to both as a sequence of `(key, value)` tuples, which can be conveniently unpacked in a `for` loop. The output shows the type of these returned objects are `dict_keys`, `dict_values`, and `dict_items` respectively, which are dynamic "view objects" that reflect changes to the original dictionary.

---

## Summary and Important Tips

*   **Dictionaries** are powerful collections for storing data as **key-value pairs**, using **curly brackets `{}`**.
*   **Keys** must be **unique, immutable, and hashable** (e.g., numbers, strings, or tuples containing only immutable elements). This means lists and other dictionaries cannot be keys.
*   **Values** can be **any data type** and can be duplicated.
*   Dictionaries are **mutable**. Be mindful when copying them: use `dictionary.copy()` for independent copies, as simple assignment (`=`) creates a reference to the same dictionary. This also means changes to a dictionary inside a function will affect the original dictionary.
*   You can easily iterate over dictionary keys, values, or both using `for` loops or the specific methods:
    *   `dictionary.keys()`: Get all keys.
    *   `dictionary.values()`: Get all values.
    *   `dictionary.items()`: Get all key-value pairs as tuples.

Understanding these concepts is crucial for effectively using dictionaries in your Python programs.