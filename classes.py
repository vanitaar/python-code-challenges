# 1 Setup Bot

# class DriveBot: 
#     def __init__(self):
#         print("robot created")
#         self.motor_speed = 0
#         self.direction = 0
#         self.sensor_range = 0

# test_bot = DriveBot()
# test_bot.motor_speed = 5
# test_bot.direction = 90
# test_bot.sensor_range = 10

# print(test_bot.motor_speed)
# print(test_bot.direction)
# print(test_bot.sensor_range)

# 2 Add Bot logic

class DriveBot: 
    def __init__(self):
        print("robot created")
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    def control_bot(self, new_speed, new_dir):
        self.motor_speed = new_speed
        self.direction = new_dir
        print("speed and direction changed")

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
        print("sensor range adjusted")        
        
robot_1 = DriveBot()

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)