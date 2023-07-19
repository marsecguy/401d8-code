#!/usr/bin/env python3

# Libraries
import datetime
import os
import time
import requests

# Declaration of variables
now = datetime.datetime.now()

#In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

#The script must:

#Transmit a single ICMP (ping) packet to a specific IP every two seconds.

#Evaluate the response as either success or failure.

#Assign success or failure to a status variable.

#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

print("Current date and time is:")
print(str(now))

def check_ping():

    while True:
        ping = os.system("ping -c 1 8.8.8.8")
        time.sleep(2)
        print(str(now) + " " + str(ping) + " to 8.8.8.8")
      
        if requests.Response == 0:
            pingstatus = "Host is up"
        else: 
            pingstatus = "Host is down"
        print (pingstatus)
    