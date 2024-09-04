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

# another way - split method

# def count_multi_char_x(word, x):
#   splits = word.split(x)
#   return(len(splits)-1)

# Q 4 Substring Between
# """
# Write a function named substring_between_letters that 
# takes a string named word, a single character named start, and another character named end.
# This function should return the substring between the first occurrence of start and end in word. 
# If start or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".
# """

def substr_btw_letters(word, start, end):
    idx_start = word.find(start)
    idx_end = word.find(end)
    if idx_start == -1 or idx_end == -1:
        return word
    # return idx_start, idx_end
    return word[idx_start + 1: idx_end]


print(substr_btw_letters("apple", "p", "e")) # pl
print(substr_btw_letters("apple", "p", "c")) # apple

# Q 5 
# Create a function called x_length_words that takes 
# a string named sentence and an integer named x as parameters. 
# This function should return True 
# if every word in sentence has a length greater than or equal to x.

def x_length_words(sentence, x):
    words = sentence.split(" ")
    # return words
    for word in words:
        if len(word) < x:
            return False
    return True


print(x_length_words("i like apples", 2)) # False
print(x_length_words("he likes apples", 2)) # True
print(x_length_words("this is a sentence", 1)) # True
print(x_length_words("randomly worded sentence", 8)) # False

# BONUS: if have punctuations in sentence? --> affects len(word)

def x_length_words(sentence, x):
    words = sentence.split(" ")
    # return words
    # cleaned_words = []
    for word in words:
    # filter out non-alphanumeric characters using built-in python method
        filtered_chars = filter(str.isalnum, word)
        cleaned_word = ''.join(filtered_chars)
        # cleaned_words.append(cleaned_word)
        if len(cleaned_word) < x:
            return False
    return True
    # return cleaned_words

print(x_length_words("i like apples.", 2)) # False
print(x_length_words("he likes apples.", 2)) # True
print(x_length_words("this is a, sentence.", 1)) # True
print(x_length_words("randomly worded sentence.", 8)) # False

