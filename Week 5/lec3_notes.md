# Programming in Python: Sorting Using Functions

This document explores how to implement a sorting algorithm using the power of functions, moving from a single, complex block of code to a more organized, modular approach. We'll revisit a sorting technique called "Obvious Sort" (a simple form of Selection Sort) and transform it using functions to highlight the benefits of this programming style.

## Key Topics

### Understanding the "Obvious Sort" Algorithm

The "Obvious Sort" technique involves repeatedly finding the smallest element in a list, adding it to a new, empty list, and then removing it from the original list. This process continues until the original list is empty, at which point the new list contains all elements in sorted order.

Here's a breakdown of the steps:
1.  Start with an empty list, let's call it `sorted_list`.
2.  While the original list is not empty:
    *   Find the smallest (minimum) element in the original list.
    *   Add this minimum element to the `sorted_list`.
    *   Remove this minimum element from the original list.
3.  Once the original list is empty, `sorted_list` will contain all elements in ascending order.

#### Initial Attempt: A Single, Complex Block of Code

Initially, when trying to implement this, it's common to put all the logic into one large block of code. This can lead to some confusion and make the code harder to follow.

**Common Pain Points and Confusions During Initial Implementation:**

*   **Where to declare variables?** For example, the `sorted_list` (often named `x` in examples) needs to be initialized as an empty list *before* the main sorting loop begins.
*   **How to find the minimum element?** This typically involves looping through the list and keeping track of the smallest value found so far.
*   **How to remove the element?** After finding the minimum, you need to use the list's `remove()` method.
*   **How to repeat the process?** The entire process of finding, appending, and removing must be repeated until the original list is empty. This suggests a `while` loop.
*   **What to return?** A frequent mistake is to return the original list (which will be empty) instead of the newly created `sorted_list`.

**Code Example 1: Initial "Obvious Sort" (Monolithic Approach)**

```python
def obvious_sort(input_list):
    # Initialize an empty list to store the sorted elements
    sorted_elements = [] 
    
    # Keep looping as long as the input list has elements
    while len(input_list) > 0:
        # Assume the first element is the minimum initially
        # This assumes the input_list is not empty here, which is ensured by the while condition
        minimum_value = input_list[0] 
        
        # Find the actual minimum value in the current input_list
        for element in input_list:
            if element < minimum_value:
                minimum_value = element
        
        # Add the found minimum value to our sorted list
        sorted_elements.append(minimum_value)
        
        # Remove the minimum value from the original list so it's not found again
        input_list.remove(minimum_value)
        
    # IMPORTANT: Return the list that contains the sorted elements, not the original empty list.
    return sorted_elements

# Example usage:
my_list = [90, 23, 97, 88, 5, 1]
print(f"Original list: {my_list}") # Note: my_list will be modified and empty after sorting
sorted_list = obvious_sort(my_list)
print(f"Sorted list: {sorted_list}")
# What happens to my_list now? It's empty because elements were removed from it!
# print(f"Original list after sorting: {my_list}") 
```

**How it works:**
1.  `obvious_sort` takes `input_list` directly.
2.  `sorted_elements` starts empty.
3.  The `while` loop runs as long as `input_list` has items.
4.  Inside the `while` loop, another `for` loop finds the `minimum_value` in the *current* `input_list`.
5.  This `minimum_value` is `append`ed to `sorted_elements`.
6.  The `minimum_value` is `remove`d from `input_list`.
7.  The loop repeats until `input_list` is empty.
8.  Finally, `sorted_elements` is returned.

While this code successfully sorts the list, putting everything into one function can make it look "heavy on the mind" and harder to debug or modify later.

### The Power of Functions: A Modular Approach

A more effective way to solve complex problems in programming is to break them down into smaller, manageable pieces, each handled by its own function. This is known as **functional programming** or **modular programming**.

#### Step 1: Identifying a Reusable Task (Finding the Minimum)

Looking at the "Obvious Sort," one distinct and repeatable task is "finding the minimum element in a list." This is a perfect candidate for its own function. By isolating this logic, we make our code:

*   **Clearer:** Each function has a single, well-defined purpose.
*   **Easier to read:** The main sorting logic becomes simpler to understand.
*   **Reusable:** The `find_minimum` function could be used in other parts of a program, not just for sorting.
*   **Easier to debug:** If there's an issue with finding the minimum, you only need to look at that specific function.

**Code Example 2: The `find_minimum` Helper Function**

```python
def find_minimum(current_list):
    """
    Finds and returns the minimum element in a given list.
    Assumes the list is not empty.
    """
    if not current_list: # Handle empty list case (though sorting logic usually ensures it's not empty)
        return None 

    minimum_element = current_list[0] # Assume the first element is the minimum
    
    # Iterate through the rest of the list to find the true minimum
    for element in current_list:
        if element < minimum_element:
            minimum_element = element
            
    return minimum_element

# Example usage of find_minimum:
test_list = [50, 10, 80, 5, 100]
min_val = find_minimum(test_list)
print(f"The minimum value in {test_list} is: {min_val}") # Output: 5
```

