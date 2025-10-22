
## 5. Movie Ratings Analyzer

**Context:** You run a small movie review site.

**Task:**  
Write a function that takes a tuple of movie ratings (from 1 to 10) and returns the **highest** and **lowest** ratings.

**Sample Input:**
```python
ratings = (8, 9, 6, 10, 7, 9)
```

**Sample Output:**
```
Highest: 10, Lowest: 6
```

---

## 6. Email Domain Extractor

**Context:** You have a list of email addresses and need to identify unique domains.

**Task:**  
Write a program that extracts all **unique email domains** from a list of email addresses.

**Sample Input:**
```python
emails = ["alice@gmail.com", "bob@yahoo.com", "alice@gmail.com", "carol@outlook.com"]
```

**Sample Output:**
```
Unique Domains: {'gmail.com', 'yahoo.com', 'outlook.com'}
```

---

## 7. Grocery List Updater

**Context:** Your grocery shopping app needs a feature to update items dynamically.

**Task:**  
Write a function that:
1. Accepts a list of grocery items.
2. Asks the user to input an item to **add** or **remove**.
3. Returns the updated list.

**Sample Input/Output:**
```
Current List: ['milk', 'bread', 'eggs']
Enter 'add' or 'remove': add
Enter item: butter
Updated List: ['milk', 'bread', 'eggs', 'butter']
```

---

## 8. Library Borrow System

**Context:** You are building a system to track borrowed books.

**Task:**  
Maintain a set of borrowed book IDs.  
Write a function that adds a book when borrowed, removes it when returned, and displays the current borrowed set.

**Sample Input/Output:**
```
Borrowed Books: {101, 102}
Borrowed Book ID: 103
Updated Books: {101, 102, 103}
Returned Book ID: 101
Updated Books: {102, 103}
```

---

## 9. Common Friends Finder

**Context:** A social media app shows mutual friends between two users.

**Task:**  
Write a function that takes two sets of friends and prints their **common friends**.

**Sample Input:**
```python
user1_friends = {'Alice', 'Bob', 'Charlie'}
user2_friends = {'Bob', 'David', 'Charlie'}
```

**Sample Output:**
```
Common Friends: {'Bob', 'Charlie'}
```

---

## 10. Student Record System

**Context:** A school database stores each student’s name and their marks.

**Task:**  
Create a function that accepts a list of tuples — each tuple containing a student’s name and marks.  
Print each student’s grade using these rules:
- Marks ≥ 90 → A
- Marks ≥ 75 → B
- Marks ≥ 60 → C
- Otherwise → D

**Sample Input:**
```python
students = [('Alice', 88), ('Bob', 92), ('Charlie', 59)]
```

**Sample Output:**
```
Alice: B
Bob: A
Charlie: D
```

---

## 11. Even and Odd Splitter

**Context:** You are analyzing numbers for a statistics app.

**Task:**  
Write a function that takes a list of integers and returns two separate lists — one containing even numbers and the other containing odd numbers.

**Sample Input:**
```python
numbers = [3, 6, 9, 12, 15, 18]
```

**Sample Output:**
```
Even: [6, 12, 18]
Odd: [3, 9, 15]
```

---

## 12. Name Initials Extractor

**Context:** You’re making a contact app that stores initials for quick lookup.

**Task:**  
Write a function that takes a list of full names (as strings) and returns a list of initials.

**Sample Input:**
```python
names = ["Alice Brown", "Bob Smith", "Charlie Adams"]
```

**Sample Output:**
```
['A.B.', 'B.S.', 'C.A.']
```

---

## 13. Second Largest Finder

**Context:** A game leaderboard system needs to identify the runner-up score.

**Task:**  
Write a function that takes a list of scores and returns the **second largest** score.

**Sample Input:**
```python
scores = [45, 67, 89, 90, 67]
```

**Sample Output:**
```
Second Largest: 89
```

---

## 14. List Flattener

**Context:** A data-cleaning task requires flattening nested lists.

**Task:**  
Write a function that takes a list of tuples and returns a single flattened list containing all elements.

**Sample Input:**
```python
data = [(1, 2), (3, 4), (5, 6)]
```

**Sample Output:**
```
[1, 2, 3, 4, 5, 6]
```

---

## 15. Set Difference Analyzer

**Context:** You’re comparing participants of two workshops.

**Task:**  
Given two sets of participants, find who attended **only the first workshop**.

**Sample Input:**
```python
workshop1 = {"Alice", "Bob", "Charlie"}
workshop2 = {"Bob", "Diana"}
```

**Sample Output:**
```
Only in Workshop 1: {'Alice', 'Charlie'}
```

---

## 16. Unique Elements in List

**Context:** You need to clean duplicate entries from a dataset.

**Task:**  
Write a function that removes duplicates from a list while keeping the **original order**.

**Sample Input:**
```python
data = [1, 2, 3, 2, 4, 1, 5]
```

**Sample Output:**
```
[1, 2, 3, 4, 5]
```

---

## 17. Tuple Sorter

**Context:** You have pairs of (name, score) that need to be sorted by score.

**Task:**  
Write a function that sorts a list of tuples based on the second element in each tuple.

**Sample Input:**
```python
records = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
```

**Sample Output:**
```
[('Bob', 75), ('Alice', 88), ('Charlie', 92)]
```

---

## 18. Common and Distinct Elements

**Context:** You are comparing datasets for overlap.

**Task:**  
Write a function that takes two lists and returns two sets — one with **common elements** and one with **distinct elements**.

**Sample Input:**
```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
```

**Sample Output:**
```
Common: {3, 4}
Distinct: {1, 2, 5, 6}
```

---

## 19. Word Length Filter

**Context:** You’re filtering short words from a paragraph for keyword extraction.

**Task:**  
Write a function that returns only words longer than a given length `n`.

**Sample Input:**
```python
words = ["the", "curious", "case", "of", "python"]
n = 4
```

**Sample Output:**
```
['curious', 'python']
```

---

## 20. List Rotation

**Context:** You need to simulate cyclic rotations of a dataset.

**Task:**  
Write a function that rotates the elements of a list by `k` positions to the right.

**Sample Input:**
```python
data = [1, 2, 3, 4, 5]
k = 2
```

**Sample Output:**
```
[4, 5, 1, 2, 3]
```

---

**End of Set 2 (No Dictionaries)**
