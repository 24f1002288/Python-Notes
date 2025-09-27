# Object-Oriented Programming in Python: Understanding Attributes and Methods

This set of notes delves into the core concepts of Object-Oriented Programming (OOP) in Python, focusing on how to structure classes effectively, manage data (attributes), and define actions (methods) for your objects.

---

## 1. Refining Our Object-Oriented Program Structure

Initially, programs might be written in a way that creates objects but doesn't fully leverage the power of OOP. A key area for improvement is to properly define both the *data* (attributes) and the *actions* (behavior or methods) that objects will possess.

The goal is to transition from simply having data associated with objects to having objects that are self-contained, with their own data and specific ways of interacting with that data.

---

## 2. The `__init__` Method: Object Initialization

In OOP, when you create a new object from a class blueprint, you often need to set up its initial state. This is handled by a special method called `__init__`.

### What is `__init__`?
*   It's a special method (also known as a **constructor**) that Python automatically calls whenever you create a new object (an "instance") of a class.
*   Its purpose is to initialize the object's attributes with starting values.
*   You **never call `__init__` directly**. Python handles its execution behind the scenes when you create an object.

### Syntax and Parameters
The `__init__` method follows a specific naming convention: two underscores, `init`, and then two more underscores (`__init__`). It always takes `self` as its first parameter, followed by any other parameters needed to set up the object.

```python
class Student:
    def __init__(self, roll_number, name): # self, roll_number, and name are parameters
        # Code here to initialize the student object
        pass

# Creating a new Student object (this implicitly calls __init__)
s0 = Student(0, "Bhuvanesh")
```

When you write `s0 = Student(0, "Bhuvanesh")`, Python performs these steps:
1.  Creates an empty `Student` object.
2.  Calls the `__init__` method of the `Student` class, passing the newly created object as the `self` argument, and `0` and `"Bhuvanesh"` as the `roll_number` and `name` arguments respectively.
3.  The `__init__` method then uses these values to set up the object's internal state.

---

## 3. Understanding the `self` Keyword

The `self` keyword is crucial in Python's OOP. It's a fundamental concept for managing data within objects.

### What is `self`?
*   `self` is a reference to the **current object** (the instance of the class) that a method is being called on.
*   It allows methods to access and modify the attributes and other methods of that *specific* object.
*   It must be the **first parameter** in the definition of any method inside a class. However, when you call a method, you don't explicitly pass `self`; Python automatically provides the object itself as this argument.

### Why is `self` necessary?
Imagine you have multiple `Student` objects, say `s0` and `s1`. Both `s0` and `s1` have `roll_number` and `name` attributes. How does Python know if you're referring to `s0`'s `roll_number` or `s1`'s `roll_number`? This is where `self` comes in.

When a method is called (e.g., `s0.display()`), `self` inside that method automatically becomes `s0`. If `s1.display()` is called, `self` becomes `s1`.

### How `self` works with `__init__`

```python
class Student:
    def __init__(self, roll_number, name):
        # These are object attributes, unique to each Student object
        self.roll_number = roll_number  
        self.name = name

# Creating objects
s0 = Student(0, "Bhuvanesh")
s1 = Student(1, "Harish")

# When s0 = Student(0, "Bhuvanesh") is executed:
# Inside __init__, 'self' refers to the object 's0'.
# So, it sets s0.roll_number = 0 and s0.name = "Bhuvanesh".

# When s1 = Student(1, "Harish") is executed:
# Inside __init__, 'self' refers to the object 's1'.
# So, it sets s1.roll_number = 1 and s1.name = "Harish".
```
This ensures that each object (`s0`, `s1`, etc.) gets its own independent copies of `roll_number` and `name`.

---

## 4. Distinguishing Between Method Parameters and Object Attributes

A common point of confusion arises with lines like `self.roll_number = roll_number` within the `__init__` method.

*   **`self.roll_number` (Left Side):** This refers to an **object attribute**. It's a variable that *belongs to the specific object* (`s0`, `s1`, etc.) being created. Each object will have its own `roll_number` stored internally.
*   **`roll_number` (Right Side):** This refers to the **parameter** passed to the `__init__` method. It's a temporary variable that holds the value provided when the object is created (e.g., `0` for `s0`, `1` for `s1`). This parameter only exists within the scope of the `__init__` method.

The line `self.roll_number = roll_number` means: "Take the value from the `roll_number` parameter and assign it to the `roll_number` attribute of *this* object."

To make this distinction clearer, you can use different names for the parameters:

```python
class Student:
    def __init__(self, initial_roll, student_name): # 'initial_roll' and 'student_name' are parameters
        self.roll_number = initial_roll             # 'self.roll_number' is an object attribute
        self.name = student_name                    # 'self.name' is an object attribute
```
Both versions achieve the same result, but using distinct names for parameters can sometimes improve readability and prevent confusion.

---

## 5. Class Attributes vs. Object (Instance) Attributes

Variables in a class can behave in two main ways, leading to "class attributes" and "object attributes."

### Object (Instance) Attributes
*   **Definition:** These are defined *inside a method* (typically `__init__`) using the `self` keyword (e.g., `self.attribute_name`).
*   **Ownership:** Each object created from the class gets its **own separate copy** of these attributes.
*   **Purpose:** To store data that is unique to each individual object.
*   **Examples:** `roll_number`, `name`, `total_score` for each specific `Student` object.

