
### Q1: Inventory Update & Cost Calculator

**Problem Statement:**
You are managing a small store's inventory. Write a program that takes an item's current stock, its unit price, and a recent sale quantity as input. Your program should then calculate and display the remaining stock after the sale, the total revenue generated from this specific sale, and the estimated cost to restock double the quantity that was sold.

**Input/Output Specification:**
-   **Input:**
    1.  `current_stock` (int)
    2.  `unit_price` (float)
    3.  `sale_quantity` (int)
-   **Output:**
    1.  On the first line, print `Remaining stock: X`
    2.  On the second line, print `Sale revenue: $Y`
    3.  On the third line, print `Restock cost for Z units: $W`

**Notes:**
-   `X` represents the new integer stock level.
-   `Y` and `W` should be floating-point numbers, representing currency.
-   `Z` is calculated as exactly double the `sale_quantity`.

**Sample Case:**
**Input:**
```
150
12.75
25
```
**Expected Output:**
```
Remaining stock: 125
Sale revenue: $318.75
Restock cost for 50 units: $637.5
```

---
### Q2: String Manipulator & Password Generator

**Problem Statement:**
Create a program that acts as a simple password and hint generator. It takes a user's chosen "favorite word" and a "lucky number" as input. It then constructs a "strong" password by combining parts of the word, the number, and some fixed characters. Additionally, it generates a "hint" based on the word.

**Input/Output Specification:**
-   **Input:**
    1.  `favorite_word` (str)
    2.  `lucky_number` (int)
-   **Output:**
    1.  On the first line, print `Generated Password: P`
    2.  On the second line, print `Password Hint: H`

**Notes:**
-   `P` (the generated password) should be constructed as follows:
    *   The first three characters of `favorite_word`.
    *   The `lucky_number` converted to a string.
    *   The last character of `favorite_word`.
    *   The first character of `favorite_word`, repeated twice.
    *   The total length of `favorite_word`, converted to a string.
-   `H` (the password hint) should be constructed as:
    *   The first character of `favorite_word`.
    *   The middle part of `favorite_word` (from the second character up to, but not including, the last character).
    *   The last character of `favorite_word`.
    *   The `lucky_number` converted to a string.
-   Assume `favorite_word` will always be at least 3 characters long.

**Sample Case:**
**Input:**
```
Python
2024
```
**Expected Output:**
```
Generated Password: Pyt2024nPP6
Password Hint: Pyth2024on
```

---
### Q3: Recipe Unit Converter

**Problem Statement:**
Many recipes use US customary units, but it's often useful to convert these to metric for consistency or international use. Write a program that takes quantities of flour in cups, sugar in tablespoons, and butter in pounds as input. It should then convert and display these quantities in milliliters (for flour and sugar) and grams (for butter).

**Input/Output Specification:**
-   **Input:**
    1.  `cups_flour` (float)
    2.  `tbsp_sugar` (float)
    3.  `pounds_butter` (float)
-   **Output:**
    1.  On the first line, print `Flour: X ml`
    2.  On the second line, print `Sugar: Y ml`
    3.  On the third line, print `Butter: Z grams`

**Notes:**
-   Use the following conversion factors:
    *   1 cup = 236.588 milliliters
    *   1 tablespoon = 14.7868 milliliters
    *   1 pound = 453.592 grams
-   `X`, `Y`, and `Z` should be floating-point numbers.

**Sample Case:**
**Input:**
```
2.5
12.0
0.75
```
**Expected Output:**
```
Flour: 591.47 ml
Sugar: 177.4416 ml
Butter: 340.194 grams
```

---
### Q4: Simple Grade Calculator & Status Checker

**Problem Statement:**
Develop a program to assist teachers in quickly evaluating student performance. The program should accept three assignment scores as input, calculate the student's average score, and then determine if the student has "passed" based on a simple pass/fail threshold.

**Input/Output Specification:**
-   **Input:**
    1.  `assignment1_score` (float)
    2.  `assignment2_score` (float)
    3.  `assignment3_score` (float)
-   **Output:**
    1.  On the first line, print `Average Score: A`
    2.  On the second line, print `Passed: B`

**Notes:**
-   `A` should be a floating-point number representing the average of the three scores.
-   `B` should be a boolean value (`True` or `False`). A student is considered to have "passed" if their average score is 60.0 or higher.

**Sample Case:**
**Input:**
```
75.0
82.5
55.0
```
**Expected Output:**
```
Average Score: 70.83333333333333
Passed: True
```

---
### Q5: Time Converter & Event Planner

**Problem Statement:**
Imagine you're planning a short event. Write a program that takes a total duration in minutes as input. It should first convert this duration into a more readable format of hours and remaining minutes. Then, assuming an event always starts at a fixed time of 09:00 AM, calculate and display the exact end time of the event.

**Input/Output Specification:**
-   **Input:**
    1.  `total_minutes_duration` (int)
-   **Output:**
    1.  On the first line, print `Duration: H hours M minutes`
    2.  On the second line, print `Event Start: HH:MM`
    3.  On the third line, print `Event End: EE:FF`

**Notes:**
-   `H` is the number of full hours, and `M` is the remaining minutes from the `total_minutes_duration`.
-   The `Event Start` time is always `09:00`.
-   `EE` and `FF` represent the end hour and end minute, respectively. You need to add the `total_minutes_duration` to the 09:00 start time.
-   For all time displays (e.g., `HH:MM` and `EE:FF`), ensure that single-digit minutes (like 5) are formatted with a leading zero (e.g., `05`) to maintain a consistent `HH:MM` format.

**Sample Case:**
**Input:**
```
145
```
**Expected Output:**
```
Duration: 2 hours 25 minutes
Event Start: 09:00
Event End: 11:25
```

---
### Q6: Receipt Calculator

**Problem Statement:**
You are developing a basic point-of-sale system. Your program needs to calculate the total cost of a customer's purchase, including a discount. It should take the price and quantity of two different items, along with a percentage discount, as input. The program will then calculate the subtotal, the discount amount, the final total price, and indicate if the final total exceeds a predefined budget.

**Input/Output Specification:**
-   **Input:**
    1.  `item1_price` (float)
    2.  `item1_qty` (int)
    3.  `item2_price` (float)
    4.  `item2_qty` (int)
    5.  `discount_percent` (float, e.g., `15.0` for 15%)
-   **Output:**
    1.  On the first line, print `Subtotal: $S`
    2.  On the second line, print `Discount Applied: $D`
    3.  On the third line, print `Final Total: $F`
    4.  On the fourth line, print `Above Budget: B`

**Notes:**
-   `S`, `D`, and `F` should be floating-point numbers, representing currency.
-   The `discount_percent` is applied to the calculated subtotal.
-   `B` should be a boolean value (`True` or `False`). Assume the budget is fixed at $100.00.

**Sample Case:**
**Input:**
```
25.50
2
10.00
3
10.0
```
**Expected Output:**
```
Subtotal: $81.0
Discount Applied: $8.1
Final Total: $72.9
Above Budget: False
```
