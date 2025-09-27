# Python Programming: Understanding Nested Loops

This document explores the concept of nested loops in Python, demonstrating how to use them effectively to solve various programming problems. We will cover all possible combinations of `for` and `while` loops nested within each other.

## Key Topics

### Introduction to Nested Loops

Nested loops occur when one loop is placed inside another. The "inner" loop completes all its iterations for each single iteration of the "outer" loop. This powerful technique allows for complex patterns of repetition and data processing.

*   **Types of Nested Loops:**
    *   `for` loop inside another `for` loop.
    *   `while` loop inside another `while` loop.
    *   `for` loop inside a `while` loop.
    *   `while` loop inside a `for` loop.

### Nested `for` Loops: Finding Prime Numbers

This section demonstrates how to use a `for` loop nested inside another `for` loop to find prime numbers within a given range.

*   **Problem Statement:** Write a program that takes an integer `num` as input and prints all prime numbers strictly less than `num`.
*   **Expected Behavior:**
    *   Input: `9` -> Output: `2 3 5 7`
    *   Input: `15` -> Output: `2 3 5 7 11 13`
    *   Input: `3` -> Output: `2`
    *   Input: `2` -> Output: (no output, as no prime number is less than 2)
    *   Input: `1` -> Output: (no output)
*   **Logic Breakdown:**
    1.  **Input:** Get the target number from the user.
    2.  **Special Case for 2:** The number `2` is the only even prime number. If the input number is greater than `2`, `2` should be printed immediately.
    3.  **Outer Loop (`for i`):** This loop iterates through all numbers from `3` up to (but not including) the input `num`. Each `i` represents a number that we need to check for primality.
    4.  **Inner Loop (`for j`):** For each `i` from the outer loop, this inner loop iterates from `2` up to (but not including) `i`. Its purpose is to check if `i` is divisible by any number `j` in this range.
    5.  **Primality Check:**
        *   A `flag` variable (e.g., `is_prime`) is used to track if the current number `i` is prime. It's initially assumed `True` at the start of each outer loop iteration.
        *   If `i` is found to be divisible by `j` (i.e., `i % j == 0`), then `i` is not prime. The `is_prime` flag is set to `False`, and the `break` statement is used to immediately exit the *inner* `for` loop. There's no need to check further divisors for `i` once one is found.
    6.  **Printing Prime Numbers:** After the inner loop completes (either by checking all divisors or by breaking early), if `is_prime` is still `True`, it means `i` has no divisors other than 1 and itself, so it's a prime number and should be printed.
    7.  **Printing on the Same Line:** The `end=' '` argument in the `print()` function is used to prevent a newline character after each number, making them print on the same line separated by a space.

*   **Common Point of Confusion / Correction:**
    *   **Initial Thought:** An `if num >= 2:` condition might seem logical to print `2`.
    *   **The Nuance:** The problem statement specifies "prime numbers *less than* the entered number." If `num` is `2`, there are no prime numbers less than `2`. So, `2` should not be printed.
    *   **Correct Condition:** The initial check for printing `2` should be `if num > 2:`.

*   **Code Example: Finding Prime Numbers**

    ```python
    num = int(input("Enter a number: "))
    
    # Corrected special handling for prime number 2
    if num > 2:  # Only print 2 if the entered number is strictly greater than 2
        print(2, end=' ')
    
    # Outer loop: Iterate through numbers from 3 up to (num - 1)
    for i in range(3, num):
        is_prime = True  # Assume current number 'i' is prime
        # Inner loop: Check for divisibility from 2 up to (i - 1)
        for j in range(2, i):
            if i % j == 0:
                is_prime = False  # If divisible, it's not prime
                break             # No need to check further, exit inner loop
        
        if is_prime:
            print(i, end=' ')
    print() # Print a newline at the end for clean output
    ```

    **How it Works:**
    1.  The program first gets `num` from the user.
    2.  It checks `if num > 2`. If `num` is `3`, it prints `2`. If `num` is `2` or `1`, this condition is `False`, and `2` is not printed, which aligns with the "less than" requirement.
    3.  The outer `for i` loop starts from `3`. If `num` is `3`, `range(3,3)` is empty, so the loop doesn't run, and only `2` (if `num > 2`) is printed.
    4.  For each `i`, `is_prime` is reset to `True`.
    5.  The inner `for j` loop attempts to find any divisor for `i`.
    6.  If `i % j == 0`, it means `i` is divisible by `j` and thus not prime. `is_prime` becomes `False`, and `break` stops the inner loop for the current `i`.
    7.  After the inner loop, if `is_prime` is still `True`, `i` is printed.

