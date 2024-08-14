# Qn 6 
# Create a function named larger_sum() that 
# takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. 
# If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for n in lst1:
        sum1 += n
    for x in lst2:
        sum2 += x
    
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
    
# ALT SOLN USING SUM FUNCTION DIRECTLY
# def larger_sum(lst1, lst2):
    # if sum(lst1) >= sum(lst2):
    #     return lst1
    # else:
    #     return lst2
    
    
print(larger_sum([1, 9, 5], [2, 3, 7]))

# Qn 7 
# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. 
# When this happens, the function should return the sum. 
# If the sum of all of the elements is never greater than 9000, 
# the function should return total sum of all the elements. 
# If the list is empty, the function should return 0.

def over_nine_thousand(lst):
    sum = 0
    if len(lst) == 0:
        return 0
    i = 0
    while i < len(lst) and sum < 9000:
        sum += lst[i]
        i += 1
    return sum

# ALT SOLN USING IF AND BREAK
# def over_nine_thousand(lst):
    # for num in lst:
    #     sum += num 
    #     if sum >= 9000:
    #         break
    # return sum
    
print(over_nine_thousand([8000, 1000, 200]))  # Output: 9000
print(over_nine_thousand([8000, 1000, 200, 300]))  # Output: 9000
print(over_nine_thousand([1000, 2000, 3000, 4000]))  # Output: 10000
print(over_nine_thousand([]))  # Output: 0
print(over_nine_thousand([8000, 900, 120, 5000])) # Output: 9020