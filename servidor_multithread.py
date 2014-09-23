#!/usr/bin python


import socket
import sys
import time
from threading import Thread


class Th(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        print('sleep for two seconds')
        time.sleep(2)

    def upper(self):
        return self.text.upper()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)
sock.listen(10)


while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address, file=sys.stderr)

        # Receive the data in small chunks and retransmit it
        data = connection.recv(1024)

        # Makes a thread to process the request
        if data:
            thread = Th(data)
            thread.start()
            connection.sendall(thread.upper())
        else:
            print('no more data from', client_address, file=sys.stderr)
            break
    finally:
        # Clean up the connection
        connection.close()