### Nested `while` Loops: Trader Profit/Loss Calculation

This scenario illustrates the use of a `while` loop inside another `while` loop, which is ideal when the number of iterations for both the outer and inner processes is unknown beforehand.

*   **Problem Statement:** Calculate the total profit or loss for each trader. The number of traders is unknown, and for each trader, the number of transactions is also unknown.
*   **Input/Output Flow:**
    1.  Enter `Employee ID` (e.g., `SJ323`).
    2.  Enter `Trade Value` (e.g., `1000`, `-500`).
    3.  Continue entering `Trade Value` until `0` is entered (signals end of transactions for current trader).
    4.  Print the total `Profit/Loss` for that `Employee ID`.
    5.  Prompt for the next `Employee ID`.
    6.  The program stops when `Employee ID` is entered as `-1`.
*   **Why `while` loops are suitable:** Both the number of traders and the number of transactions per trader are not fixed and are determined by specific termination conditions (`-1` for traders, `0` for transactions).

*   **Logic Breakdown:**
    1.  **Outer `while` Loop (for traders):** This loop continues as long as the entered `employee_id` is not `-1`.
    2.  **Inner `while` Loop (for transactions):** Inside the outer loop, for each trader, this loop continues as long as the entered `trade_amount` is not `0`.
    3.  **Initialization:** For each new trader (at the beginning of the outer loop, before the inner loop starts), a `profit_loss` variable is initialized to `0` to accumulate their transactions.
    4.  **Accumulation:** Within the inner loop, each `trade_amount` is added to `profit_loss`.
    5.  **Termination:**
        *   The inner loop terminates when `trade_amount` becomes `0`.
        *   The outer loop terminates when `employee_id` becomes `-1`.
    6.  **Output:** After the inner loop completes for a trader, the total `profit_loss` for that `employee_id` is printed using formatted string literals.

*   **Code Example: Trader Profit/Loss**

    ```python
    print("Enter Employee ID (or -1 to stop):")
    employee_id = input()
    
    # Outer while loop: Continues as long as the employee_id is not '-1'
    while employee_id != "-1":
        profit_loss = 0  # Initialize profit/loss for the current employee
        print(f"Enter trade values for {employee_id} (0 to stop):")
        
        trade_amount_str = input()
        # Handle potential non-integer input for trade_amount initially
        try:
            trade_amount = int(trade_amount_str)
        except ValueError:
            print("Invalid trade amount. Please enter an integer.")
            trade_amount = 1 # Keep loop going or handle as desired
        
        # Inner while loop: Continues as long as the trade_amount is not 0
        while trade_amount != 0:
            profit_loss += trade_amount
            trade_amount_str = input()
            try:
                trade_amount = int(trade_amount_str)
            except ValueError:
                print("Invalid trade amount. Please enter an integer.")
                trade_amount = 1 # Keep loop going or handle as desired
        
        print(f"Employee {employee_id} Total Profit/Loss: {profit_loss}")
        print("\nEnter next Employee ID (or -1 to stop):")
        employee_id = input()
    
    print("Program terminated.")
    ```

    **How it Works:**
    1.  The program first prompts for an `employee_id`.
    2.  The outer `while` loop checks if this `employee_id` is `"-1"`. If not, it proceeds.
    3.  Inside the outer loop, `profit_loss` is reset to `0` for the current trader.
    4.  It then prompts for the first `trade_amount`.
    5.  The inner `while` loop checks if this `trade_amount` is `0`. If not, it adds it to `profit_loss` and prompts for the next `trade_amount` for the *same* trader. This continues until `0` is entered for `trade_amount`.
    6.  Once `0` is entered, the inner loop finishes, and the total `profit_loss` for that `employee_id` is printed.
    7.  Then, the program prompts for the `employee_id` of the next trader, which is then evaluated by the outer `while` loop's condition.

