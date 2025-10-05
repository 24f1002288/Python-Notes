Here are 5 moderately challenging coding exercises, adhering strictly to the provided cumulative topic list for Weeks 1 and 2.

---
### Q1: Smart Unit Converter

**Problem Statement:**
Write a program that acts as a simple smart converter and calculator. It should first ask the user for a numeric value and its initial unit (e.g., "meters", "feet", "celsius", "fahrenheit"). Then, it should present a menu of operations: either convert to another unit or perform a mathematical calculation (square root or power). Based on the user's choices, it should perform the action and print the result.

**Input/Output Specification:**
-   **Input:**
    1.  `value` (float) - The numeric value to operate on.
    2.  `initial_unit` (str) - The unit of the initial value (e.g., 'm', 'ft', 'C', 'F'). Case-insensitive.
    3.  `operation_type` (str) - Choice between 'convert' or 'calculate'. Case-insensitive.
    4.  If `operation_type` is 'convert':
        *   `target_unit` (str) - The unit to convert to (e.g., 'ft', 'm', 'F', 'C'). Case-insensitive.
    5.  If `operation_type` is 'calculate':
        *   `calc_choice` (str) - Choice between 'sqrt' (square root) or 'power' (raise to a power). Case-insensitive.
        *   If `calc_choice` is 'power':
            *   `exponent` (float) - The power to raise the value to.
-   **Output:**
    *   A single line showing the result, formatted as `"{result_value} {result_unit}"` or `"{result_value}"` if no unit is applicable (e.g., after `sqrt`).
    *   If an invalid choice or conversion is made, print an appropriate error message.

**Notes:**
-   Support the following conversions:
    *   Meters (m) to Feet (ft): `1 m = 3.28084 ft`
    *   Feet (ft) to Meters (m): `1 ft = 0.3048 m`
    *   Celsius (C) to Fahrenheit (F): `F = C * 9/5 + 32`
    *   Fahrenheit (F) to Celsius (C): `C = (F - 32) * 5/9`
-   Ensure all unit inputs are handled case-insensitively (e.g., 'm', 'M' are both meters).
-   For `sqrt`, the value must be non-negative. If negative, print an error.
-   Use the `math` module for `sqrt` and `pow`.

**Sample Case 1 (Conversion):**
**Input:**
```
10
m
convert
ft
```
**Expected Output:**
```
32.8084 ft
```

**Sample Case 2 (Calculation - Sqrt):**
**Input:**
```
25
units
calculate
sqrt
```
**Expected Output:**
```
5.0
```

**Sample Case 3 (Calculation - Power):**
**Input:**
```
2
none
calculate
power
3
```
**Expected Output:**
```
8.0
```

**Sample Case 4 (Invalid Sqrt):**
**Input:**
```
-9
units
calculate
sqrt
```
**Expected Output:**
```
Error: Cannot calculate square root of a negative number.
```

---

### Q2: Text Analysis & Transformation

**Problem Statement:**
Create a program that first analyzes a user-provided sentence for specific characteristics and then offers to transform it based on another user choice. The analysis should include checking if it starts with a vowel, if it contains the word "Python" (case-insensitive), and its total length. The transformation options should be to convert the sentence to uppercase, lowercase, or title case.

**Input/Output Specification:**
-   **Input:**
    1.  `sentence` (str) - The sentence to analyze and transform.
    2.  `transform_action` (str) - The desired transformation: 'upper', 'lower', or 'title'. Case-insensitive.
-   **Output:**
    1.  First line: `Length: X characters.`
    2.  Second line: `Starts with vowel: {True/False}`
    3.  Third line: `Contains 'Python': {True/False}`
    4.  Fourth line: `Transformed sentence: {result_sentence}`
    5.  If `transform_action` is invalid, print `Invalid transformation choice.` on the fourth line instead of the transformed sentence.

**Notes:**
-   Vowels are 'a', 'e', 'i', 'o', 'u' (case-insensitive).
-   The word "Python" should be checked case-insensitively.
-   Use string methods for analysis and transformation.

**Sample Case 1:**
**Input:**
```
This is a Python sentence.
upper
```
**Expected Output:**
```
Length: 28 characters.
Starts with vowel: False
Contains 'Python': True
Transformed sentence: THIS IS A PYTHON SENTENCE.
```

**Sample Case 2:**
**Input:**
```
An apple a day.
title
```
**Expected Output:**
```
Length: 16 characters.
Starts with vowel: True
Contains 'Python': False
Transformed sentence: An Apple A Day.
```

**Sample Case 3:**
**Input:**
```
hello world
invalid
```
**Expected Output:**
```
Length: 11 characters.
Starts with vowel: False
Contains 'Python': False
Invalid transformation choice.
```

---

### Q3: Dice Roll Game

**Problem Statement:**
Develop a simple dice game. The program will simulate rolling two six-sided dice and calculate their sum. Before the roll, the user will be prompted to make two predictions:
1.  Is the sum of the dice "even" or "odd"?
2.  Is the sum of the dice "high" (sum > 7) or "low" (sum <= 7)?
After the dice are rolled, the program should reveal the dice values, their sum, and then tell the user if each of their predictions was correct or incorrect.

**Input/Output Specification:**
-   **Input:**
    1.  `even_odd_guess` (str) - User's guess: 'even' or 'odd'. Case-insensitive.
    2.  `high_low_guess` (str) - User's guess: 'high' or 'low'. Case-insensitive.
