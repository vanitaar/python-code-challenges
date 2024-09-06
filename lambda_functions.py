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