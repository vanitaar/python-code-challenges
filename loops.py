# Qn 1
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
    return count
        
    
print(divisible_by_ten([20, 25, 30, 35, 40]))

# Qn 2
# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. 
# Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))

# Qn 3
# Write a function called delete_starting_evens() that has a parameter named my_list.

# The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.

# For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

def delete_starting_evens(my_list):
    # for num in my_list:
    #     print("start")
    #     if num % 2 == 0:
    #         my_list.pop(0)
    #         print("popped")
    while my_list and my_list[0] % 2 == 0:
        my_list.pop(0)
    return my_list    
        
#ALT SOLN
# def delete_starting_evens(my_list):
#   while (len(my_list) > 0 and my_list[0] % 2 == 0):
#     my_list = my_list[1:]
#   return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
print(delete_starting_evens([]))

# Qn 4
# Create a function named odd_indices() that has one parameter named my_list.

# The function should create a new empty list and 
# add every element from my_list that has an odd index. 
# The function should then return this new list.

# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

def odd_indices(my_list):
    #list comprehension
    new_list = [my_list[i] for i in range(1, len(my_list), 2)]
    # use range(start at 1, stop b4 len(my_list), step 2)
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Qn 5
# Create a function named exponents() that takes two lists as parameters named bases and powers. 
# Return a new list containing every number in bases raised to every number in powers.

def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return new_list

print(exponents([2, 3, 4], [1, 2, 3]))

# Bonus Qn 
#Extract odd numbers into separate list
def odd_numbers(my_list):
    #list comprehension
    odd_list = [num for num in my_list if (num % 2 != 0)]
    # odd_list = []
    # for num in my_list:
    #     if num % 2 != 0:
    #         odd_list.append(num)
    return odd_list

print(odd_numbers([4, 3, 7, 10, 11, -2]))