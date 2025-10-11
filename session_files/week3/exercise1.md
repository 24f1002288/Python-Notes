# Python Practice Problems

## Q1: Daily Expense Tracker

**Problem Statement:**  
Create a program that helps a user track their daily expenses. The program should repeatedly ask the user to enter an expense amount until they type 'done'. Once they are finished, the program should calculate and display the total number of expenses, the total amount spent, and the average expense.

**Challenge:** Implement this using a while loop for input collection and a for loop for calculation.

### Input/Output Specification

**Input:**
- A series of floating-point numbers representing expenses, entered one by one.
- The string 'done' (case-insensitive) to signal the end of input.

**Output:**
- The total number of expenses entered.
- The total sum of all expenses, formatted to two decimal places.
- The average expense, formatted to two decimal places.

**Notes:**
- If no expenses are entered, the program should print a message indicating this and not attempt to calculate the average to avoid division by zero.

**Sample Case:**

```
Input:
12.50
3.45
25.00
8.99
done

Expected Output:
Number of expenses: 4
Total expenses: $49.94
Average expense: $12.48
```

---

## Q2: Filename Cleaner

**Problem Statement:**  
Write a program that "cleans" a list of filenames. For each filename, it should check if the name part (without the extension) contains any spaces and, if so, replace them with underscores. The program should then print the new, cleaned filename.

**Challenge:** Implement this using a for loop.

### Input/Output Specification

**Predefined Input (inside your code):**
```python
['Vacation photo 1.jpg', 'my report final.docx', 'budget-plan.xlsx', 'project presentation.ppt']
```

**User Input:** None.

**Output:**
- The cleaned filenames, printed one per line.

**Sample Case:**

```
Expected Output:
Cleaned filename: Vacation_photo_1.jpg
Cleaned filename: my_report_final.docx
Cleaned filename: budget-plan.xlsx
Cleaned filename: project_presentation.ppt
```

---

## Q3: Guess the Number Game

**Problem Statement:**  
Create a classic "Guess the Number" game. The program will generate a random integer between 1 and 100, and the user has to guess it. After each guess, the program will tell the user if their guess was too high or too low. The game ends when the user guesses the correct number, and the program should report how many guesses it took.

**Challenge:** Implement the core game logic using a while loop.

### Input/Output Specification

**Input:**
- A series of integers representing the user's guesses.

**Output:**
- Feedback after each guess ('Too high!' or 'Too low!').
- A final congratulatory message including the number of guesses taken.

**Sample Case:**

```
Secret number: 42
Input:
50
25
40
45
42

Expected Output:
Guess a number between 1 and 100: 50
Too high!
Guess a number between 1 and 100: 25
Too low!
Guess a number between 1 and 100: 40
Too low!
Guess a number between 1 and 100: 45
Too high!
Guess a number between 1 and 100: 42
Congratulations! You guessed the number in 5 tries.
```

---

## Q4: Simple Login System

**Problem Statement:**  
Simulate a simple login system. The system allows a user up to three attempts to enter the correct password. If they succeed, print a welcome message. If they fail three times, lock them out.

**Challenge:** Implement this using a while loop.

### Input/Output Specification

**Predefined Input (inside your code):**
```python
'Python123'
```

**User Input:**  
The user's password attempt (a string).

**Sample Case 1:**

```
Input:
wrongpass
anotherwrong
Python123

Expected Output:
Enter password: wrongpass
Incorrect password. You have 2 attempts remaining.
Enter password: anotherwrong
Incorrect password. You have 1 attempts remaining.
Enter password: Python123
Access granted. Welcome!
```

**Sample Case 2:**

```
Input:
pass1
pass2
pass3

Expected Output:
Enter password: pass1
Incorrect password. You have 2 attempts remaining.
Enter password: pass2
Incorrect password. You have 1 attempts remaining.
Enter password: pass3
Incorrect password. You have 0 attempts remaining.
Access denied. Account locked.
```

---

## Q5: Prime Number Generator

**Problem Statement:**  
Write a program that finds all prime numbers up to a given integer N. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

**Challenge:**  
- Write the solution using nested for loops.  
- Write the solution using a while loop for the outer loop and a for loop for the inner loop.

### Input/Output Specification

**Input:**
- N (int) - The upper limit to search for prime numbers (inclusive).

**Output:**
- All prime numbers from 2 up to N, printed on a single line and separated by spaces.

**Notes:**
- Remember that 1 is not a prime number.
- To check if a number `num` is prime, test divisibility from 2 to `num - 1`.

**Sample Case:**

```
Input:
20

Expected Output:
2 3 5 7 11 13 17 19
```

---

## Q6: Temperature Data Analyzer

**Problem Statement:**  
You are given a list of daily maximum temperatures for a week. Write a program to analyze this data. It should calculate the average temperature, find the highest and lowest temperatures, and count how many days were "hot" (e.g., above 25°C).

**Challenge:** Implement the analysis using a for loop.

### Input/Output Specification