-   **Output:**
    1.  First line: `Dice 1: X, Dice 2: Y`
    2.  Second line: `Sum: Z`
    3.  Third line: `Even/Odd Guess: {Correct/Incorrect}`
    4.  Fourth line: `High/Low Guess: {Correct/Incorrect}`

**Notes:**
-   Use the `random.randrange()` function to simulate dice rolls (values 1 to 6, inclusive).
-   The "high" threshold is > 7, meaning 8, 9, 10, 11, 12 are high. The "low" threshold is <= 7, meaning 2, 3, 4, 5, 6, 7 are low.
-   Handle user input for guesses case-insensitively.

**Sample Case:**
**Input:**
```
odd
high
```
**Expected Output (example, dice rolls are random):**
```
Dice 1: 3, Dice 2: 4
Sum: 7
Even/Odd Guess: Correct
High/Low Guess: Incorrect
```

---

### Q4: Simple Invoice Generator

**Problem Statement:**
Create a program that generates a simple invoice for a single item purchase. The program should ask for the item's name, quantity, and unit price. It should then prompt for a discount code. If the discount code is "SAVE10", a 10% discount is applied to the subtotal. Otherwise, no discount is applied. Finally, a fixed sales tax of 5% is applied to the discounted subtotal (or original subtotal if no discount). The program should then print a formatted invoice.

**Input/Output Specification:**
-   **Input:**
    1.  `item_name` (str)
    2.  `quantity` (int)
    3.  `unit_price` (float)
    4.  `discount_code` (str) - Case-insensitive.
-   **Output:**
    *   The invoice should be formatted as follows, with monetary values rounded to two decimal places:
        ```
        --- INVOICE ---
        Item: {item_name}
        Quantity: {quantity}
        Unit Price: ${unit_price:.2f}
        Subtotal: ${subtotal:.2f}
        Discount (10%): -${discount_amount:.2f}
        Tax (5%): ${tax_amount:.2f}
        Total: ${final_total:.2f}
        ---------------
        ```
    *   If no discount is applied, `Discount (10%): -$0.00` should be printed.

**Notes:**
-   The discount code "SAVE10" should be checked case-insensitively.
-   Calculations:
    *   `subtotal = quantity * unit_price`
    *   `discount_amount = subtotal * 0.10` (if code is "SAVE10")
    *   `taxable_amount = subtotal - discount_amount`
    *   `tax_amount = taxable_amount * 0.05`
    *   `final_total = taxable_amount + tax_amount`
-   Use f-strings for formatting the output, ensuring two decimal places for currency.

**Sample Case 1 (with discount):**
**Input:**
```
Laptop
1
1200.00
SAVE10
```
**Expected Output:**
```
--- INVOICE ---
Item: Laptop
Quantity: 1
Unit Price: $1200.00
Subtotal: $1200.00
Discount (10%): -$120.00
Tax (5%): $54.00
Total: $1134.00
---------------
```

**Sample Case 2 (no discount):**
**Input:**
```
Mouse
2
25.50
NONE
```
**Expected Output:**
```
--- INVOICE ---
Item: Mouse
Quantity: 2
Unit Price: $25.50
Subtotal: $51.00
Discount (10%): -$0.00
Tax (5%): $2.55
Total: $53.55
---------------
```

---

### Q5: Basic Password Validator

**Problem Statement:**
Write a program that evaluates the strength of a user-provided password based on several criteria and provides feedback. The criteria are:
1.  **Length:** At least 8 characters long.
2.  **Uppercase:** Contains at least one uppercase letter.
3.  **Lowercase:** Contains at least one lowercase letter.
4.  **Digit:** Contains at least one digit.
5.  **Special Character:** Contains at least one of these special characters: `!@#$%^&*`
Based on how many criteria are met, the password should be rated:
*   **Weak:** 0-2 criteria met.
*   **Moderate:** 3-4 criteria met.
*   **Strong:** All 5 criteria met.

The program should also print specific feedback for each unmet criterion.

**Input/Output Specification:**
-   **Input:**
    1.  `password` (str) - The password to validate.
-   **Output:**
    1.  First line: `Password Strength: {Weak/Moderate/Strong}`
    2.  Subsequent lines (only if criteria are NOT met):
        *   `Feedback: Password must be at least 8 characters long.`
        *   `Feedback: Password must contain at least one uppercase letter.`
        *   `Feedback: Password must contain at least one lowercase letter.`
        *   `Feedback: Password must contain at least one digit.`
        *   `Feedback: Password must contain at least one of !@#$%^&*`

**Notes:**
-   To check for the presence of uppercase, lowercase, or digits without using loops or `any()`, you can compare the original password with its `lower()`, `upper()` versions, and check for individual digits using the `in` operator.
-   The special characters to check for are `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`. Use the `in` operator for these.

**Sample Case 1 (Weak):**
**Input:**
```
short1
```
**Expected Output:**
```
Password Strength: Weak
Feedback: Password must be at least 8 characters long.
Feedback: Password must contain at least one uppercase letter.
Feedback: Password must contain at least one of !@#$%^&*
```

**Sample Case 2 (Moderate):**
**Input:**
```
MyPass12
```
**Expected Output:**
```
Password Strength: Moderate
Feedback: Password must contain at least one of !@#$%^&*
```

**Sample Case 3 (Strong):**
**Input:**
```
Secure!P@ss
```
**Expected Output:**
```
Password Strength: Strong
```

---
