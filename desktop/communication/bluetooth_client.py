import bluetooth


class Bluetooth():
    def __init__(self, target_addr, port=1):
        self.target_addr = target_addr
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        try:
            self.sock.connect((self.target_addr, self.port))
        except bluetooth.BluetoothError as e:
            raise e

        return True

    def disconnect(self):
        self.sock.close()

    def get_orientation(self):
        if not self.sock:
            print("""
            connection not established:
            establish a connection before polling
            """)
            return

        self.sock.send('GET_ORIENTATION')

        orientation = int(self.sock.recv(1024))


        if orientation in [0, 90, 180, 270]:
            return orientation
        else:
            print("got invalid orientation: {}".format(orientation))
