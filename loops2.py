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


# Qn 8
# Create a function named max_num() that takes 
# a list of numbers named nums as a parameter.

# The function should return the largest number in nums

def max_num(nums):
    # return max(nums)
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max

print(max_num([50, -10, 0, 75, 20]))

# Qn 9
# Write a function named same_values() that 
# takes two lists of numbers of equal size as parameters.

# The function should return a *list of the indices* 
# where the values were equal in lst1 and lst2.

def same_values(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Invalid inputs: list length not same"
    
    indices = []
        
    for i in range(0, len(lst1)):
            if lst1[i] == lst2[i]:
                indices.append(i)
    return indices

print(same_values([1, 2, 3], [4, 5, 6])) #[]
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])) #[0, 2, 3]
print(same_values([5, 1, -10], [5, 10, -10, 3, 5])) #"Invalid..."

# Qn 10 
# Create a function named reversed_list() that 
# takes two lists of the same size as parameters named lst1 and lst2.

# The function should return True if lst1 is the same as lst2 reversed. 
# The function should return False otherwise.

# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
    if len(lst1) != len(lst2):
        return "Invalid inputs: list length not same"
    
    for i in range(len(lst1)):
        if lst1[i] != lst2[-(i+1)]:
            return False
    return True

# cannot do the following as will return True the instance element matches
# BUT we want ALL to match --> then true, if sth no match --> false else i.e. all match True
#   for i in range(len(lst1)):
#       if lst1[i] == lst2[-(i+1)]:
#           return True
#     return False

print(reversed_list([1, 2, 3], [3, 2, 1]))  # Output: True
print(reversed_list([1, 2, 3], [1, 2, 3]))  # Output: False
print(reversed_list([1, 5, 3], [3, 2, 1])) # Output: False
print(reversed_list([1, 2, 3], [3, 2, 1, 0]))  # Output: Invalid inputs: list length not same


# nested lists, loops, list comprehension

# if __name__ == '__main__':
#     records = []
#     scores = []
#     names = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
#         scores.append(score)
    
#     # print(records)
#     # print(scores)
#     min_num = min(scores)
#     scores = [num for num in scores if num != min_num]
#     # print(scores)
#     second_min = min(scores)
    
#     for student in records:
#         if student[1] == second_min:
#             names.append(student[0])
#     # names = sorted(names)
#     names.sort()
#     for name in names:
#         print(name)

# #######
# if __name__ == '__main__':
#     records = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
    
#     scores = [record[1] for record in records]
#     min_num = min(scores)
#     second_min = min(score for score in scores if score != min_num)
    
#     names = sorted([record[0] for record in records if record[1] == second_min])
    
#     for name in names:
#         print(name)


# using set
# colors = []
# for color in thread_sold_split:
#     if color not in colors:
#         colors.append(color)

# colors = list(set(thread_sold_split))

## MATCH-CASE STATEMENTS
# efficient alternative to if-elif-else statements
# check for different conditions on Python objects like lists, tuples, and strings.

user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  