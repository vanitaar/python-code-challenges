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