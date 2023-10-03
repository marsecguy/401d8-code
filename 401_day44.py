#!/usr/bin/python3

import socket
import time

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: Set a timeout value here.
timeout = time.sleep(10)
sockmod.settimeout(timeout)

# TODO: Collect a host IP from the user.
hostip = input("Enter Host Ip Address: ")
# TODO: Collect a port number from the user, then convert it to an integer data type.
portno = int(input("Enter Port Number: "))

def portScanner(portno):
    # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
    if sockmod.connect((hostip, portno)):
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)

# End

# Resources
#          Python socket module documentation - https://docs.python.org/3/library/socket.html
#          DEMO.md - https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html