#!/usr/bin/python3

# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

# Utilize the scapy library
    # If scapy not installed, first run "pip3 install scapy"
import sys
from scapy.all import sr1, ICMP, IP, TCP

# Define host IP
host = "scanme.nmap.org"

# Define port range or specific set of ports to scan
port_range = 22-80
scr_port = 22-80
dst_port =22-80 

# Test each port in the specified range using a for loop
p=sr1(IP(dst=host)/ICMP())
if p:
        p.show()

# Send TP packet and define the response
response= sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port, flags="S"),timeout=1, verbose=0)

    # If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
for flags in response: 
    if (response.haslayer(TCP)):
        if (response.getlayer(TCP).flags == 0x12):
            send_rst = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port, flags="R"),timeout=1, verbose=0)
            print(f"{host}:{dst_port} is open")

    # If flag 0x14 received, notify user the port is closed.cd
        elif (response.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed")
    # If no flag is received, notify the user the port is filtered and silently dropped.
        else:
             print("Host is unresponsive")
