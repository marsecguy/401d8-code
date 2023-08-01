#!/usr/bin/python3

# In Python, create a script that prompts the user to select one of the following modes:

# Mode 1: Offensive; Dictionary Iterator
    # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
    # Add a delay between words.
    # Print to the screen the value of the variable.

# Mode 2: Defensive; Password Recognized
    # Accepts a user input string.
    # Accepts a user input word list file path.
    # Search the word list for the user input string.
    # Print to the screen whether the string appeared in the word list.

# Import librabries
import time
import getpass

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
    list = "/home/divermedic/401d8-code/401d8-code/rockyou.txt"
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

def main():
    mode = input("Choose mode: 1 for Offensive, 2 for Defensive or 3 to exit: ")
    if mode == "1":
       iterator()
    elif mode == "2":
       finder()
    elif mode == "3":
        exit
    else:
        print("Invalid slection. Try again.")

main()

# End