### Nested `while` inside `for` Loops: Daily Rainfall Calculation

This combination is useful when a task needs to be repeated a fixed number of times (outer `for` loop), but the number of sub-tasks within each iteration is variable (inner `while` loop).

*   **Problem Statement:** Calculate the total rainfall for a specific number of days. For each day, the user enters rainfall values until a `-1` is entered, signifying the end of entries for that day.
*   **Example Scenario:**
    *   Input `Number of days`: `7`
    *   For Day 1: Enter `10`, `15`, `19`, `5`, then `-1` -> Total: `49`
    *   For Day 5: Enter `-1` -> Total: `0` (no rainfall recorded)
*   **Why this combination:**
    *   **Outer `for` loop:** The number of days is fixed (e.g., `7`), making `for` a suitable choice for iterating through each day.
    *   **Inner `while` loop:** The number of rainfall entries for each day is unknown and ends with a sentinel value (`-1`), making `while` a suitable choice.

*   **Logic Breakdown:**
    1.  **Input Number of Days:** Get `num_days` from the user.
    2.  **Outer `for` Loop (`for day`):** This loop iterates from `1` to `num_days`. The `range(1, num_days + 1)` is used to make the days 1-indexed (e.g., Day 1, Day 2).
    3.  **Initialization:** For each new day, `total_rainfall` is initialized to `0`.
    4.  **First Rainfall Input:** Prompt for the first `rainfall_value` for the current `day`.
    5.  **Inner `while` Loop (for rainfall entries):** This loop continues as long as `rainfall_value` is not `-1`.
    6.  **Accumulation:** Inside the inner loop, each `rainfall_value` is added to `total_rainfall`.
    7.  **Next Rainfall Input:** Prompt for the next `rainfall_value` for the *same* day.
    8.  **Output:** Once `-1` is entered, the inner `while` loop terminates, and the `total_rainfall` for the current `day` is printed.

*   **Code Example: Daily Rainfall**

    ```python
    num_days = int(input("Enter the number of days: "))
    
    # Outer for loop: Iterates for each day
    # range(1, num_days + 1) makes days 1-indexed (Day 1, Day 2, ..., Day num_days)
    for day_num in range(1, num_days + 1):
        total_rainfall = 0  # Initialize total rainfall for the current day
        print(f"Enter rainfall values for Day {day_num} (-1 to stop):")
        
        rainfall_value_str = input()
        try:
            rainfall_value = int(rainfall_value_str)
        except ValueError:
            print("Invalid input. Assuming 0 and stopping for this day.")
            rainfall_value = -1 # Treat as end of input for the day
        
        # Inner while loop: Continues as long as the rainfall value is not -1
        while rainfall_value != -1:
            total_rainfall += rainfall_value
            rainfall_value_str = input()
            try:
                rainfall_value = int(rainfall_value_str)
            except ValueError:
                print("Invalid input. Assuming 0 and stopping for this day.")
                rainfall_value = -1 # Treat as end of input for the day
        
        print(f"Total rainfall for Day {day_num}: {total_rainfall}")
    ```

    **How it Works:**
    1.  The program takes `num_days` as input (e.g., `7`).
    2.  The outer `for` loop starts, setting `day_num` to `1`.
    3.  `total_rainfall` for `Day 1` is set to `0`.
    4.  The program prompts for the first `rainfall_value` for `Day 1`.
    5.  The inner `while` loop begins. If `rainfall_value` is not `-1`, it's added to `total_rainfall`, and the next `rainfall_value` for `Day 1` is requested.
    6.  This continues until `-1` is entered for `Day 1`, at which point the inner `while` loop finishes.
    7.  The `total_rainfall` for `Day 1` is printed.
    8.  The outer `for` loop then moves to `Day 2`, and the process repeats.

### Nested `for` inside `while` Loops: Finding the Longest Word

This pattern is useful when the overall process continues based on an unknown condition (outer `while` loop), but a fixed, repetitive action is needed for each step of that process (inner `for` loop).

