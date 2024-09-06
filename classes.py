# 1 Setup Bot

class DriveBot: 
    def __init__(self):
        print(f"{self} created")
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0


test_bot = DriveBot()
test_bot.motor_speed = 5
test_bot.direction = 90
test_bot.sensor_range = 10

print(test_bot.motor_speed)
print(test_bot.direction)
print(test_bot.sensor_range)

