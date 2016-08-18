import bluetooth


class Bluetooth():
    def __init__(self, target_addr, port=1):
        self.target_addr = target_addr
        self.port = port

    def connect(self):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        try:
            self.sock.connect((self.target_addr, self.port))
        except bluetooth.BluetoothError as e:
            raise e

        return True
