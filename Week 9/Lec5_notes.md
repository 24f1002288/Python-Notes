# Caesar Cipher Implementation in Python

This document explores the Caesar Cipher encryption technique and its implementation using Python, focusing on string manipulation, dictionary creation, and file handling.

## Key Topics

### 1. Introduction to Caesar Cipher

*   **Concept:** The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
*   **Purpose:** To encrypt text, making it difficult to read without knowing the shift key.
*   **Example (Shift by 3):**
    *   `a` becomes `d`
    *   `b` becomes `e`
    *   `h` becomes `k`
*   **Wrap-around:** When shifting letters near the end of the alphabet (e.g., `z`), the alphabet "wraps around" to the beginning.
    *   For a shift of 3:
        *   `w` becomes `z`
        *   `x` becomes `a`
        *   `y` becomes `b`
        *   `z` becomes `c`

### 2. Preparing Input Text for Encryption

*   **Simplification:** For this implementation, the input text is pre-processed to remove spaces and other unwanted characters, and all letters are converted to lowercase.
*   **Rationale:** This simplifies the encryption logic as only lowercase English alphabets need to be handled.
*   **Example:** A phrase like "Pick up the stick" becomes "pickupthestick". While difficult for a human to read, the structure is still understandable.

### 3. Building the Caesar Cipher Dictionary

To efficiently encrypt characters, a dictionary mapping each original character to its encrypted counterpart is created.

#### 3.1. Generating the Alphabet

*   **`import string` module:** Python's `string` module provides useful constants, including `ascii_lowercase`.
*   **`string.ascii_lowercase`:** This constant is a string containing all lowercase English letters: `'abcdefghijklmnopqrstuvwxyz'`.
*   **Converting to a List:** For easier indexing and manipulation (like accessing the 20th letter), it's best to convert this string into a list of characters.

**Code Example 1: Creating the alphabet list**

```python
import string

# Get all lowercase English letters as a string
alphabet_string = string.ascii_lowercase
print(f"Alphabet string: {alphabet_string}")

# Convert the string to a list of characters for easier indexing
alphabet_list = list(alphabet_string)
print(f"Alphabet list: {alphabet_list}")

# Accessing elements (e.g., the first letter 'a')
print(f"First letter: {alphabet_list[0]}") # Output: a
# Accessing elements (e.g., the letter at index 24, which is 'y')
print(f"Letter at index 24: {alphabet_list[24]}") # Output: y
```

#### 3.2. Implementing the Shift Logic

*   **Modulo Operator (`%`):** This operator is crucial for handling the wrap-around effect. When we shift a letter's index, we use the modulo operator with `26` (the number of letters in the alphabet) to ensure the new index stays within the valid range `0-25`.

**Code Example 2: Understanding Modulo for wrap-around**

```python
alphabet_list = list(string.ascii_lowercase) # 'a' at index 0, 'z' at index 25

# Example: Shift 'y' (index 24) by 3
original_index_y = 24
shift = 3
new_index_y = (original_index_y + shift) % 26
print(f"New index for 'y' shifted by 3: {new_index_y}") # Output: 1 (which corresponds to 'b')
print(f"Encrypted 'y': {alphabet_list[new_index_y]}") # Output: b

# Example: Shift 'z' (index 25) by 3
original_index_z = 25
new_index_z = (original_index_z + shift) % 26
print(f"New index for 'z' shifted by 3: {new_index_z}") # Output: 2 (which corresponds to 'c')
print(f"Encrypted 'z': {alphabet_list[new_index_z]}") # Output: c
```

#### 3.3. Creating the Dictionary

*   A loop iterates through each character in the alphabet list.
*   For each character, its original index is determined.
*   The shifted index is calculated using `(original_index + shift) % 26`.
*   The original character is then mapped to the character at the new, shifted index in the dictionary.

**Code Example 3: Creating the Caesar Cipher dictionary**

