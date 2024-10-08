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

print("--Q2--")
print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

# Qn 3 Count Multi Char X (X is a str with multiple letters, not a singular letter)

def count_multi_char_x(word, x):
    count = 0
    for i in range(len(word) - len(x) + 1):
        if word[i:i + len(x)] == x:
            count += 1
    return count

print("--Q3--")
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

print("--Q4--")
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

print("--Q5--")
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

# Qn 6 
# Write a function called check_for_name that takes two strings 
# as parameters named sentence and name. 
# The function should return True if name appears in sentence in all lowercase letters, 
# all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return False otherwise.

# def check_for_name(sentence, name):
#     # convert both params to same case
#     sentence_lower = sentence.lower()
#     name_lower = name.lower()
#     # using find method instead of manually doing a for loop
#     if sentence_lower.find(name_lower) == -1:
#         return False
#     return True


# Recall! the IN keyword --> returns boolean

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print("--Q6--")
print(check_for_name("My name is Jamie", "Jamie")) # True
print(check_for_name("My name is jamie", "Jamie")) # True
print(check_for_name("My name is JAMIE", "Jamie")) # True
print(check_for_name("My name is JAMeE", "Jamie")) # False
print(check_for_name("My name is Samantha", "Jamie")) # False

# Qn 7
# Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

def every_other_letter(word):
    if word == "" or type(word) == int:
        return "invalid parameter!"
    new_word = ""
    for i in range(0, len(word), 2):
        new_word += word[i]
    return new_word

print("--Q7--")
print(every_other_letter("Coding School"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))
print(every_other_letter(5))

# Q 8

def reverse_string(word):
    reversed_word = ""
    for i in range(1, len(word) + 1):
        reversed_word += word[-i]
    return reversed_word
print("--Q8--")
print(reverse_string("Coding and Progamming"))
print(reverse_string("Hello world!"))

# alt soln
def reverse_string2(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

print(reverse_string2("Coding and Progamming"))
print(reverse_string2("Hello world!"))

# Q 9
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2.  
# we’re going to switch the first letters of each word. 
# Return the two new words as a single string separated by a space.

def make_spoonerism(word1, word2):
    return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

print("--Q9--")
print(make_spoonerism("Jelly", "Bean"))

# Q 10

# Create a function named add_exclamation that has one parameter named word. 
# This function should add exclamation points to the end of word until word is 20 characters long.
# If word is already at least 20 characters long, just return word.

def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

print("--Q10--")
print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))