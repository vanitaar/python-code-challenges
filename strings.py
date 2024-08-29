# 1 Count Unique Letters

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

# 2 Count X

def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))