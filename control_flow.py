# You are given two numbers stored in num1 and num2. 
# If the sum of num1 and num2 is NOT equal to 10, 
# then store True into a variable called not_ten, 
# otherwise store False in not_ten. 

num1 = 6
num2 = 3

# Write your if statement here

if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False

print("Does the sum of the numbers equal 10? " + str(not_ten))