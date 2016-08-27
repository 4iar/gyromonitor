from communication.bluetooth_server import Bluetooth
from sensors import SenseHat
from time import sleep
import threading


sensor = SenseHat.SenseHat()

conn = Bluetooth()
conn.orientation = sensor.get_orientation()

t = threading.Thread(target=conn.listen)
t.start()

while True:
    sleep(0.5)
    conn.orientation = sensor.get_orientation()