```python
import string

def create_caesar_dictionary(shift_amount):
    """
    Creates a dictionary for Caesar Cipher encryption with a given shift.
    Maps original lowercase letters to their shifted counterparts.
    """
    alphabet_list = list(string.ascii_lowercase)
    caesar_dict = {}

    for i in range(len(alphabet_list)):
        original_char = alphabet_list[i]
        shifted_index = (i + shift_amount) % len(alphabet_list)
        encrypted_char = alphabet_list[shifted_index]
        caesar_dict[original_char] = encrypted_char
    
    return caesar_dict

# Create a dictionary for a shift of 3
encryption_map = create_caesar_dictionary(3)

# Print some mappings to verify
print(f"Encryption map (a -> d): {encryption_map['a']}") # Output: d
print(f"Encryption map (z -> c): {encryption_map['z']}") # Output: c
print(f"Encryption map (y -> b): {encryption_map['y']}") # Output: b
```

### 4. File Handling in Python

To encrypt an entire text file, Python's file handling capabilities are used.

#### 4.1. Opening Files

*   **`open()` function:** Used to open a file. It takes the file path and the mode as arguments.
*   **Modes:**
    *   `'r'` (read mode): Opens a file for reading. The file must exist.
    *   `'w'` (write mode): Opens a file for writing. If the file exists, its content is truncated (emptied). If it doesn't exist, a new file is created.

**Code Example 4: Opening files**

```python
# To open an existing file named 'input.txt' for reading
# file_input = open('input.txt', 'r') 

# To create/open a file named 'output.txt' for writing
# file_output = open('output.txt', 'w') 
```

#### 4.2. Reading and Writing Character by Character

*   **`file.read(1)`:** Reads exactly one character from the file.
    *   When the end of the file is reached, `file.read(1)` returns an empty string (`''`). This is a crucial condition for knowing when to stop reading.
*   **`file.write(character)`:** Writes the given character (or string) to the file.

#### 4.3. Closing Files

*   **`file.close()`:** It's essential to close files after use to free up system resources and ensure all buffered writes are flushed to the disk.

### 5. The Complete Encryption Script

Combining the Caesar Cipher dictionary with file handling, a script can encrypt an entire input file and write the encrypted content to an output file.

**Code Example 5: Full Encryption Script (`caesar.py`)**

```python
import string

def create_caesar_dictionary(shift_amount):
    """
    Creates a dictionary for Caesar Cipher encryption with a given shift.
    Maps original lowercase letters to their shifted counterparts.
    """
    alphabet_list = list(string.ascii_lowercase)
    caesar_dict = {}

    for i in range(len(alphabet_list)):
        original_char = alphabet_list[i]
        shifted_index = (i + shift_amount) % len(alphabet_list)
        encrypted_char = alphabet_list[shifted_index]
        caesar_dict[original_char] = encrypted_char
    
    return caesar_dict

def encrypt_file_caesar(input_filepath, output_filepath, shift_amount=3):
    """
    Encrypts a file using the Caesar Cipher.
    Assumes input file contains only lowercase English letters (no spaces/punctuation).
    """
    encryption_map = create_caesar_dictionary(shift_amount)

    try:
        # Open the input file for reading
        # 'sherlock.txt' is an example filename mentioned in the lecture
        input_file = open(input_filepath, 'r') 
        
        # Open the output file for writing
        output_file = open(output_filepath, 'w')

        # Read the first character
        current_char = input_file.read(1)

        # Loop until the end of the file is reached
        while current_char != '':
            # Look up the encrypted character in the dictionary
            # If the character is not in the dictionary (e.g., a number or symbol),
            # it will remain unchanged for simplicity in this example.
            # However, for the provided input, all characters are lowercase alphabets.
            encrypted_char = encryption_map.get(current_char, current_char)
            
            # Write the encrypted character to the output file
            output_file.write(encrypted_char)
            
            # Read the next character for the next iteration
            current_char = input_file.read(1)

        print(f"File '{input_filepath}' encrypted successfully to '{output_filepath}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure files are closed even if an error occurs
        if 'input_file' in locals() and not input_file.closed:
            input_file.close()
        if 'output_file' in locals() and not output_file.closed:
            output_file.close()

# Example Usage:
# 1. Create a dummy 'sherlock.txt' for testing:
#    with open('sherlock.txt', 'w') as f:
#        f.write("chapteronepickupthestick") 

# 2. Run the encryption:
# encrypt_file_caesar('sherlock.txt', 'encrypted_sherlock.txt', 3)
```

