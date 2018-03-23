import random
class Drought_sensor:
    def __init__(self):
        self.s0_val = 0
        self.s1_val = 0
        self.s2_val = 0
    
    def get_data(self):
        for i in range(0,3):
            self.set_sensor_val(i, self.plant_data())
        return True
    
    def send_data(self):
        print("s0\ts1\ts2")
        print(str(self.get_sensor_val(0)) + "\t" + str(self.get_sensor_val(1)) + "\t" \
            + str(self.get_sensor_val(2)))    
        return True
    
    def modulate(self):
        print('not yet implemented')

    def calibrate(self):
        print('not implemented')
    
    def get_sensor_val(self, sensor):
        if sensor == 0:
            return self.s0_val
        elif sensor == 1:
            return self.s1_val
        elif sensor == 2:
            return self.s2_val
        else:
            print("sensor does not exit")

    def set_sensor_val(self, sensor, value):
        if sensor == 0:
            self.s0_val = value
        elif sensor == 1:
            self.s1_val = value
        elif sensor == 2:
            self.s2_val = value
        else:
            print("sensor does not exit")

    def plant_data(self):
        return random.randint(0,100)
