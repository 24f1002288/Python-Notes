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
Write a program that finds all prime numbers up to a given integer N.

**Challenge:**  
- Write the solution using nested for loops.  
- Write the solution using a while loop for the outer loop and a for loop for the inner loop.

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
You are given a list of daily maximum temperatures for a week. Write a program to analyze this data.

**Challenge:** Implement the analysis using a for loop.

**Predefined Input:**
```python
[22, 26.5, 19, 28, 25, 31.2, 24]
```

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
Write a program that takes a string from the user, reverses it, and checks if it’s a palindrome.

**Challenge:** Provide two implementations — using a for loop and using a while loop.

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
Create a command-line shopping cart using lists to store product data.

**Challenge:** Use parallel lists and loops for adding, checking, and printing.

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
...
TOTAL: $4.75
```

---

## Q9: Pomodoro Timer

**Problem Statement:**  
Create a simple text-based Pomodoro timer.

**Challenge:** Use a for loop to handle sessions.

**Sample Case (shortened for demo):**

```
Input:
2

Expected Output:
Session 1: Work time (25 minutes). Focus!
Session 1: Break time (5 minutes). Relax!
Session 2: Work time (25 minutes). Focus!
Session 2: Break time (5 minutes). Relax!
Pomodoro complete!
```

---

## Q10: Grade Calculator

**Problem Statement:**  
Write a program that calculates the final letter grade for a student.

**Challenge:** Use loops for input and validation.

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

