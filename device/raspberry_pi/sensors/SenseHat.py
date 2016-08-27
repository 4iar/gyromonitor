from sense_hat import SenseHat as SenseHatDriver

class SenseHat():
    def __init__(self):
        self.sense = SenseHatDriver()

    def get_orientation(self):
        return self.sense.get_orientation()['yaw']