**Predefined Input (inside your code):**
```python
[22, 26.5, 19, 28, 25, 31.2, 24]
```

**User Input:**
- `hot_threshold` (float) - The temperature to consider as "hot".

**Output:**
- The highest temperature.  
- The lowest temperature.  
- The average temperature for the week, formatted to two decimal places.  
- The number of hot days.

**Sample Case:**

```
Input:
27.0

Expected Output:
Highest Temperature: 31.2°C
Lowest Temperature: 19.0°C
Average Temperature: 25.10°C
Number of hot days: 2
```

---

## Q7: Text Reverser and Palindrome Checker

**Problem Statement:**  
Write a program that takes a string from the user, reverses it, and then checks if the original string is a palindrome (reads the same forwards and backward).

**Challenge:**  
Provide two implementations for reversing the string:
- Using a for loop, iterating through the original string and building a new, reversed string.
- Using a while loop with two index pointers (one at the start, one at the end).

### Input/Output Specification

**Input:**
- `text` (str) - The string to be checked.

**Output:**
- The reversed string.  
- A message indicating whether the original string is a palindrome.

**Notes:**
- Ignore case and spaces when checking for palindromes.
- Preprocess the string by converting to lowercase and removing spaces.

**Sample Case 1:**

```
Input:
racecar

Expected Output:
Reversed string: racecar
The string "racecar" is a palindrome.
```

**Sample Case 2:**

```
Input:
Hello World

Expected Output:
Reversed string: dlroW olleH
The string "Hello World" is not a palindrome.
```

---

## Q8: Shopping Cart Simulator (List Version)

**Problem Statement:**  
Create a command-line shopping cart using lists to store product data. The program should display a list of available items and their prices. The user can add items to their cart by typing the item name. The program should keep running, allowing multiple additions, until they type 'checkout'.

**Challenge:**  
Use parallel lists to store item names and prices. Use a while loop for the shopping session and a for loop to print the receipt.

### Input/Output Specification

**Predefined Input (inside your code):**
```python
products = ['apple', 'banana', 'milk', 'bread']
prices = [0.50, 0.25, 3.50, 2.75]
```

**User Input:**
- A series of strings representing items to add to the cart.
- The string 'checkout' to end the session.

**Output:**
- Confirmation message after adding an item.  
- Error message for invalid items.  
- A final receipt listing each item and the total cost.

**Sample Case:**

```
Input:
apple
milk
apple
cheese
banana
checkout

Expected Output:
--- MENU ---
apple: $0.5
banana: $0.25
milk: $3.5
bread: $2.75
Enter an item to add to the cart, or 'checkout' to finish: apple
apple added to cart.
Enter an item to add to the cart, or 'checkout' to finish: milk
milk added to cart.
Enter an item to add to the cart, or 'checkout' to finish: apple
apple added to cart.
Enter an item to add to the cart, or 'checkout' to finish: cheese
Sorry, 'cheese' is not a valid item.
Enter an item to add to the cart, or 'checkout' to finish: banana
banana added to cart.
Enter an item to add to the cart, or 'checkout' to finish: checkout
--- YOUR RECEIPT ---
apple: $0.50
milk: $3.50
apple: $0.50
banana: $0.25
--------------------
TOTAL: $4.75
```

---

## Q9: Pomodoro Timer

**Problem Statement:**  
Create a simple text-based Pomodoro timer. The Pomodoro technique uses a timer to break work into 25-minute intervals separated by short breaks.

**Challenge:** Use a for loop to handle the cycles of work and break periods.

### Input/Output Specification

**Input:**
- `sessions` (int) - The number of Pomodoro sessions to run.

**Output:**
- Messages indicating the start and end of each work and break period for each session.

**Notes:**
- Use the `time` module and `time.sleep(seconds)` to simulate time.  
- For faster testing, use short pauses (e.g., 5 seconds for work, 2 for breaks).

**Sample Case:**

```
Input:
2

Expected Output:
Session 1: Work time (25 minutes). Focus!
(Program pauses)
Session 1: Break time (5 minutes). Relax!
(Program pauses)
Session 2: Work time (25 minutes). Focus!
(Program pauses)
Session 2: Break time (5 minutes). Relax!
(Program pauses)
Pomodoro complete!
```

---

## Q10: Grade Calculator

**Problem Statement:**  
Write a program that calculates the final letter grade for a student based on a series of scores.

**Challenge:** Use a for loop to get the score inputs and calculate their sum.

### Input/Output Specification

**Input:**
- `num_scores` (int) - Number of scores to be entered.  
- A series of `num_scores` floats, representing the scores.

**Output:**
- The average score, formatted to two decimal places.  
- The final letter grade.

**Notes:**
- Validate that each score is between 0 and 100.  
- Use a while loop for validation inside the for loop.

**Grading Scale:**
```
90–100: A
80–89.9: B
70–79.9: C
60–69.9: D
< 60: F
```

**Sample Case:**

```
Input:
3
95
82
78

Expected Output:
Average score: 85.00
Final Grade: B
```



