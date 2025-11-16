**1. Number Grid Generator**

Write a function named `write_number_grid` that accepts three arguments: a filename `file_path`, a positive integer `m`, and a positive integer `n`. The function should create a file at `file_path` and write the first `m * n` positive integers to it in the following way:
* Each line should be a sequence of `n` space-separated integers.
* There should be a total of `m` lines in the file.

### Example
* **Input (Function Call):** `write_number_grid('grid.txt', 5, 3)`
* **Output (Contents of `grid.txt`):**
    ```
    1 2 3
    4 5 6
    7 8 9
    10 11 12
    13 14 15
    ```

---

**2. Timestamped Logger**

Write a function named `log_message` that accepts two string arguments: a filename `log_file` and a `message`. The function should append the `message` to the `log_file`, prefixed with the current date and time in the format `[YYYY-MM-DD HH:MM:SS]`. Each log entry must be on a new line. (You will need to `import datetime`).

### Example
* **Input (Function Call):** `log_message('app.txt', 'User login successful.')`
* **Output (Contents of `app.txt` after running, assuming the file was empty and the time is 7:02:11 PM on Nov 14, 2025):**
    ```
    [2025-11-14 19:02:11] - User login successful.
    ```
* **If run again with:** `log_message('app.txt', 'File upload failed.')`
* **The file would become:**
    ```
    [2025-11-14 19:02:11] - User login successful.
    [2025-11-14 19:02:12] - File upload failed.
    ```

---

**3. Configuration File Reader**

Write a function named `read_config` that accepts one argument: a filename `config_file`. The `config_file` contains application settings, with one setting per line in the format `key=value` (e.g., `theme=dark`, `font_size=12`). The function should read this file and return a Python dictionary containing the key-value pairs.

### Example
* **Input (Contents of `settings.txt`):**
    ```
    theme=dark
    font_size=12
    username=admin
    ```
* **Function Call:** `read_config('settings.txt')`
* **Output (Return Value):** `{'theme': 'dark', 'font_size': '12', 'username': 'admin'}`

---

**4. Configuration File Writer**

Write a function named `write_config` that accepts two arguments: a filename `config_file` and a Python dictionary `settings_dict`. The function should overwrite the `config_file`, writing each key-value pair from the dictionary as a new line in the format `key=value`.

### Example
* **Input (Function Call):**
    ```python
    settings = {'user': 'johndoe', 'mode': 'night', 'notifications': 'off'}
    write_config('new_config.txt', settings)
    ```
* **Output (Contents of `new_config.txt`):**
    ```
    user=johndoe
    mode=night
    notifications=off
    ```

---

**5. Find and Replace in File**

Write a function named `find_and_replace` that accepts four string arguments: `input_file`, `output_file`, `old_word`, and `new_word`. The function should read the entire contents of `input_file`, replace every occurrence of `old_word` with `new_word`, and write the modified content to `output_file`.

### Example
* **Input (Contents of `story.txt`):**
    ```
    A fast brown fox jumps over the lazy dog.
    The fast fox is very fast.
    ```
* **Function Call:** `find_and_replace('story.txt', 'new_story.txt', 'fast', 'quick')`
* **Output (Contents of `new_story.txt`):**
    ```
    A quick brown fox jumps over the lazy dog.
    The quick fox is very quick.
    ```

---

**6. Line Filter**

Write a function named `filter_lines` that accepts three string arguments: `input_file`, `output_file`, and `keyword`. The function should read `input_file` line by line and write only the lines that contain the `keyword` to `output_file`. Each written line should maintain its original newline.

### Example
* **Input (Contents of `server.txt`):**
    ```
    [INFO] Server started successfully.
    [DEBUG] Checking database connection...
    [ERROR] Failed to connect to database.
    [INFO] Listening on port 8080.
    [ERROR] User authentication failed.
    ```
* **Function Call:** `filter_lines('server.txt', 'errors.txt', 'ERROR')`
* **Output (Contents of `errors.txt`):**
    ```
    [ERROR] Failed to connect to database.
    [ERROR] User authentication failed.
    ```

