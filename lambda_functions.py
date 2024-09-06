# Lambda functions, also known as ANONYMOUS functions, are SMALL, INLINE functions 
# that can have any number of arguments but ONLY ONE EXPRESSION. They are 
# defined using the lambda keyword and are typically used for short, simple operations.


# Regular function 
def square(x): 
    return x ** 2 

# Lambda function 
square_lambda = lambda x: x ** 2 

# --> more concise using this basic syntax :-
# lambda [arguments]: [expression] 

print(square_lambda(7)) # 49

add = lambda a, b: a + b 

print(add(3, 5)) # 8

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Alice")) # Hello, Alice!

"""Lambda functions are most commonly used as arguments to higher-order functions 
such as map(), filter(), and sorted(). 
Higher-order functions are functions that can accept other functions, 
such as lambda functions, as arguments."""

# Map function

numbers_to_square = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers_to_square)) 

print(squared) # [1, 4, 9, 16, 25]

# Filter function

numbers_to_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers_to_filter)) # [2, 4, 6, 8, 10]

print(even_numbers) 

# Sorted function
# In this case, the lambda function lambda x: x[2] is used as the key for sorting. 
# It tells the sorted() function to use the third element (index 2) of each tuple for comparison. 
# As a result, the list of students is sorted based on their age 
# (the third element in each tuple).

students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 

# sort by age 
sorted_students = sorted(students, key=lambda x: x[2]) 

print(sorted_students) # [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)]

"""
BEST TO USE lambda functions when:

You need a simple function for a short period.

You’re passing a simple function as an argument to higher-order functions.

AVOID lambda functions when:

The operation is complex or requires multiple expressions.

You need to reuse the function multiple times (define a regular function instead).
"""
