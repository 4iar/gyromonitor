# placeholder imports
from communication.bluetooth_client import Bluetooth
from orientation.linux import Monitor
from time import sleep

# begin talking to the pi
# poll for curr orientation


monitor = Monitor()
target_addr = input('bd_addr: ')
conn = Bluetooth(target_addr)
conn.connect()

prev_orientation = conn.get_orientation()
while True:
    sleep(0.5)
    orientation = conn.get_orientation()
    if orientation != prev_orientation:
        Monitor.change_orientation(orientation)
        prev_orientation = orientation



