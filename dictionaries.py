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
    max_key = 0
    max_value = 0
    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
    
print("--Q5--")    
print(find_max_key({1:100, 2:1, 3:4, 4:10}))
print(find_max_key({"a":100, "b":10, "c":1000}))