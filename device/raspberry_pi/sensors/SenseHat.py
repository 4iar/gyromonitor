from sense_hat import SenseHat

class SenseHat():
    def __init__(self):
        self.sense = SenseHat()

    def get_orientation(self):
        return self.sense.get_orientation()['yaw']
