# Qn 6
# Create a function named in_range() that has three parameters 
# named num, lower, and upper.
# The function should return True 
# if num is greater than or equal to lower and less than or equal to upper. 
# Otherwise, return False.

def in_range(num, upper, lower):
  if num >= lower and num <= upper:
    return True
  else:
    return False

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# Qn 7
# Create a function named same_name() that has two parameters 
# named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# Qn 8
# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, 
# make it so your function will return False no matter what number is stored in num.

ef always_false(num):
  if num > 0 or num < 0 or num == 0:
    return False

print(always_false(0)) # False

print(always_false(-5)) # False

print(always_false(90)) # False
