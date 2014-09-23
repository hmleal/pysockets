#!/usr/bin python

import socket
import sys
from threading import Thread


class ConnectionThread(Thread):

    def run(self):
        try:
            # Create a TCP/IP socket
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('localhost', 8000))

            # Send message
            client.send('henrique martins leal'.encode())

            data = client.recv(1024)
            print('received "%s"' % data, file=sys.stderr)
        finally:
            print('Closing socket', file=sys.stderr)
            client.close()


for x in range(2):
    ConnectionThread().start()
