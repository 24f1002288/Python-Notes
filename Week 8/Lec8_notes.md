Here are detailed notes on recursive binary search and recursion limits in Python, structured for clarity and easy understanding.

---

# Lecture Notes: Recursive Binary Search and Python's Recursion Limits

### **1. Recursive Binary Search**

*   **What is it?**
    *   Binary Search is an efficient way to find a specific element in a **sorted list**.
    *   The "recursive" part means the function solves a problem by calling itself with smaller versions of the same problem, until a very simple case is reached.
    *   It works by repeatedly dividing the search area in half.
*   **How it Works (The Big Picture)**
    *   Imagine you have a large sorted list and you're looking for a number (`k`).
    *   Instead of checking every number one by one, you look at the **middle** number.
    *   If the middle number is `k`, you've found it!
    *   If `k` is smaller than the middle number, you know `k` must be in the **left half** of the list. So, you discard the right half and repeat the process on the left half.
    *   If `k` is larger than the middle number, you know `k` must be in the **right half** of the list. So, you discard the left half and repeat the process on the right half.
    *   This "halving" continues until you find `k` or there are no numbers left to check.
*   **Key Parameters for the Recursive Function:**
    *   `L`: The sorted list where you want to search.
    *   `k`: The element you are trying to find.
    *   `begin`: The starting index of the current portion of the list we are searching.
    *   `end`: The ending index of the current portion of the list we are searching.
    *   Initially, `begin` would be `0` (the start of the list) and `end` would be `len(L) - 1` (the end of the list).

*   **Breaking Down the Recursion (Two Main Parts):**

    1.  **Trivial Cases (Base Cases - When to Stop Recursion):**
        *   These are the simple situations where the function knows the answer immediately without calling itself again.
        *   **Case A: Invalid Search Region (`end < begin`)**
            *   If, at any point, the `end` index becomes smaller than the `begin` index, it means our search range has become empty or invalid.
            *   This implies the element `k` is not in the list.
            *   **Action:** Return `0` (indicating "not found").
        *   **Case B: Element Found (`L[mid] == k`)**
            *   If the middle element of our current search region happens to be `k`.
            *   **Action:** Return `1` (indicating "found").

    2.  **Non-Trivial Case (Recursive Step - When to Keep Searching):**
        *   This happens when the search region is still large enough to be split further, and `k` hasn't been found yet.
        *   **Step 1: Calculate the Middle Index**
            *   `mid = (begin + end) // 2` (The `//` ensures we get a whole number for the index).
        *   **Step 2: Compare the Middle Element (`L[mid]`) with `k`**
            *   **If `L[mid] > k` (Target is in the Left Half):**
                *   Since the list is sorted, if the middle element is *larger* than `k`, then `k` must be in the portion of the list *before* `mid`.
                *   We can discard the right half (from `mid` to `end`).
                *   **Action:** Call the `r_binary_search` function again, but this time, the new search range will be `begin` to `mid - 1`.
            *   **If `L[mid] < k` (Target is in the Right Half):**
                *   If the middle element is *smaller* than `k`, then `k` must be in the portion of the list *after* `mid`.
                *   We can discard the left half (from `begin` to `mid`).
                *   **Action:** Call the `r_binary_search` function again, but this time, the new search range will be `mid + 1` to `end`.

*   **Analogy: Searching a Dictionary**
    *   Imagine looking up a word in a huge dictionary. You don't start from the first page.
    *   You open it roughly in the middle.
    *   Based on whether your word comes alphabetically *before* or *after* the words on that middle page, you quickly decide to ignore either the first half or the second half of the dictionary.
    *   You then repeat this process on the remaining half. This is exactly how recursive binary search efficiently finds your word!

