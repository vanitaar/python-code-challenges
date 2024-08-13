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

def always_false(num):
  if num > 0 or num < 0 or num == 0:
    return False

print(always_false(0)) # False

print(always_false(-5)) # False

print(always_false(90)) # False


# Qn 9
# Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!". 
# If rating is between 5 and 9, return "This one was fun.". 
# If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

print(movie_review(9))
# "Outstanding!"
print(movie_review(4))
# "Avoid at all costs!"
print(movie_review(6))
# "This one was fun."

# Qn 10
# Create a function called max_num() that has three parameters named num1, num2, and num3.
# The function should return the largest of these three numbers. 
# If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1, num2, num3):
  num_max = max(num1, num2, num3)
  if num_max == num1 and num1 == num2 or num1 == num3:
    return "It's a tie!"
  elif num_max == num2 and num2 == num1 or num2 == num3:
    return "It's a tie!"
  elif num_max == num3 and num3 == num1 or num3 == num2:
    return "It's a tie!" 
  else:
    return num_max

print(max_num(-10, 0, 10))
# 10
print(max_num(-10, 5, -30))
# 5
print(max_num(-5, -10, -10))
# "It's a tie!" should be -5

### suggested answer
def max_num2(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"

print(max_num2(-10, 5, 5)) #It's a tie!
print(max_num2(-5, -10, -10))# -5