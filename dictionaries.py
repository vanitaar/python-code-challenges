# Q 1 Sum Values

def sum_values(dict):
    total_sum = 0
    for value in dict.values():
        # print(value)
        total_sum += value
    return total_sum

print("--Q1--")        
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))

# Q 2 Sum even keys
# This function should return the sum of the values of all even keys.

def sum_even_keys(dict):
    total_sum = 0
    for key in dict:
        if key % 2 == 0:
            total_sum += dict[key]
    return total_sum

print("--Q2--")  
print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

# Q 3 Add 10
# function should add 10 to every value in the dictionary and 
# return the modified dictionary.

def add_ten(dict):
    for key in dict:
        dict[key] += 10
    return dict

print("--Q3--")
print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

# Q 4
# This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(dict):
    my_list = []
    for value in dict.values():
        if value in dict:
            my_list.append(value)
    return my_list

print("--Q4--")
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))


# Q 5 

def find_max_key(dict):
    # max_key = 0
    max_key = float("-inf")
    # max_value = 0
    max_value = float("-inf")
    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
    
print("--Q5--")    
print(find_max_key({1:100, 2:1, 3:4, 4:10}))
print(find_max_key({"a":100, "b":10, "c":1000}))
print(find_max_key({"a":100, "b":10, "c":-1000}))

# prev soln only woorks for int >= 0
# using float("-inf") in order to initialize them to the lowest possible value.

# Q 6
# a function that creates a new dictionary based on a list of strings. 
# The keys of our dictionary will be every string in our list of strings, while 
# the values will be the length of each of the words in the string list. 

def word_length_dict(strings):
    my_dict = {}
    for string in strings:
        my_dict[string] = len(string)
    return my_dict

print("--Q6--")
print(word_length_dict(["apple", "dog", "cat"]))
print(word_length_dict(["a", ""]))


# Q 7
# Write a function named frequency_dictionary that takes a list of elements named words as a parameter.
# The function should return a dictionary containing the frequency of each element in words.

# def frequency_dictionary(words):
#     freq_dict = {}
#     for word in words:
#         freq_dict[word] = words.count(word)
#     return freq_dict

# alt soln w/o count method - more efficient for larger lists -- O(n) -- only iterates thru list once
# v/s using count in for loop -- O(n^2)
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

print("--Q7--")
print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))

# Q 8

def unique_values(my_dict):
    uniques = []
    for value in my_dict.values():
        if value not in uniques:
            uniques.append(value)
    return len(uniques)

print("--Q8--")
print(unique_values({0:3, 1:3, 4:3, 5:3}))
print(unique_values({0:3, 1:1, 4:1, 5:3}))

# Q 9
# This function accepts a dictionary where the keys are last names 
# and the values are lists of first names of people who have that last name. 
# We need to calculate the number of people who have the same first letter in their last name

def count_same_last_name_initial(names):
    initials = {}
    for last_name in names:
        initial_letter = last_name[0]
        if initial_letter not in initials:
            initials[initial_letter] = 0
        initials[initial_letter] += len(names[last_name])
    return initials

print("--Q9--")
print(count_same_last_name_initial({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_same_last_name_initial({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))