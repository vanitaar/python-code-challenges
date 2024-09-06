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

# class DriveBot: 
#     def __init__(self):
#         print("robot created")
#         self.motor_speed = 0
#         self.direction = 0
#         self.sensor_range = 0
    
#     def control_bot(self, new_speed, new_dir):
#         self.motor_speed = new_speed
#         self.direction = new_dir
#         print("speed and direction changed")

#     def adjust_sensor(self, new_sensor_range):
#         self.sensor_range = new_sensor_range
#         print("sensor range adjusted")        
        
# robot_1 = DriveBot()

# robot_1.control_bot(10, 180)
# robot_1.adjust_sensor(20)

# print(robot_1.motor_speed)
# print(robot_1.direction)
# print(robot_1.sensor_range)

# 3 Enhance constructor

class DriveBot: 
    # 4 add class variables
    all_disabled = False
    latitude = -999999
    longitude = -999999
    
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        print("robot created")
    
    def control_bot(self, new_speed, new_dir):
        self.motor_speed = new_speed
        self.direction = new_dir
        print("speed and direction changed")

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range
        print("sensor range adjusted")  
        
robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

robot_3 = DriveBot(20, 60, 10)

DriveBot.all_disabled = True
DriveBot.latitude = -50.0
DriveBot.longitude = 50.0

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

# ## Different ways to use constructor:
# # sensor_range defaults to 10
# test_bot_1 = DriveBot(10, 270) 
# # direction defaults to 180
# test_bot_2 = DriveBot(sensor_range = 20, motor_speed = 45) 
# # direction defaults to 180 and sensor_range defaults to 10
# test_bot_3 = DriveBot(50) 
# # all default values are used
# test_bot_4 = DriveBot() 