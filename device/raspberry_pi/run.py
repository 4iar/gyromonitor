from communication.bluetooth_server import Bluetooth
from sensors import SenseHat
from time import sleep


sensor = SenseHat.SenseHat()

conn = Bluetooth()
conn.orientation = sensor.get_orientation()
conn.listen()

while True:
    sleep(0.5)
    conn.orientation = sensor.get_orientation()