---

**7. Add Line Numbers**

Write a function named `add_line_numbers` that accepts two string arguments: `input_file` and `output_file`. The function should read the content of `input_file` and write it to `output_file`, with each line prefixed by its line number, followed by a colon and a space (e.g., `1: Hello world`).

### Example
* **Input (Contents of `poem.txt`):**
    ```
    Roses are red,
    Violets are blue,
    Sugar is sweet,
    And so are you.
    ```
* **Function Call:** `add_line_numbers('poem.txt', 'numbered_poem.txt')`
* **Output (Contents of `numbered_poem.txt`):**
    ```
    1: Roses are red,
    2: Violets are blue,
    3: Sugar is sweet,
    4. And so are you.
    ```

---

**8. Merge Multiple Files**

Write a function named `merge_files` that accepts two arguments: a list of filenames `file_list` and a single filename `output_file`. The function should read the content of each file in `file_list` (in order) and append all their contents together into the `output_file`.

### Example
* **Input (Contents of `part1.txt`):**
    ```
    This is the first part.
    ```
* **Input (Contents of `part2.txt`):**
    ```
    This is the second part.
    ```
* **Function Call:** `merge_files(['part1.txt', 'part2.txt'], 'merged.txt')`
* **Output (Contents of `merged.txt`):**
    ```
    This is the first part.
    This is the second part.
    ```

---

**9. Simple Template Filler**

Write a function named `fill_template` that accepts three arguments: a `template_file`, an `output_file`, and a dictionary `data`. The `template_file` contains text with placeholders (e.g., `Hello, {{name}}! Today is {{day}}.`). The function should read the template, replace all placeholders (like `{{name}}`) with their corresponding values from the `data` dictionary, and write the result to `output_file`.

### Example
* **Input (Contents of `email.txt`):**
    ```
    Dear {{name}},
    
    You are invited to our event on {{date}}.
    We hope to see you at {{location}}.
    ```
* **Input (Function Call):**
    ```python
    data = {'name': 'Alex', 'date': 'November 30th', 'location': 'City Hall'}
    fill_template('email.txt', 'invite.txt', data)
    ```
* **Output (Contents of `invite.txt`):**
    ```
    Dear Alex,
    
    You are invited to our event on November 30th.
    We hope to see you at City Hall.
    ```

---

**10. Reverse File Content**

Write a function named `reverse_file_lines` that accepts two string arguments: `input_file` and `output_file`. The function should read `input_file`, reverse the order of the lines, and write the reversed lines to `output_file`.

### Example
* **Input (Contents of `steps.txt`):**
    ```
    Step 1: Open the door.
    Step 2: Enter the room.
    Step 3: Close the door.
    ```
* **Function Call:** `reverse_file_lines('steps.txt', 'reversed_steps.txt')`
* **Output (Contents of `reversed_steps.txt`):**
    ```
    Step 3: Close the door.
    Step 2: Enter the room.
    Step 1: Open the door.
    ```

**16. Sales Data Aggregator**

Write a function named `summarize_sales` that accepts two string arguments: `input_file` and `output_file`. The `input_file` contains sales records, with one transaction per line in the format `ProductName Quantity` (space-separated). The function should read the file, aggregate the total quantity for each product, and write the summary to the `output_file` in the format `ProductName: TotalQuantity`, sorted alphabetically by product name.

### Example
* **Input (Contents of `sales.txt`):**
    ```
    Apple 5
    Orange 10
    Apple 3
    Banana 7
    Orange 2
    Apple 10
    ```
* **Function Call:** `summarize_sales('sales.txt', 'summary.txt')`
* **Output (Contents of `summary.txt`):**
    ```
    Apple: 18
    Banana: 7
    Orange: 12
    ```

---

**17. Parse Indented List**

