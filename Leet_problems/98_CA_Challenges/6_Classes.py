class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


test_bot = DriveBot()
test_bot.motor_speed = 30
test_bot.direction = 90
test_bot.sensor_range = 25

print(test_bot.motor_speed)
test_bot.control_bot(10, 1000)
print(test_bot.motor_speed)
print(test_bot.direction)

robot_2 = DriveBot(35, 75, 25)
print(robot_2.motor_speed)

robot_3 = DriveBot(20, 60, 10)
DriveBot.latitude = -50
DriveBot.longitude = 50
DriveBot.all_disabled = True