*   **Problem Statement:** Find the length of the longest word from a set of words entered by the user. The user keeps entering words until `-1` is entered.
*   **Example Scenario:**
    *   Input: `IITM`, `online`, `degree`, `-1` -> Longest length: `6` (`degree`)
    *   Input: `Bachelor`, `of`, `Science`, `-1` -> Longest length: `8` (`Bachelor` or `Science`)
*   **Why this combination:**
    *   **Outer `while` loop:** The number of words the user will enter is unknown, terminating with a sentinel value (`-1`), making `while` suitable for the overall process.
    *   **Inner `for` loop:** To find the length of each word, we iterate through its characters, which is a fixed process for each word, making `for` (specifically, iterating over a string) suitable.

*   **Logic Breakdown:**
    1.  **Initialization:** A `max_length` variable is initialized to `0` to keep track of the longest word found so far.
    2.  **First Word Input:** Prompt the user to enter the first `word`.
    3.  **Outer `while` Loop (for words):** This loop continues as long as the entered `word` is not `"-1"`.
    4.  **Inner `for` Loop (for word length):**
        *   Inside the outer `while` loop, for each `word`, a `current_word_length` variable is initialized to `0`.
        *   The `for char in word:` loop iterates through each character of the `current word`.
        *   For each character, `current_word_length` is incremented. This effectively counts the characters.
    5.  **Updating `max_length`:** After the inner `for` loop finishes counting the characters of the current `word`, `current_word_length` is compared with `max_length`. If `current_word_length` is greater, `max_length` is updated.
    6.  **Next Word Input:** Prompt for the next `word`.
    7.  **Output:** Once `"-1"` is entered, the outer `while` loop terminates, and the final `max_length` is printed.

*   **Code Example: Longest Word**

    ```python
    max_length = 0  # Initialize max_length to 0
    
    print("Enter words (type -1 to stop):")
    word = input()
    
    # Outer while loop: Continues as long as the entered word is not "-1"
    while word != "-1":
        current_word_length = 0  # Initialize length for the current word
        
        # Inner for loop: Iterates through each character in the current word
        # This is a 'for-each' style loop, effectively counting characters
        for char in word:
            current_word_length += 1
        
        # Compare current word's length with the maximum found so far
        if current_word_length > max_length:
            max_length = current_word_length  # Update max_length if current word is longer
        
        # Get the next word from the user
        word = input()
    
    print(f"The length of the longest word is: {max_length}")
    ```

    **How it Works:**
    1.  `max_length` starts at `0`.
    2.  The program asks for the first `word`.
    3.  The outer `while` loop checks if the `word` is `"-1"`. If not, it enters.
    4.  `current_word_length` for the current `word` is reset to `0`.
    5.  The inner `for char in word:` loop iterates over each character, incrementing `current_word_length` for each one. This efficiently calculates the length of the `word`.
    6.  After the inner loop, `current_word_length` holds the length of the just-processed word. This is compared to `max_length`, and `max_length` is updated if the current word is longer.
    7.  The program then asks for the next `word`, and the outer `while` loop condition is re-evaluated.

## Summary and Important Tips

*   **Flexibility:** Python's `for` and `while` loops offer complete flexibility for nesting. All four combinations (`for`-`for`, `while`-`while`, `for`-`while`, `while`-`for`) are possible and useful.
*   **Choosing the Right Loop:**
    *   Use a `for` loop when you know the **exact number of iterations** or when you need to iterate over a **sequence** (like a `range`, list, or string).
    *   Use a `while` loop when the number of iterations is **unknown** and depends on a **condition** being met (e.g., until a specific input is received, or a certain state is achieved).
*   **Problem-Driven Design:** The choice of nesting structure should always be driven by the specific requirements and conditions of the problem you are trying to solve. Analyze whether the outer or inner iterations have a fixed count or depend on a dynamic condition.
*   **`break` Statement:** Remember that `break` only exits the *innermost* loop it is contained within. It does not affect any outer loops.
*   **Variable Scope:** Variables initialized *outside* an inner loop retain their values across inner loop iterations. Variables initialized *inside* an outer loop (but outside an inner loop) are re-initialized for each new iteration of the outer loop.
*   **Readability:** Keep nested loops as simple and clear as possible. Deeply nested loops (more than 2 or 3 levels) can become difficult to read and understand. Consider breaking down complex logic into separate functions if nesting becomes too deep.