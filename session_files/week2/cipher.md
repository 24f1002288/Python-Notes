Q1: Building a Caesar Cipher Step-by-StepProblem StatementWrite a Python program that encrypts a predefined 4-letter word using the Caesar Cipher technique. The Caesar Cipher is a simple substitution cipher where each letter in a message is shifted a certain number of places down the alphabet. For this assignment, you will encrypt the word "code" by shifting each letter forward by a key of 3.The process involves manually implementing the logic for each character:Find the position (index) of a character in the alphabet.Add the key to this index to find the new position.Use the modulo operator (%) to ensure the index "wraps around" from 'z' back to 'a'.Find the new character at the new position.Repeat for all characters in the word.Combine the new characters to form the final encrypted message.The assignment is broken down into sequential parts in the "Notes" section to guide you through the implementation.Input/Output SpecificationInput:For the main assignment, all inputs are predefined as variables within the script.alphabet (str) - The string "abcdefghijklmnopqrstuvwxyz".message (str) - The lowercase 4-letter word "code".key (int) - The number of positions to shift, which is 3.Output:A single string representing the fully encrypted message. The program should print intermediate steps for each character as outlined in the notes, followed by the final combined result.Notes / Implementation GuideThis assignment should be completed in order, as each part builds on the previous one. The repetition is intentional to help you master the core logic.Part 0: The SetupFirst, create the variables that will serve as the basis for your program.# --- Part 0: Setup ---
alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "code"
key = 3

# Test your setup
print("Alphabet:", alphabet)
print("Original Message:", message)
print("Key:", key)
Part 1: Encrypting the First CharacterFocus on encrypting just the first character of the message ('c').# --- Part 1: Encrypting the First Character ---
# 1. Get the first character
char1 = message[0]
# 2. Find its index in the alphabet
index1 = alphabet.index(char1)
# 3. Calculate the new, shifted index using the key and modulo 26
new_index1 = (index1 + key) % 26
# 4. Get the new encrypted character from the alphabet
char1_encrypted = alphabet[new_index1]

print("First character encrypted:", char1_encrypted)
Part 2: Encrypting the Remaining CharactersRepeat the exact same logic for the second, third, and fourth characters of the message ('o', 'd', and 'e').# --- Part 2: Encrypting the Rest of the Characters ---

# --- Encrypt the SECOND character ('o') ---
char2 = message[1]
index2 = alphabet.index(char2)
new_index2 = (index2 + key) % 26
char2_encrypted = alphabet[new_index2]
print("Second character encrypted:", char2_encrypted)

# --- Encrypt the THIRD character ('d') ---
char3 = message[2]
index3 = alphabet.index(char3)
new_index3 = (index3 + key) % 26
char3_encrypted = alphabet[new_index3]
print("Third character encrypted:", char3_encrypted)

# --- Encrypt the FOURTH character ('e') ---
char4 = message[3]
index4 = alphabet.index(char4)
new_index4 = (index4 + key) % 26
char4_encrypted = alphabet[new_index4]
print("Fourth character encrypted:", char4_encrypted)
Part 3: Assembling the Final Encrypted MessageYou now have four separate variables holding your encrypted characters. Combine them using string concatenation (+) to form the final result.# --- Part 3: Assembling the Final Message ---
encrypted_message = char1_encrypted + char2_encrypted + char3_encrypted + char4_encrypted

print("---------------------------------")
print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("---------------------------------")
🌟 Bonus Challenge: Make it Interactive!After completing the main task, try modifying your program to take the message and key as input from the user. You will need to use the input() function to get the values and the int() function to convert the key from a string to an integer. Note: this will require you to expand your logic to handle words of different lengths.Sample Case 1 (Main Task)Input:(predefined in code)message = "code"key = 3Expected Output:Alphabet: abcdefghijklmnopqrstuvwxyz
Original Message: code
Key: 3
First character encrypted: f
Second character encrypted: r
Third character encrypted: g
Fourth character encrypted: h
---------------------------------
Original message: code
Encrypted message: frgh
---------------------------------
Sample Case 2 (Bonus Challenge)Input:(user enters the following)Enter a 6-letter lowercase word: pythonEnter a number to use as the key: 5Expected Output:(output may vary based on your implementation)---------------------------------
Original message: python
Encrypted message: ubesrq
---------------------------------