### Class Attributes
*   **Definition:** These are defined directly *inside the class* but *outside any method*.
*   **Ownership:** There is **only one copy** of a class attribute, which is shared by *all* objects of that class. It "belongs" to the class itself, not to individual objects.
*   **Purpose:** To store data that is common to all instances of the class, or to track class-wide information (e.g., a counter for how many objects have been created).
*   **Access:** Accessed using the class name (e.g., `ClassName.attribute_name`). While you *can* access them via `object.attribute_name`, it's best practice to use `ClassName.attribute_name` to emphasize it's a class attribute.

### Code Example: Class Attribute `total_students`

```python
class Student:
    total_students = 0  # This is a CLASS ATTRIBUTE

    def __init__(self, roll_number, name, total_score):
        self.roll_number = roll_number      # Object attribute
        self.name = name                    # Object attribute
        self.total_score = total_score      # Object attribute
        Student.total_students += 1         # Increment the class attribute

    def display(self):
        print(f"Roll No: {self.roll_number}, Name: {self.name}, Score: {self.total_score}")

# Creating student objects
s0 = Student(0, "Bhuvanesh", 100)
s1 = Student(1, "Harish", 150)
s2 = Student(2, "Alice", 110)

# Accessing the class attribute
print(f"Total students created: {Student.total_students}")
# Output: Total students created: 3

# If we tried to access s0.total_students, it would still give 3,
# but it's less clear that it's a shared attribute.
```
In this example, `total_students` is a single variable, and every `Student` object shares and contributes to its value. `roll_number`, `name`, and `total_score` are unique for each student.

---

## 6. Adding Behavior with Methods

Beyond simply storing data, objects can also perform actions. These actions are defined by **methods** within the class. While `__init__` and a basic `display` method are useful, true object behavior often involves more complex operations.

### Example: Determining a Student's Exam Result

Let's enhance our `Student` class to include a `check_result` method that determines if a student passed or failed based on their `total_score`.

```python
class Student:
    def __init__(self, roll_number, name, total_score):
        self.roll_number = roll_number
        self.name = name
        self.total_score = total_score

    def display(self):
        print(f"Roll No: {self.roll_number}, Name: {self.name}, Score: {self.total_score}")

    def check_result(self): # This method defines a behavior for a Student object
        if self.total_score > 120:
            print("Pass")
        else:
            print("Fail")

# Create student objects with their scores
s0 = Student(0, "Bhuvanesh", 100)
s1 = Student(1, "Harish", 150)

# Display student info
s0.display()
s0.check_result() # Call the behavior method for s0

s1.display()
s1.check_result() # Call the behavior method for s1
```

**Output:**
```
Roll No: 0, Name: Bhuvanesh, Score: 100
Fail
Roll No: 1, Name: Harish, Score: 150
Pass
```
Here, `check_result()` is a method that encapsulates a specific behavior unique to a `Student` object. It uses the object's own `total_score` attribute to make a decision, demonstrating that behavior is tied directly to the object's data.

---

## 7. Functions vs. Methods: A Clarification

In Python, the terms "function" and "method" are often used interchangeably, but there's a technical distinction in OOP.

*   **Function:** A block of organized, reusable code that performs a single, related action. It is defined *outside* of any class.
    *   **Example:** `len("hello")`, `print("message")` are examples of built-in functions.
*   **Method:** A function that is defined *inside a class*. It "belongs" to that class and its objects. Methods operate on the data (attributes) of the object they are called on and require `self` as their first parameter.
    *   **Examples:** `__init__`, `display`, `check_result` are methods of the `Student` class. Also, `my_string.upper()` is a method of string objects, and `my_list.append(item)` is a method of list objects.

Understanding this distinction helps in using the correct terminology and appreciating how code is structured in an object-oriented way.

---

## Summary and Important Tips

### Key Takeaways:
*   **`__init__` Method:** This is the special "constructor" method that initializes a new object. Python calls it automatically when an object is created.
*   **`self` Keyword:** This refers to the current object and is essential for methods to access an object's unique attributes and other methods. It's always the first parameter in a method definition.
*   **Object Attributes:** Defined using `self.attribute_name` (usually in `__init__`). Each object gets its own copy.
*   **Class Attributes:** Defined directly in the class, outside any method. All objects share a single copy, accessed via `ClassName.attribute_name`.
*   **Methods:** Functions defined inside a class that encapsulate an object's behavior and operate on its data.
*   **Functions vs. Methods:** Methods are functions that belong to a class.

### Important Tips:
*   **Clarity with `self`:** Always remember `self` is how an object refers to itself from within its methods.
*   **Meaningful Names:** Use descriptive names for your classes, attributes, and methods to make your code easy to understand.
*   **Encapsulation:** OOP promotes bundling data (attributes) and the methods that operate on that data together within an object, leading to more organized and maintainable code.
*   **Start Simple:** Don't try to make your first OOP programs overly complex. Master these foundational concepts first.

---

## Exercise: Exploring Built-in Types as Classes

Python is thoroughly object-oriented. Even basic data types you've used since the beginning are actually objects of specific classes.

Consider the following code:

```python
x = 10
y = "hello"
z = [1, 2, 3]
d = {"a": 1, "b": 2}

print(type(x))
print(type(y))
print(type(z))
print(type(d))
```

**Your Task:**
1.  **Run this code** and observe the output.
2.  **Explain what `int`, `str`, `list`, and `dict` represent** in the context of Object-Oriented Programming, based on the output.
3.  **Explain why the output always says `class '...'`** for each type.

*(Hint: Relate this back to the concepts of classes and objects you've just learned.)*