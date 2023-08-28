#!/usr/bin/python3

# In Python create a script that executes from a Linux box to perform the following:

    # Prompts the user to type a URL or IP address.
    # Prompts the user to type a port number.
    # Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
    # Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
    # Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.

# Import libraries
import os
import socket

# Declare variables

# Define functions

    # netcat
def netcat_scan(addr, port):
    
    # Create a socket and a connection (INET = IPv4 / SOCK_STREAM = port)
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((addr, int(port)))

    # Send netcat command
    command = "netcat " + addr + " " + port
    socket1.sendall(command.encode())
    socket1.shutdown(socket.SHUT_WR)

    # Handle the output
    output = socket1.recv(1024)
    clean_output = output.decode()
    
    print(clean_output)

    # Close the connection
    socket1.close()

    # telnet
def telnet_scan(addr, port):

    # Create a socket and a connection (INET = IPv4 / SOCK_STREAM = port)
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((addr, int(port)))

    # Send telnet command
    command = "telnet " + addr + " " + port
    socket1.sendall(command.encode())
    socket1.shutdown(socket.SHUT_WR)

    # Handle the output
    output = socket1.recv(1024)
    clean_output = output.decode()
    print(clean_output)

    # Close the connection
    socket1.close()

    # nmap
def nmap_scan(addr):

    os.system("nmap " + addr)
   
# Main
def main():
    print("Scannning Tool Menu: ")
    addr = input("Enter a URL or IP address: ")
    mode = input("""Choose mode: 
        1 for Netcat scan, 
        2 for Telnet scan,      
        3 for Nmap scan,
        4 to exit: """)
    if mode == "1":
        port = input("Enter a port: ")
        netcat_scan(addr,port)
    elif mode == "2":
        port = input("Enter a port: ")
        telnet_scan(addr,port)
    elif mode == "3":
        nmap_scan(addr)
    elif mode == "4":    
        exit
    else:
        print("Invalid slection. Try again.")

main()

# End 