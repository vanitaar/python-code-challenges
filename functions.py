# Qn 1
# Write a function named tenth_power() that has one parameter named num.

# The function should return num raised to the 10th power.

def tenth_power(num):
    return num ** 10

print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))


# Qn 2
# Write a function named square_root() that has one parameter named num.
# And return the square root of num

def square_root(num):
    return num ** (1/2)

print(square_root(16))
print(square_root(100))

# Qn 3
# Create a function called win_percentage() that takes two parameters 
# named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

def win_percentage(wins, losses):
    # return (wins / (wins + losses)) * 100
    total_games = wins + losses
    if total_games == 0:
        return 0
    ratio_won = wins / total_games
    return ratio_won * 100

print(win_percentage(5, 5))
print(win_percentage(10, 0))
print(win_percentage(0, 0))


# Qn 4
# Write a function named average() that has two parameters 
# named num1 and num2.
# The function should return the average of these two numbers.

def average(num1, num2):
    sum = num1 + num2
    return sum / 2

print(average(1, -1))
print(average(1, 100))

# Qn 5
# Write a function named remainder() that has 
# two parameters named num1 and num2.
# The function should return 
# the remainder of twice num1 divided by half of num2.

def remainder(num1, num2):
    return (2*num1) % (num2/2)

print(remainder(15, 14))
print(remainder(9, 6))