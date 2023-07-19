#!/usr/bin/env python3

# Libraries
import datetime
import os
from time import sleep
import requests

# Declaration of variables
now = datetime.datetime.now()

def check_ping(target): 
    ping = os.system("ping -c 1 "+ target)
    
    print(str(now) + " " + str(ping) + " to "+ target)

    if ping == 0:
        pingstatus = "Host is up"
    else: 
        pingstatus = "Host is down"
    print(pingstatus)
    sleep(2)

#In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

#The script must:

#Transmit a single ICMP (ping) packet to a specific IP every two seconds.

#Evaluate the response as either success or failure.

#Assign success or failure to a status variable.

#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

while True:
    check_ping("8.8.8.8")
    
    print("Current date and time is:")
    print(str(now))