Write a function named `parse_indented_list` that accepts two string arguments: `input_file` and `output_file`. The `input_file` contains a list of projects and their tasks, formatted with indentation (two spaces). Lines with no indentation are projects, and lines indented with two spaces are tasks belonging to the preceding project. The function should parse this file and write a summary to `output_file` in the format `ProjectName: X tasks`.

### Example
* **Input (Contents of `projects.txt`):**
    ```
    Website Relaunch
      Design mockups
      Develop homepage
      Write content
    Server Migration
      Backup database
      Update DNS
    Marketing Campaign
    ```
* **Function Call:** `parse_indented_list('projects.txt', 'project_summary.txt')`
* **Output (Contents of `project_summary.txt`):**
    ```
    Website Relaunch: 3 tasks
    Server Migration: 2 tasks
    Marketing Campaign: 0 tasks
    ```

---

**18. File Difference Checker**

Write a function named `compare_files` that accepts three string arguments: `file1`, `file2`, and `output_file`. The function should compare the two input files line by line. It should write a report to `output_file` detailing the first line (1-indexed) where they differ. If the files are identical, it should write "Files are identical." If one file is shorter than the other and the common lines are identical, it should note that.

### Example 1 (Different Content)
* **Input (Contents of `version1.txt`):**
    ```
    Line 1
    Line 2
    Line 3
    ```
* **Input (Contents of `version2.txt`):**
    ```
    Line 1
    Line Two
    Line 3
    ```
* **Function Call:** `compare_files('version1.txt', 'version2.txt', 'diff.txt')`
* **Output (Contents of `diff.txt`):**
    ```
    Files differ at line 2:
    < file1: "Line 2"
    > file2: "Line Two"
    ```

### Example 2 (Different Length)
* **Input (Contents of `version1.txt`):**
    ```
    Line 1
    Line 2
    ```
* **Input (Contents of `version2.txt`):**
    ```
    Line 1
    Line 2
    Line 3
    ```
* **Function Call:** `compare_files('version1.txt', 'version2.txt', 'diff.txt')`
* **Output (Contents of `diff.txt`):**
    ```
    Files are identical up to line 2.
    file2 is longer than file1.
    ```

---

**19. Split File by Marker**

Write a function named `split_by_marker` that accepts two arguments: an `input_file` string and a `marker` string. The function should read the `input_file` and split it into multiple new files every time it encounters a line that *starts with* the `marker`. The new files should be named `part_1.txt`, `part_2.txt`, etc. The marker line itself should not be included in the output files.

### Example
* **Input (Contents of `long_book.txt`):**
    ```
    This is the introduction.
    It is very interesting.
    ==CHAPTER 1==
    This is the first chapter.
    A lot happens here.
    ==CHAPTER 2==
    This is the second chapter.
    The plot thickens.
    ```
* **Function Call:** `split_by_marker('long_book.txt', '==CHAPTER')`
* **Output (New files created):**
    * **`part_1.txt`:**
        ```
        This is the introduction.
        It is very interesting.
        ```
    * **`part_2.txt`:**
        ```
        This is the first chapter.
        A lot happens here.
        ```
    * **`part_3.txt`:**
        ```
        This is the second chapter.
        The plot thickens.
        ```

---

**20. Parse Multi-Line Records**

Write a function named `parse_records` that accepts two string arguments: `input_file` and `output_file`. The `input_file` contains records for different users. Each record starts with a line `USER: username` and is followed by one or more `DATA: somedata` lines. Records are separated by a blank line. The function should parse this file and write a summary to `output_file` in the format `username: X data points`.

### Example
* **Input (Contents of `records.txt`):**
    ```
    USER: alice
    DATA: 101
    DATA: 102
    
    USER: bob
    DATA: 201
    
    USER: charlie
    DATA: 301
    DATA: 302
    DATA: 303
    ```
* **Function Call:** `parse_records('records.txt', 'record_summary.txt')`
* **Output (Contents of `record_summary.txt`):**
    ```
    alice: 2 data points
    bob: 1 data points
    charlie: 3 data points
    ```
