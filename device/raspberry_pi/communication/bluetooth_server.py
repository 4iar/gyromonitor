import bluetooth


class Bluetooth():
    def __init__(self, orientation=0):
        self.orientation = orientation

    def listen(self):
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        port = 1
        server_sock.bind(("", port))
        server_sock.listen(1)

        while True:
            client_sock, address = server_sock.accept()
            self.accept_connection(client_sock, address)

    def accept_connection(self, client_sock, address):
        data = client_sock.recv(1024)
        if data == b'GET_ORIENTATION':
            client_sock.send(str(self.orientation))

        client_sock.close()
