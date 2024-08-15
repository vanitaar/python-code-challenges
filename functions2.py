# Qn 6
# Write a function named first_three_multiples() that has one parameter named num.

# This function should print the first three multiples of num. Then, it should return the third multiple.

# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

def first_three_multiples(num):
    # print(num * 1)
    # print(num * 2)
    # print(num * 3)
    for i in range(1, 4):
        print(num * i)
    return num * 3

first_three_multiples(0)
first_three_multiples(11)

# Qn 7
# Create a function called tip() that has two parameters named total and percentage.

# This function should 
# return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
    return percentage/100 * total

print(tip(10, 25))
print(tip(0, 100))

# Qn 8
# Write a function named introduction() that has two parameters named first_name and last_name.

# The function should return the 
# last_name, followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))

# Qn 9
# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. 
# Write a function named dog_years() that has two parameters named name and age.
# he function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"

def dog_years(name, age):
    age_in_dog_yrs = age * 7
    return name + ", you are " + str(age_in_dog_yrs) + " years old in dog years"

print(dog_years("Lola", 16))

# Qn 10
# Create a function named lots_of_math(). This function should have four parameters 
# named a, b, c, and d. The function should print 3 lines and return 1 value.

# First, print the sum of a and b.

# Second, print c minus d.

# Third, print the first number printed, multiplied by the second number printed.

# Finally, return the third number printed modulo a.

def lots_of_math(a, b, c, d):
    sum = a + b
    minus = c - d 
    print(sum)
    print(minus)
    print(sum * minus)
    return ((sum * minus) % a)

print(lots_of_math(1, 2, 3, 4))


# EXTRA

# BTS len function --> uses a for loop

def get_length(str):
  # return len(str)
  len = 0
  for char in str:
    len += 1
  return len

# keyword IN AND NOT

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    # if (letter in string_two) and common.count(letter) == 0:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("banana", "cream"))

def reversed(str):
    reversed_str = ""
    for i in range(1, len(str) + 1):
        reversed_str += str[-i]
    return reversed_str
    
print(reversed("AbeSimp"))

  
# -1 0 1 2 3 4 ...
def shift_to_right(str):
    shifted = ""
    for i in range(0, len(str)):
        shifted += str[i-1]
    return shifted
print(shift_to_right("AbeSimp"))