**How it works:**
1.  `find_minimum` takes a `current_list` as input.
2.  It initializes `minimum_element` with the first element of the list.
3.  It then loops through the entire `current_list` to compare each `element` with `minimum_element`.
4.  If a smaller `element` is found, `minimum_element` is updated.
5.  Finally, it returns the `minimum_element` found.

#### Step 2: Rebuilding the Sort Using the Helper Function

Now that we have a dedicated function for finding the minimum, we can simplify our main sorting function. Instead of rewriting the minimum-finding logic every time, we simply *call* our `find_minimum` function.

**Code Example 3: The `obvious_sort_functional` Function (Modular Approach)**

```python
def obvious_sort_functional(original_list):
    """
    Sorts a list using the 'Obvious Sort' (Selection Sort) technique,
    utilizing a helper function to find the minimum element.
    """
    sorted_result = [] # Initialize the list to store sorted elements
    
    # Make a copy of the original list to avoid modifying it directly if desired
    # If you want to modify the original list, you can skip this line.
    # For this example, we will let it modify the original list to match the lecture.
    # working_list = list(original_list) 
    
    # Continue as long as there are elements in the list to be sorted
    while len(original_list) > 0: 
        # Find the minimum element using our dedicated helper function
        # This is the "climax" - we don't write the logic again!
        min_val = find_minimum(original_list) 
        
        # Add the found minimum to our results list
        sorted_result.append(min_val)
        
        # Remove the minimum from the original list so it's not considered again
        original_list.remove(min_val)
        
    # IMPORTANT: Return the list that has been built with sorted elements.
    return sorted_result

# Example usage:
my_unsorted_list = [90, 23, 97, 88, 5, 1]
print(f"Original list before sorting: {my_unsorted_list}")

# Call the sorting function. It will internally call find_minimum().
final_sorted_list = obvious_sort_functional(my_unsorted_list)
print(f"Sorted list (functional approach): {final_sorted_list}")
print(f"Original list after functional sort: {my_unsorted_list}") # It's empty!
```

**How it works:**
1.  `obvious_sort_functional` takes `original_list` as input.
2.  `sorted_result` starts empty.
3.  The `while` loop runs as long as `original_list` has items.
4.  Crucially, `min_val = find_minimum(original_list)` is called. This statement *delegates* the task of finding the minimum to another function.
5.  The returned `min_val` is `append`ed to `sorted_result`.
6.  `min_val` is `remove`d from `original_list`.
7.  The loop repeats.
8.  Finally, `sorted_result` is returned.

Notice how much cleaner and more direct `obvious_sort_functional` looks. The responsibility of finding the minimum is neatly encapsulated in `find_minimum`, making `obvious_sort_functional` easier to read and understand at a glance.

### Key Takeaways and Principles

The transformation of our sorting program illustrates a fundamental principle in programming:

*   **Functional Approach / Modular Programming:** This technique involves breaking down a large, complex problem into smaller, independent, and reusable sub-problems (modules or functions).
*   **Benefits of Modularity:**
    *   **Simplicity:** Each function focuses on a specific task, making it easier to write and understand.
    *   **Organization:** Code becomes structured and well-arranged, improving readability.
    *   **Reduced Mental Load:** You don't have to keep track of all the details at once. You can focus on one small piece at a time.
    *   **Reusability:** Functions written for specific tasks (like `find_minimum`) can be reused in other parts of the program or in entirely different programs.
    *   **Easier Debugging:** When an error occurs, you can often pinpoint which small function is causing the problem.
    *   **Collaboration:** Different programmers can work on different functions simultaneously.

This principle is not just for coding; it's a general problem-solving strategy. When faced with a big task, breaking it into smaller chunks makes it less daunting and more achievable.

## Summary

We revisited the "Obvious Sort" algorithm, first implementing it in a single, large function which, while functional, was complex to follow. We then refactored this solution by identifying a key sub-task ("finding the minimum element") and encapsulating it within its own function, `find_minimum`. By utilizing this helper function, the main sorting logic in `obvious_sort_functional` became significantly clearer, demonstrating the immense power and benefits of **modular programming** (or the **functional approach**). This approach involves breaking down problems into smaller, independent, and reusable functions, leading to more organized, understandable, and maintainable code.

## Important Tips

*   **Practice, Practice, Practice:** The best way to understand and internalize functional programming is to write code yourself. Try converting existing monolithic programs into a modular design.
*   **Identify Sub-Problems:** Whenever you're writing a piece of code, ask yourself: "Can any part of this be a standalone, reusable task?" If the answer is yes, consider making it a function.
*   **Keep Functions Focused:** Aim for functions that do one thing and do it well. This makes them easier to test, debug, and understand.
*   **Don't Be Afraid to Refactor:** It's okay to write a less-than-perfect solution first and then refine it into a more modular and elegant one. This is a common and valuable part of the programming process.