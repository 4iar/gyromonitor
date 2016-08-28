from sense_hat import SenseHat as SenseHatDriver


class SenseHat():
    def __init__(self):
        self.sense = SenseHatDriver()
        self.sense.set_imu_config(False, True, False)  # we only need the gyroscope

    def get_orientation(self):
        x, y, z = self.sense.get_accelerometer_raw().values()
        x = round(x, 0)
        y = round(y, 0)
        if x == -1:
            return 180
        elif y == 1:
            return 90
        elif y == -1:
            return 270
        else:
            return 0
