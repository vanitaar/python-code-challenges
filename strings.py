# Qn 1 Count Unique Letters

def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    uniques = []
    for char in word:
        if char in letters and char not in uniques:
            uniques.append(char)
    return len(uniques)
    
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))

# alt sol
def unique_english_letters2(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques

# Qn 2 Count X

def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

# Qn 3 Count Multi Char X (X is a str with multiple letters, not a singular letter)

def count_multi_char_x(word, x):
    count = 0
    for i in range(len(word) - len(x) + 1):
        if word[i:i + len(x)] == x:
            count += 1
    return count

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))

# alt soln - more concised & optimized using count method

def count_multi_char_x_2(word, x):
    return word.count(x)

print(count_multi_char_x_2("mississippi", "iss"))
print(count_multi_char_x_2("apple", "pp"))
