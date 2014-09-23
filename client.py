#!/usr/bin python

import socket
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8000)
print('Connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:
    # Send data
    message = "This is the message. It will be repeated."
    print('sending "%s"' % message, file=sys.stderr)
    sock.send(message.encode())

    data = sock.recv(1024)
    data = data.decode()

    print('received "%s"' % data, file=sys.stderr)
finally:
    print('closing socket', file=sys.stderr)
    sock.close()