**Explanation of the Encryption Loop:**

1.  **`current_char = input_file.read(1)`:** Reads the *very first* character from the input file.
2.  **`while current_char != '':`:** This loop continues as long as `current_char` is not an empty string. An empty string signifies the End Of File (EOF).
3.  **`encrypted_char = encryption_map.get(current_char, current_char)`:** This line encrypts the `current_char`.
    *   `encryption_map.get(key, default_value)` is used. If `current_char` is a key in the `encryption_map` (i.e., a lowercase letter), its encrypted value is retrieved.
    *   If `current_char` is *not* a key (e.g., if we were handling spaces or punctuation, which are removed in this specific context), `current_char` itself is used as the default value, meaning non-alphabetical characters would pass through unchanged.
4.  **`output_file.write(encrypted_char)`:** The (potentially) encrypted character is written to the output file.
5.  **`current_char = input_file.read(1)`:** This is crucial! It reads the *next* character from the input file. This ensures the loop processes all characters one by one and eventually hits the EOF condition to terminate.

### 6. Verifying Encryption

*   After running the script, two files will exist: the original input file and the new encrypted output file.
*   The sizes of the files should be identical if only character-for-character substitution occurred.
*   Opening the encrypted file will show a jumbled sequence of letters, demonstrating the successful encryption. For example, `chapter` becomes `fkdswhu`.

### 7. Decryption (Homework / Reverse Engineering)

*   **Concept:** To decrypt a Caesar Cipher, the process is reversed. If the original encryption shifted letters forward by 3, decryption involves shifting letters backward by 3.
*   **Implementation:** This would involve creating a *new* decryption dictionary where `d` maps back to `a`, `e` to `b`, and `c` to `z`. This can be achieved by shifting indices by `-3` (or `+23`, which is `26 - 3`) using the modulo operator.
*   **Task:** Write a separate script or modify the existing one to take the `encrypted_sherlock.txt` as input and produce the original `sherlock.txt` content as output.

### 8. Beyond Caesar Cipher: Cryptanalysis

*   The Caesar Cipher is very basic and easily broken.
*   **Cryptanalysis:** The study of methods for obtaining the meaning of encrypted information without access to the secret key.
*   Future topics will delve into more sophisticated encryption techniques and how they are analyzed.

---

## Summary

The Caesar Cipher is an introductory encryption method that involves shifting letters in the alphabet. Implementing it in Python requires leveraging the `string` module for alphabet generation, dictionaries for mapping original to encrypted characters, and file handling operations (`open()`, `read(1)`, `write()`, `close()`) for processing entire text files. The modulo operator (`%`) is key for handling the wrap-around effect of the alphabet.

## Important Tips

*   **Practice with Interactive Python:** Use the Python interpreter (type `python` or `ipython` in your terminal) to test small code snippets like `string.ascii_lowercase` or how the modulo operator works. This helps understand individual components before integrating them into a larger script.
*   **Code Step-by-Step:** Don't try to write the entire program at once. Build it piece by piece (e.g., first create the dictionary, then add file reading, then file writing).
*   **Pause and Code:** When following along with explanations, pause, type the code yourself, and ensure it runs without errors. Typing reinforces understanding.
*   **Error Checking:** Pay attention to file paths, correct file modes (`'r'` vs. `'w'`), and the logic of your loops, especially the end-of-file condition (`while char != ''`).
*   **Homework:** Attempting the decryption task is an excellent way to solidify your understanding of the Caesar Cipher and file handling. It reinforces the concepts by asking you to apply them in reverse.
*   **File Resource Management:** Always remember to `close()` files after you are done with them to prevent resource leaks and data corruption. Using `try...finally` blocks or `with open(...)` statements (not explicitly covered here but good practice) can help ensure files are closed automatically.