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