*   **Code Example: Recursive Binary Search**

    ```python
    def r_binary_search(L, k, begin, end):
        # Base Case 1: Invalid search region (k not found)
        # If the 'end' index crosses below the 'begin' index, the element isn't there.
        if end < begin:
            return 0

        # Calculate the middle index of the current search range
        mid = (begin + end) // 2

        # Base Case 2: Element found at the middle
        if L[mid] == k:
            return 1
        # Recursive Step 1: k is in the left half
        # If the middle element is greater than k, k must be on the left side
        elif L[mid] > k:
            # Recursively search the left half (from 'begin' to 'mid - 1')
            return r_binary_search(L, k, begin, mid - 1)
        # Recursive Step 2: k is in the right half
        # If the middle element is less than k, k must be on the right side
        else: # L[mid] < k
            # Recursively search the right half (from 'mid + 1' to 'end')
            return r_binary_search(L, k, mid + 1, end)

    # --- How to Use It ---
    my_list = [1, 7, 10, 16, 100, 108, 1008]
    list_length = len(my_list) - 1 # 'end' is usually len(L) - 1 for 0-indexed lists

    # Searching for an element that exists
    print(f"Is 7 in the list? {r_binary_search(my_list, 7, 0, list_length)}") # Output: Is 7 in the list? 1
    # Searching for an element that does not exist
    print(f"Is 5 in the list? {r_binary_search(my_list, 5, 0, list_length)}") # Output: Is 5 in the list? 0

    # Example with a very large list to show efficiency
    huge_list = list(range(100_000_000)) # A list from 0 to 99,999,999
    huge_list_length = len(huge_list) - 1

    print(f"Is 1,000,000 in a 100 million element list? {r_binary_search(huge_list, 1_000_000, 0, huge_list_length)}") # Output: ...? 1
    print(f"Is 100,000,000 (not present) in a huge list? {r_binary_search(huge_list, 100_000_000, 0, huge_list_length)}") # Output: ...? 0
    ```
    *   **Explanation:** The `r_binary_search` function effectively cuts the problem size in half with each call. It keeps doing this until it finds `k` (returning `1`) or until the search area disappears (`end < begin`, returning `0`). This makes it incredibly fast, even for lists with millions of items.

---

### **2. Understanding Recursion Limits in Python**

*   **The Concept of Recursion Depth:**
    *   When a function calls itself, Python keeps track of each call on something called the "call stack." Each call adds a "frame" to this stack.
    *   If a function calls itself too many times without reaching a base case (a stopping point), this call stack can grow excessively large, using up all available memory. This is known as a **stack overflow**.
*   **Python's Safety Mechanism:**
    *   To prevent programs from crashing due to uncontrolled recursion, Python imposes a **default recursion depth limit**.
    *   This limit is typically **999** on most systems. It means a function can only call itself recursively about 999 times deep by default.
    *   If a recursive function tries to go beyond this limit, Python will stop it and raise a `RecursionError`.
*   **Why is this Limit Important?**
    *   **Resource Protection:** It prevents programs from hogging all your computer's memory.
    *   **Bug Detection:** It often helps programmers catch mistakes in their recursive code (like missing or incorrect base cases that would lead to infinite recursion).
*   **Why Recursive Binary Search Doesn't Hit the Limit:**
    *   Binary search is extremely efficient. For a list of 100 million elements, it only needs about 27 recursive calls to find an element (because it halves the problem size each time, `log₂(100,000,000)` is roughly 27).
    *   This number (27) is much smaller than Python's default limit of 999, so binary search works perfectly fine recursively.
*   **Can You Change the Limit?**
    *   Yes, it's possible to change Python's recursion limit using the `sys` module and `sys.setrecursionlimit()`.
    *   However, you **cannot** set it to an infinite value. You are always limited by your computer's physical memory. Increasing it too much for highly recursive functions can still lead to memory issues.

*   **Code Example: Exceeding the Recursion Limit**

    ```python
    # A simple recursive function to sum numbers from 1 to n
    def sum_recursive(n):
        if n == 0:
            return 0
        else:
            return n + sum_recursive(n - 1)

    print(f"Sum of 10: {sum_recursive(10)}") # Output: Sum of 10: 55
    print(f"Sum of 900: {sum_recursive(900)}") # Output: Sum of 900: 405450

    # This call will attempt to make 100,000 recursive calls.
    # It will likely exceed Python's default recursion limit (e.g., 999)
    # and cause a 'RecursionError'.
    # Uncomment the line below to see the error in action:
    # print(f"Sum of 100,000: {sum_recursive(100000)}")
    ```
    *   **Explanation:** The `sum_recursive(n)` function needs `n` separate function calls to complete its task. If `n` is 100,000, it tries to make 100,000 calls. Since this far exceeds the typical recursion limit of 999, Python intervenes and stops the program with a `RecursionError` to prevent a stack overflow.

---

### **3. Summary and Important Tips**

*   **Recursive Binary Search is Powerful:** It's an elegant and incredibly fast algorithm for searching sorted lists, leveraging the principle of "divide and conquer" through recursion.
*   **Recursion Needs Base Cases:** The most crucial part of any recursive function is defining its **base cases** – the conditions under which it stops calling itself. Without them, you'll likely encounter infinite recursion and Python's `RecursionError`.
*   **Python's Recursion Limit is a Safeguard:** Remember that Python has a default limit on how deep recursion can go (around 999 calls). This is a helpful feature to prevent programs from crashing due to runaway recursive functions.
*   **Practice is Key:** Understanding recursion can be tricky at first. Don't worry if you "stumble" a bit; it's a normal part of the learning process in programming. The best way to grasp it is to write the code yourself, trace its execution with small examples, and experiment with different inputs.

---