# The map() function is a built-in function in Python 
# that applies a given function to each item in an iterable 
# (like a list, tuple, or string) 
# and returns a new iterable as a result.

# basic syntax:
#  map(function, iterable, [iterable2, iterable3, ...]) 

def double(x): 
    return x * 2 

numbers = [1, 2, 3, 4, 5] 

doubled_numbers = map(double, numbers) 

print(doubled_numbers) # <map object at 0x000001623E000190>
print(list(doubled_numbers)) # [2, 4, 6, 8, 10]


# Converting strings to integers 

str_nums = ['1', '2', '3', '4', '5'] 

int_nums = list(map(int, str_nums)) 

print(int_nums)  # [1, 2, 3, 4, 5] 

# Finding the length of strings 

words = ['apple', 'banana', 'cherry'] 

word_lengths = list(map(len, words)) 

print(word_lengths)  # [5, 6, 6] 

# Using w lambda fn

numbers_to_subtract = [1, 2, 3, 4, 5] 

substracted = list(map(lambda x: x -1, numbers_to_subtract)) 

print(substracted)  # [0, 1, 2, 3, 4]

# Using multiple iterables

list1 = [1, 2, 3] 

list2 = [10, 20, 30] 

result = list(map(lambda x, y: x + y, list1, list2)) 

print(result)  # [11, 22, 33]

