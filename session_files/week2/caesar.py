string = "abcdt"
delta = 4

## we need to know index of each character

# a b c d e....
# 0 1 2 3 4....


a = "x"
uncrypted = "hardik"
index = string.index(a)
print("index:",index)

for i in range(0,26):
    if string[i] == a:
        print(i)

## when we know the index:

    # delta = 4
    # use mod (%)
delta = 4
capture_index = (string.index(a) + delta) % 26
new_char = string[capture_index]

    ## have to iterate over all the characters and "change" them.
    
    ## use for loop

## new encryted string

string = "abcdefghijklmnopqrstuvwxyz"
delta = 4
uncrypted = "hardik"

encrypted = ''
for char in uncrypted:
    index = string.index(char)
    capture_index = (index + delta)%26
    new_char = string[capture_index]
    encrypted = encrypted + new_char

print(encrypted)


# how do we decrypt this encryted message




