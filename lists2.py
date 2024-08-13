# Qn 6
# Create a function called every_three_nums that has one parameter named start.

# The function should return a list of every third number between start and 100 (inclusive). 
# For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
# If start is greater than 100, the function should return an empty list

def every_three_nums(start):
  if start > 100:
    return []
  else:
    return list(range(start, 101, 3))

print(every_three_nums(91))

# Qn 7
# Create a function named remove_middle which has three parameters named my_list, start, and end.

# The function should return a list where all elements in my_list with an index between start and end (inclusive) have been removed.

# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

def remove_middle(my_list, start, end):
    # print(my_list[:start])
    # print([ my_list[end+1:]])
    amended = my_list[:start] + my_list[end+1:]
    return amended

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# correction: no need to assign to local variable, can direct return statement

# Qn 8
# Create a function named more_frequent_item that has three parameters named my_list, item1, and item2.

# Return either item1 or item2 depending on which item appears more often in my_list.

# If the two items appear the same number of times, return item1.

def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3)) #3
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 2], 2, 3)) #2

# Qn 9 
# Create a function named double_index that has two parameters: 
#     a list named my_list and a single number named index.

# The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.

# If index is not a valid index, the function should return the original list.

# For example, the following code should return [1,2,6,4] 
# because the element at index 2 has been doubled:

# double_index([1, 2, 3, 4], 2)

def double_index(my_list, index):
    #check valid index
    if index >= len(my_list):
        return my_list
    else:
        double = [my_list[index] * 2]
        return my_list[:index] + double + my_list[index + 1:]
    
print(double_index([1, 2, 3, 4], 4)) 
print(double_index([1, 2, 3, 4], 2)) 
print(double_index([3, 8, -10], 2))
