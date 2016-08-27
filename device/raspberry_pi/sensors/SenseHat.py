from sense_hat import SenseHat as SenseHatDriver

class SenseHat():
    def __init__(self):
        self.sense = SenseHatDriver()
        self.sense.set_imu_config(False, True, False)  # we only need the gyroscope

    def get_orientation(self):
        raw_orientation = self.sense.get_orientation()['yaw']

        for eps in [10, 25, 90]:
            orientation = self.round_orientation(raw_orientation, eps)
            if orientation:
                return orientation

    def round_orientation(self, raw_orientation, epsilon):
        for o in [0, 90, 180, 270]:
            if epsilon >= abs(o - raw_orientation) >= 0:
                return o

